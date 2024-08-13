# Module `lamini.api.lamini`

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

### Methods

#### `cancel_all_jobs`
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

