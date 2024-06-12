# Training Quick Start
When running inference, with prompt-engineering and RAG, is not enough for your LLM, you can tune it. This is harder but will result in better performance, better leverage of your data, and increased knowledge and reasoning capabilities.

There are many ways to tune your LLM. We'll cover the most common ones here:

- Basic tuning: build your own LLM for specific domain knowledge or task with finetuning, domain adaptation, and more

- Better tuning: customize your tuning call and evaluate your LLM

- Bigger tuning: pretrain your LLM on a large dataset, e.g. Wikipedia, to improve its general knowledge

In combination with a few techniques, we tune LoRAs (low-rank adapters) on top of a pretrained LLM to get the same performance as finetuning the entire model, but with 266x fewer parameters and 1.09 billion times faster model switching.

This efficiency gain is on and handled by default so you can use the correct model.
## Basic tuning

=== "Python SDK"

    First, get data and put it into an `input` and `output` format. We recommend at least 1000 examples to see a difference in tuning.

    Sample data:

    ```python
    {
        "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
        "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/",
    }
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
                "output": "The `cancel_job()` function is used to stop a tuning job that is currently running.",
            },
            {
                "input": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does it optimize the model for a specific use case?",
                "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization process. It employs an intelligent algorithm to explore the hyperparameter space and find the optimal combination of values. This is done through techniques such as heuristics, grid search, random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes computational resources to evaluate multiple model instances with different hyperparameter configurations. It incorporates techniques like cross-validation to prevent overfitting and ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine learning workflow and improves the chances of developing high-performing models for specific use cases.",
            },
            {
                "input": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized language model?",
                "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license unless otherwise specified. You keep access and ownership of your own data, and we don't use your data to tune models for anyone else but you. For more information, please reach out to Lamini directly.",
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
                "output": "Lamini is primarily focused on generating text, and it can be used for tasks like summarization and paraphrasing. Lamini can also be used to tune a LLM for tasks like translation and question answering. You\u2019re talking to a model tuned using Lamini right now!",
            },
            {
                "input": "What is Lamini? Is it like a robot or a computer program?",
                "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not a robot, but rather a tool for building and executing LLMs.",
            },
        ]
        return data
    ```

    </details>

    Next, instantiate and tune the model!
    ```python
    from lamini import Lamini

    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
    data = get_data()
    llm.tune(data_or_dataset_id=data)
    ```
=== "REST API"
    See the [REST API docs](../rest_api/train.md) for more details on tuning, checking the status of the tuning job, canceling the job, evaluating the model, loading data, and deleting data.

You can track the tuning progress and view eval results at [https://app.lamini.ai/train](https://app.lamini.ai/train).


## Better tuning

Lamini is designed to have good default hyperparameters, so you don't need to tune them. If, however, you would like the flexibility to, you can do so through the `tune` method:

```python hl_lines="3"
results = llm.tune(
    data_or_dataset_id=data,
    finetune_args={'learning_rate': 1.0e-4}
    )
```

Currently we support most hyper-parameters in [HuggingFace's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc.

Common hyperparameters to tune include:

- `learning_rate` (float) - the learning rate of the model

- `early_stopping` (bool) - whether to use early stopping or not

- `max_steps` (int) - the maximum number of steps to train for

- `optim` (str) - the optimizer to use, e.g. `adam` or `sgd`, a string from HuggingFace



## Bigger tuning

If you are tuning on a large file of data, you can use the `upload_file` function to first upload the file onto the servers.

Here is an example with a `test.csv` file:

```csv
user,answer
"Explain the process of photosynthesis","Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things.
"What is the capital of USA?", "Washington, D.C."
....
```

You can use the Lamini to tune on this file directly by uploading the file and specifying the input and output keys.

```python
from lamini import Lamini

llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
dataset_id = llm.upload_file("test.csv", input_key="user", output_key="answer")

llm.tune(data_or_dataset_id=dataset_id)
```

Alternatively, you can also use `jsonlines` files

<details>
    <summary>Using <code>test.jsonl</code></summary>

    ```json
    {"user": "Explain the process of photosynthesis", "answer": "Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things."}
    {"user": "What is the capital of USA?", "answer": "Washington, D.C."}
    ....
    ```

    Then tune on this file using the `tune` function.

    ```python
    from lamini import Lamini

    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
    dataset_id = llm.upload_file("test.jsonl", input_key="user", output_key="answer")

    llm.tune(data_or_dataset_id=dataset_id)
    ```
