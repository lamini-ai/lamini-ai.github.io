---
hide:
  - navigation
---

# Module `lamini.api.lamini` (lamini-3.2.3)

Want to see more? Check out our full open source repo: [https://github.com/lamini-ai/lamini](https://github.com/lamini-ai/lamini).

## Classes

``` python
Lamini(
    model_name: str,
    api_key: Optional[str] = None,
    api_url: Optional[str] = None,
)
```

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
class Lamini:
    def __init__(
        self,
        model_name: str,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
    ):
        self.config = get_config()
        self.model_name = model_name
        self.api_key = api_key
        self.api_url = api_url
        self.completion = Completion(api_key, api_url)
        self.trainer = Train(api_key, api_url)
        self.upload_file_path = None
        self.upload_base_path = None

    def version(self):
        return get_version(self.api_key, self.api_url, self.config)

    def generate(
        self,
        prompt: Union[str, List[str]],
        model_name: Optional[str] = None,
        output_type: Optional[dict] = None,
        max_tokens: Optional[int] = None,
        max_new_tokens: Optional[int] = None,
    ):
        result = self.completion.generate(
            prompt=prompt,
            model_name=model_name or self.model_name,
            output_type=output_type,
            max_tokens=max_tokens,
            max_new_tokens=max_new_tokens,
        )
        if output_type is None:
            if isinstance(prompt, list):
                result = [single_result["output"] for single_result in result]
            else:
                result = result["output"]
        return result

    async def async_generate(
        self,
        prompt: Union[str, List[str]],
        model_name: Optional[str] = None,
        output_type: Optional[dict] = None,
        max_tokens: Optional[int] = None,
        max_new_tokens: Optional[int] = None,
    ):
        req_data = self.completion.make_llm_req_map(
            prompt=prompt,
            model_name=model_name or self.model_name,
            output_type=output_type,
            max_tokens=max_tokens,
            max_new_tokens=max_new_tokens,
        )
        result = await self.completion.async_generate(req_data)
        if output_type is None:
            if isinstance(prompt, list):
                result = [single_result["output"] for single_result in result]
            else:
                result = result["output"]
        return result

    def upload_data(
        self,
        data: Iterable[Dict[str, Union[int, float, str, bool, Dict, List]]],
        is_public: Optional[bool] = None,
    ):
        num_datapoints = 0

        def get_data_str(d):
            nonlocal num_datapoints
            for item in d:
                num_datapoints += 1
                yield json.dumps(item) + "\n"

        if not data:
            raise ValueError("Data pairs cannot be empty.")

        output = self.trainer.get_upload_base_path()
        self.upload_base_path = output["upload_base_path"]

        try:
            if self.upload_base_path == "azure":
                data_str = get_data_str(data)
                response = self.trainer.create_blob_dataset_location(
                    self.upload_base_path, is_public
                )
                self.upload_file_path = response["dataset_location"]
                upload_to_blob(data_str, self.upload_file_path)
                self.trainer.update_blob_dataset_num_datapoints(
                    response["dataset_id"], num_datapoints
                )
                print("Data pairs uploaded to blob.")
            else:
                response = self.trainer.upload_dataset_locally(
                    self.upload_base_path, is_public, data
                )
                self.upload_file_path = response["dataset_location"]
                print("Data pairs uploaded to local.")

            print(response)
            print(
                f"\nYour dataset id is: {response['dataset_id']} . Consider using this in the future to train using the same data. \nEg: "
                f"llm.train(data_or_dataset_id='{response['dataset_id']}')"
            )

        except Exception as e:
            print(f"Error uploading data pairs: {e}")
            raise e

        return response["dataset_id"]

    def upload_file(
        self, file_path: str, input_key: str = "input", output_key: str = "output"
    ):
        items = self._upload_file_impl(file_path, input_key, output_key)
        try:
            dataset_id = self.upload_data(items)
            return dataset_id
        except Exception as e:
            print(f"Error reading data file: {e}")
            raise e

    def _upload_file_impl(
        self, file_path: str, input_key: str = "input", output_key: str = "output"
    ):
        if os.path.getsize(file_path) > 1e10:
            raise Exception("File size is too large, please upload file less than 10GB")

        # Convert file records to appropriate format before uploading file
        items = []
        if file_path.endswith(".jsonl") or file_path.endswith(".jsonlines"):
            with open(file_path) as dataset_file:

                for row in jsonlines.Reader(dataset_file):
                    yield {"input": row[input_key], "output": row.get(output_key, "")}

        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path).fillna("")
            data_keys = df.columns
            if input_key not in data_keys:
                raise ValueError(
                    f"File must have input_key={input_key} as a column (and optionally output_key={output_key}). You "
                    "can pass in different input_key and output_keys."
                )

            try:
                for _, row in df.iterrows():
                    yield {
                        "input": row[input_key],
                        "output": row.get(output_key, ""),
                    }
            except KeyError:
                raise ValueError("Each object must have 'input' and 'output' as keys")

        else:
            raise Exception(
                "Upload of only csv and jsonlines file supported at the moment."
            )
        return items

    def train(
        self,
        data_or_dataset_id: Union[
            str, Iterable[Dict[str, Union[int, float, str, bool, Dict, List]]]
        ],
        finetune_args: Optional[dict] = None,
        gpu_config: Optional[dict] = None,
        is_public: Optional[bool] = None,
        **kwargs,
    ):
        if isinstance(data_or_dataset_id, str):
            dataset_id = data_or_dataset_id
        else:
            dataset_id = self.upload_data(data_or_dataset_id, is_public=is_public)
        assert dataset_id is not None
        base_path = self.trainer.get_upload_base_path()
        self.upload_base_path = base_path["upload_base_path"]
        existing_dataset = self.trainer.get_existing_dataset(
            dataset_id, self.upload_base_path
        )
        self.upload_file_path = existing_dataset["dataset_location"]

        job = self.trainer.train(
            model_name=self.model_name,
            dataset_id=dataset_id,
            upload_file_path=self.upload_file_path,
            finetune_args=finetune_args,
            gpu_config=gpu_config,
            is_public=is_public,
        )
        job["dataset_id"] = dataset_id
        return job

    # Add alias for tune
    tune = train

    # continuously poll until the job is completed
    def train_and_wait(
        self,
        data_or_dataset_id: Union[
            str, Iterable[Dict[str, Union[int, float, str, bool, Dict, List]]]
        ],
        finetune_args: Optional[dict] = None,
        gpu_config: Optional[dict] = None,
        is_public: Optional[bool] = None,
        **kwargs,
    ):
        job = self.train(
            data_or_dataset_id,
            finetune_args=finetune_args,
            gpu_config=gpu_config,
            is_public=is_public,
        )

        try:
            status = self.check_job_status(job["job_id"])
            if status["status"] == "FAILED":
                print(f"Job failed: {status}")
                return status

            while status["status"] not in (
                "COMPLETED",
                "PARTIALLY COMPLETED",
                "FAILED",
                "CANCELLED",
            ):
                if kwargs.get("verbose", False):
                    print(f"job not done. waiting... {status}")
                time.sleep(30)
                status = self.check_job_status(job["job_id"])
                if status["status"] == "FAILED":
                    print(f"Job failed: {status}")
                    return status
                elif status["status"] == "CANCELLED":
                    print(f"Job canceled: {status}")
                    return status
            print(
                f"Finetuning process completed, model name is: {status['model_name']}"
            )
        except KeyboardInterrupt as e:
            print("Cancelling job")
            return self.cancel_job(job["job_id"])

        return status

    # Add alias for tune
    tune_and_wait = train_and_wait

    def cancel_job(self, job_id=None):
        return self.trainer.cancel_job(job_id)

    def cancel_all_jobs(
        self,
    ):
        return self.trainer.cancel_all_jobs()

    def resume_job(self, job_id=None):
        return self.trainer.resume_job(job_id)

    def check_job_status(self, job_id=None):
        return self.trainer.check_job_status(job_id)

    def get_jobs(self):
        return self.trainer.get_jobs()

    def evaluate(self, job_id=None):
        return self.trainer.evaluate(job_id)
```

</details>

``` python
MemoryRAG(
    job_id: int = None,
    api_key: Optional[str] = None,
    api_url: Optional[str] = None,
    model_name: str = "meta-llama/Llama-3.2-3B-Instruct",
)
```

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

```python
class MemoryRAG:

    def __init__(
        self,
        job_id: int = None,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
        model_name: str = "meta-llama/Llama-3.2-3B-Instruct",
    ):
        self.job_id = job_id
        self.config = get_config()
        self.api_key = api_key or lamini.api_key or get_configured_key(self.config)
        self.api_url = api_url or lamini.api_url or get_configured_url(self.config)
        self.api_prefix = self.api_url + "/alpha/memory-rag"
        self.model_name = model_name

    def memory_index(
        self,
        documents: List,
    ) -> str:
        if self.model_name is None:
            raise Exception("model_name must be set in order to use memory_index")
        payload = {"model_name": self.model_name}

        files = [
            (
                "files",
                (
                    file_path,
                    open(file_path, "rb"),
                ),
            )
            for file_path in documents
        ]
        headers = {
            "Authorization": f"Bearer {self.api_key}",
        }
        response = requests.request(
            "POST",
            self.api_prefix + f"/train",
            headers=headers,
            data=payload,
            files=files,
        )

        json_response = response.json()
        self.job_id = json_response["job_id"]
        return json_response

    def status(self) -> str:
        if self.job_id is None:
            raise Exception("job_id must be set in order to get status")
        params = {"job_id": self.job_id}
        resp = make_web_request(
            self.api_key, self.api_prefix + f"/status", "post", params
        )
        return resp

    def query(self, prompt: str, k: int = 3) -> str:
        if self.job_id is None:
            raise Exception("job_id must be set in order to query")
        params = {
            "prompt": prompt,
            "model_name": self.model_name,
            "job_id": self.job_id,
            "rag_query_size": k,
        }
        resp = make_web_request(
            self.api_key,
            self.api_prefix + f"/completions",
            "post",
            params,
        )
        return resp

    def add_index(self, prompt: str) -> str:
        if self.job_id is None:
            raise Exception("job_id must be set in order to add to index")
        params = {"prompt": prompt, "job_id": self.job_id}
        resp = make_web_request(
            self.api_key,
            self.api_prefix + f"/add-index",
            "post",
            params,
        )
        return resp

    def get_logs(self) -> List[str]:
        """Get training logs for a memory RAG job.

        Args:
            job_id: The ID of the memory RAG job

        Returns:
            List of log lines
        """
        if self.job_id is None:
            raise Exception("job_id must be set in order to get job logs")
        resp = make_web_request(
            self.api_key,
            self.api_prefix + f"/training_log/{self.job_id}",
            "get",
        )
        return resp
```

</details>

### Methods

#### `cancel_all_jobs`
>
> Cancel all jobs associated with your key.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def cancel_all_jobs(
    self,
):
    return self.trainer.cancel_all_jobs()
```

</details>

#### `cancel_job`
>
> Cancel the job or specify a job id to cancel.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def cancel_job(self, job_id=None):
    return self.trainer.cancel_job(job_id)
```

</details>

#### `check_job_status`
>
> Check the status of the job or a given job id.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def check_job_status(self, job_id=None):
    '''
    Possible statuses include:
    'SCHEDULED'
    'QUEUED'
    'LOADING DATA'
    'TRAINING MODEL'
    'EVALUATING MODEL'
    'COMPLETED'
    'PARTIALLY COMPLETED'
    'FAILED'
    'CANCELLED'
    '''
    return self.trainer.check_job_status(job_id)
```

</details>

#### `generate`
>
> Run inference on the model or a given model.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def generate(
    self,
    prompt: Union[str, List[str]],
    model_name: Optional[str] = None,
    output_type: Optional[dict] = None,
    max_tokens: Optional[int] = None,
    max_new_tokens: Optional[int] = None,
):
    result = self.completion.generate(
        prompt=prompt,
        model_name=model_name or self.model_name,
        output_type=output_type,
        max_tokens=max_tokens,
        max_new_tokens=max_new_tokens,
    )
    if output_type is None:
        if isinstance(prompt, list):
            result = [single_result["output"] for single_result in result]
        else:
            result = result["output"]
    return result
```

</details>

#### `get_jobs`
>
> Get information on all jobs associated with your key.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def get_jobs(self):
    return self.trainer.get_jobs()
```

</details>

#### `resume_job`
>
> Resume `CANCELLED`, `PARTIALLY COMPLETED`, `FAILED`, or `COMPLETED` job.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def resume_job(self, job_id=None):
    return self.trainer.resume_job(job_id)
```

</details>

#### `train`
>
> Train a job.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def train(
    self,
    data_or_dataset_id: Union[
        str, Iterable[Dict[str, Union[int, float, str, bool, Dict, List]]]
    ],
    finetune_args: Optional[dict] = None,
    gpu_config: Optional[dict] = None,
    is_public: Optional[bool] = None,
    **kwargs,
):
    if isinstance(data_or_dataset_id, str):
        dataset_id = data_or_dataset_id
    else:
        dataset_id = self.upload_data(data_or_dataset_id, is_public=is_public)
    assert dataset_id is not None
    base_path = self.trainer.get_upload_base_path()
    self.upload_base_path = base_path["upload_base_path"]
    existing_dataset = self.trainer.get_existing_dataset(
        dataset_id, self.upload_base_path
    )
    self.upload_file_path = existing_dataset["dataset_location"]

    job = self.trainer.train(
        model_name=self.model_name,
        dataset_id=dataset_id,
        upload_file_path=self.upload_file_path,
        finetune_args=finetune_args,
        gpu_config=gpu_config,
        is_public=is_public,
    )
    job["dataset_id"] = dataset_id
    return job
```

</details>

#### `tune`
>
> Aliases to `train`.
<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
tune = train
```

</details>

#### `train_and_wait`
>
> Train a job, synchronous.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def train_and_wait(
    self,
    data_or_dataset_id: Union[
        str, Iterable[Dict[str, Union[int, float, str, bool, Dict, List]]]
    ],
    finetune_args: Optional[dict] = None,
    gpu_config: Optional[dict] = None,
    is_public: Optional[bool] = None,
    **kwargs,
):
    job = self.train(
        data_or_dataset_id,
        finetune_args=finetune_args,
        gpu_config=gpu_config,
        is_public=is_public,
    )

    try:
        status = self.check_job_status(job["job_id"])
        if status["status"] == "FAILED":
            print(f"Job failed: {status}")
            return status

        while status["status"] not in (
            "COMPLETED",
            "PARTIALLY COMPLETED",
            "FAILED",
            "CANCELLED",
        ):
            if kwargs.get("verbose", False):
                print(f"job not done. waiting... {status}")
            time.sleep(30)
            status = self.check_job_status(job["job_id"])
            if status["status"] == "FAILED":
                print(f"Job failed: {status}")
                return status
            elif status["status"] == "CANCELLED":
                print(f"Job canceled: {status}")
                return status
        print(
            f"Finetuning process completed, model name is: {status['model_name']}"
        )
    except KeyboardInterrupt as e:
        print("Cancelling job")
        return self.cancel_job(job["job_id"])

    return status
```

</details>

#### `upload_data`
>
> Upload data, most commonly a list of dictionaries with `input` and `output` keys.

<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def upload_data(
    self,
    data: Iterable[Dict[str, Union[int, float, str, bool, Dict, List]]],
    is_public: Optional[bool] = None,
):
    num_datapoints = 0

    def get_data_str(d):
        nonlocal num_datapoints
        for item in d:
            num_datapoints += 1
            yield json.dumps(item) + "\n"

    if not data:
        raise ValueError("Data pairs cannot be empty.")

    output = self.trainer.get_upload_base_path()
    self.upload_base_path = output["upload_base_path"]

    try:
        if self.upload_base_path == "azure":
            data_str = get_data_str(data)
            response = self.trainer.create_blob_dataset_location(
                self.upload_base_path, is_public
            )
            self.upload_file_path = response["dataset_location"]
            upload_to_blob(data_str, self.upload_file_path)
            self.trainer.update_blob_dataset_num_datapoints(
                response["dataset_id"], num_datapoints
            )
            print("Data pairs uploaded to blob.")
        else:
            response = self.trainer.upload_dataset_locally(
                self.upload_base_path, is_public, data
            )
            self.upload_file_path = response["dataset_location"]
            print("Data pairs uploaded to local.")

        print(
            f"\nYour dataset id is: {response['dataset_id']} . Consider using this in the future to train using the same data. \nEg: "
            f"llm.train(data_or_dataset_id='{response['dataset_id']}')"
        )

    except Exception as e:
        print(f"Error uploading data pairs: {e}")
        raise e

    return response["dataset_id"]
```

</details>

#### `upload_file`
>
> Upload data as a file, can be `csv` or `jsonl`.
<details class="source">

<summary>

<span>Expand source code</span>

</summary>

``` python
def upload_file(
    self, file_path: str, input_key: str = "input", output_key: str = "output"
):
    items = self._upload_file_impl(file_path, input_key, output_key)
    try:
        dataset_id = self.upload_data(items)
        return dataset_id
    except Exception as e:
        print(f"Error reading data file: {e}")
        raise e
```

</details>

## lamini.api.memory_rag

### initialize

Creates a Memory RAG object.

```python
from lamini import MemoryRAG
client = MemoryRAG(job_id=1,model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
```


#### Parameters

- `job_id`: Name of an existing memory rag index.
- `api_key`: Lamini API key.
- `api_url`: Lamini API URL.
- `model_name`: Optional name of base model to use for Memory RAG Index building or inference.


### Build Memory RAG Index

Start a Memory RAG build job.

```python
lamini_wikipedia_page_pdf = "<path-to-file>.pdf"
response = client.memory_index(documents=[lamini_wikipedia_page_pdf])

print(response)
### {'job_id': 27666, 'status': 'created'}
```

Wait for Memory RAG train job to finish.

```python
while status["status"] == "running":
    time.sleep(5)
    status = client.status(job_id)
    print(status["status"])
### running
### running
### running
### completed
```

#### Parameters

- `documents`: List of paths (strings)to local files for building the Memory Rag index.

#### Returns

Dictionary containing job information including:

- `job_id`: ID of the training job
- `status`: Job ENUM status: {"created", "running", "completed", "failed"}


## lamini.classify.lamini_classifier

### initialize

Creates a new classifier project and kicks off the initial data generation and training process.

```python
def initialize(
    name: str,
    classes: List[str],
    examples: Dict[str, List[str]],
    model_name: Optional[str] = None
) -> Dict[str, str]
```

#### Parameters

- `name`: Name for the classifier project. Must be unique for the user.
- `classes`: List of class names that the classifier will be trained to identify.
- `examples`: Dictionary mapping class names to lists of example texts for each class.
- `model_name`: Optional name of base model to use for classification.

#### Returns

Dictionary containing:

- `name`: Name of the created project
- `job_id`: ID of the training job that was initiated

#### Raises

- `HTTPException(497)`: If a project with the given name already exists
- `HTTPException(499)`: If project creation fails

#### Example

```python
from lamini.classify.lamini_classifier import LaminiClassifier
classifier = Classifier()
result = classifier.initialize(
    name="sentiment_classifier",
    classes=["positive", "negative"],
    examples={
        "positive": ["great movie!", "loved it"],
        "negative": ["terrible film", "waste of time"]
    }
)
print(f"Created project {result['name']} with job {result['job_id']}")
```

### train

Train a classifier model on provided data.

```python
def train(
    data_or_dataset_id: Union[str, List[Dict]],
    finetune_args: Optional[dict] = None,
    gpu_config: Optional[dict] = None,
    is_public: Optional[bool] = None,
    **kwargs
) -> Dict[str, str]
```

#### Parameters

- `data_or_dataset_id`: Either a dataset ID string or list of training examples
- `finetune_args`: Optional dictionary of fine-tuning parameters
- `gpu_config`: Optional GPU configuration settings
- `is_public`: Whether to make the trained model public

#### Returns

Dictionary containing job information including:

- `job_id`: ID of the training job
- `dataset_id`: ID of the dataset used for training

### classify

Run classification on input text using a trained model.

```python
def classify(
    prompt: Union[str, List[str]], 
    top_n: Optional[int] = None,
    threshold: Optional[float] = None,
    metadata: Optional[bool] = None
) -> Union[str, List[str]]
```

#### Parameters

- `prompt`: Input text or list of texts to classify
- `top_n`: Optional number of top predictions to return
- `threshold`: Optional confidence threshold for predictions
- `metadata`: Whether to return prediction metadata

#### Returns

Predicted class(es) for the input text(s)

#### Example

```python
cls.classify("woof")
```

```json
{
  "classification": [
    [
      {
        "class_id": 1,
        "class_name": "dog",
        "prob": 0.9263275590881269
      },
      {
        "class_id": 0,
        "class_name": "cat",
        "prob": 0.2736724409118731
      }
    ]
  ]
}
```

### add

Add additional training examples to an existing classifier project.

```python
def add(
    project_name: str,
    dataset_name: str,
    data: Dict[str, List[str]]
) -> Dict[str, bool]
```

#### Parameters

- `project_name`: Name of the existing classifier project
- `dataset_name`: Name for the new dataset being added
- `data`: Dictionary mapping class names to lists of example texts

#### Returns

Dictionary containing:

- `success`: Boolean indicating if examples were added successfully

#### Example

```python
classifier.add(
    project_name="sentiment_classifier",
    dataset_name="additional_examples",
    data={
        "positive": ["excellent work", "fantastic results"],
        "negative": ["poor quality", "disappointing outcome"]
    }
)
```

## lamini.one_evaler.one_evaler

### run

Run evaluation on a model using provided test data.

```python
def run() -> Dict[str, Union[str, List, Dict, str]]
```

#### Parameters

- `test_model_id`: ID of the model to evaluate
- `eval_data`: List of dictionaries with `input` and `target` keys
- `eval_data_id`: name or ID for the evaluation dataset
- `base_model_id`: ID of the base model to compare against (optional)
- `fuzzy`: Whether to perform fuzzy matching of predictions (optional)
- `sbs`: Whether to perform side-by-side comparison with the base model (optional)

#### Returns

Dictionary containing:

- `eval_job_id`: Unique identifier for the evaluation job
- `eval_data_id`: ID of the evaluation dataset used
- `metrics`: Evaluation metrics results
- `status`: Status of the evaluation job ("COMPLETED" or "FAILED")
- `predictions`: List of actual model outputs

#### Example

```python
from lamini.one_evaler import LaminiOneEvaler

evaluator = LaminiOneEvaler(
    test_model_id="my-model-id",
    eval_data=[
        {"input": "text1", "output": "label1"},
        {"input": "text2", "output": "label2"}
    ],
    test_eval_type="classifier"
)

result = evaluator.run()
print(f"Evaluation completed with job ID: {result['eval_job_id']}")
print(f"Metrics: {result['metrics']}")
```

#### Notes

- The evaluation compares model predictions against provided ground truth labels
- Can optionally perform side-by-side (sbs) comparison with a base model
- Supports fuzzy matching of predictions when fuzzy=True
