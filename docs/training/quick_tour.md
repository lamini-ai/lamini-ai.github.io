When running inference, with prompt-engineering and RAG, is not enough for your LLM, you can train it. This is harder but will result in better performance, better leverage of your data, and increased knowledge and reasoning capabilities.

There are many ways to train your LLM. We'll cover the most common ones here:

- Basic training: build your own LLM for specific domain knowledge or task with finetuning, domain adaptation, and more
- Better training: customize your training call and evaluate your LLM
- Bigger training: pretrain your LLM on a large dataset, e.g. Wikipedia, to improve its general knowledge

## Basic and better training

=== "Python SDK"

    First, get data and put it in the format that `Lamini` expects, which includes an `input` and `output`.

    Sample data:

    ```python
    {
        "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
        "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/",
    }
    ```

    Now, load more data in that format. We recommend at least 1000 examples to see a difference in training.

    ```python
    data = get_data()
    ```

    <details>
    <summary>Code for <code>get_data()</code></summary>

    ```python
    def get_data():
        data = [
            {
                "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
                "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/",
            },
            {
                "input": "Is the Lamini type system similar to a python type system?",
                "output": "Yes, the Lamini type system is built using Pydantic BaseModel.",
            },
            {
                "input": "Does Lamini have a limit on the number of API requests I can make?",
                "output": "Lamini provides each user with free tokens up front.",
            },
            {
                "input": "What does it mean to cancel a job using the `cancel_job()` function? Can we stop the machine from doing its task?",
                "output": "The `cancel_job()` function is used to stop a training job that is currently running.",
            },
            {
                "input": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does it optimize the model for a specific use case?",
                "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization process. It employs an intelligent algorithm to explore the hyperparameter space and find the optimal combination of values. This is done through techniques such as heuristics, grid search, random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes computational resources to evaluate multiple model instances with different hyperparameter configurations. It incorporates techniques like cross-validation to prevent overfitting and ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine learning workflow and improves the chances of developing high-performing models for specific use cases.",
            },
            {
                "input": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized language model?",
                "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license unless otherwise specified. You keep access and ownership of your own data, and we don't use your data to train models for anyone else but you. For more information, please reach out to Lamini directly.",
            },
            {
                "input": "Can Lamini be used on a regular computer, or do I need specialized hardware or software?",
                "output": "Lamini can be used on a regular computer without any specialized hardware or software by using the python client or REST APIs. It is designed to be easily accessible and user-friendly.  The LLM Engine itself requires GPU accelerated servers capable of running large language models.  Lamini hosts such machines that can be easily connected to, e.g. from a jupyter notebook or python program.  Lamini also offers enterprise deployments of the LLM Engine on your infrastructure.",
            },
            {
                "input": "Does Lamini require an internet connection to work, or can I use it offline?",
                "output": "Lamini requires an internet connection to work, as it is a cloud-based language model. However, you can use it offline by downloading and running a local instance of the Lamini API. To learn more about this deployment process, reach out to the Lamini team.",
            },
            {
                "input": "Can Lamini help me with tasks like translating text or answering questions, or is it focused on generating text?",
                "output": "Lamini is primarily focused on generating text, and it can be used for tasks like summarization and paraphrasing. Lamini can also be used to train a LLM for tasks like translation and question answering. You\u2019re talking to a model trained using Lamini right now!",
            },
            {
                "input": "What is Lamini? Is it like a robot or a computer program?",
                "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not a robot, but rather a tool for building and executing LLMs.",
            },
        ]
        return data
    ```

    </details>

    Next, instantiate the model and train. Track progress and view eval results at [https://app.lamini.ai/train](https://app.lamini.ai/train).

    ```python
    from lamini import Lamini

    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
    llm.data = data
    llm.train()
    ```

    Lamini is designed to have good default hyperparameters, so you don't need to tune them. If, however, you would like the flexibility to drop lower, you can do so through the `train` method:
    ```python
    results = llm.train(finetune_args={'learning_rate': 1.0e-4})
    ```

    More details on overriding default hyperparameters can be found in the [`train` method reference](../lamini_python_class/train.md) of the `Lamini` python class.

=== "REST API"

    ```bash
    curl --location "https://api.lamini.ai/v1/train" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct"
            "data": [
                    {"input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nAre there any step-by-step tutorials or walkthroughs available in the documentation?[/INST]", "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/"},
                    {"input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nDoes Lamini have a limit on the number of API requests I can make?", "output": "Lamini provides each user with free tokens up front."}
                ]
        }'
    ```

    See the [REST API docs](../rest_api/train.md) for more details on training, checking the status of the training job, canceling the job, evaluating the model, loading data, and deleting data.

## Bigger training:

=== "Python SDK"

For training on a large file of data, you can use the `upload_file` function to first upload the file onto the servers.

Say, you have a csv file `test.csv` with the following format:

```csv
user,answer
"Explain the process of photosynthesis","Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things.
"What is the capital of USA?", "Washington, D.C."
....
```

You can use the Lamini to train on this file directly. First, upload the file and specify the input and output keys.

```python
from lamini import Lamini

llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
llm.upload_file("test.csv", input_key="user", output_key="answer")
```

Alternatively, you may pass in a `jsonlines` file which may look like this:

`test.jsonlines`

```json
{"user": "Explain the process of photosynthesis", "answer": "Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things."}
{"user": "What is the capital of USA?", "answer": "Washington, D.C."}
....
```

Then train on this file using the `train` function.

```python
from lamini import Lamini

llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
llm.upload_file("test.jsonlines", input_key="user", output_key="answer")

llm.train(limit=100000)
```

Everytime you upload a file, the subsequent `train` would operate on the latest uploaded file, unless you pass in another dataset via `train(data)`.

You may also just use the `Lamini` interface to train on a file using any other model.
Make sure that the data in the file is in the following format:

`data.json`

```json
[
{"input": "What's your favorite animal?","output": "dog"},
{"input": "What's your favorite color?","output": "blue"},
    ......
]
```

Example code snippet:

```python
llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
llm.upload_file(data.json)
llm.train()
```

<br><br>
