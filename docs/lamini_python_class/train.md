# lamini.Lamini.train

Train a LLM. This function will submit a training job and continuously poll until the job is completed. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

Specify the data as an argument to `lamini.Lamini.train` then Lamini will train _only_ on that data.

```python
data = [
    {"input": "What's your favorite animal?", "output": "dog"},
    {"input": "What's your favorite color?", "output": "blue"},
    ...
]
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
results = llm.train(data)
```

This will return a `dataset_id` which can be used to persist the data across multiple runs.

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
results = llm.train(data="dataset_id")
```

Persisted data will be evicted after a month of storage, and we recommend that you manage your data separately.

Optional Step: If you want to change the default values of the hyper-parameters of the model (like learning rate), you can pass the hyper-parameters you want to modify using the following code

```python
results = llm.train(finetune_args={'learning_rate': 1.0e-4})
```

Currently we support most hyper-parameters in [HuggingFace's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc.

Common hyperparameters to tune include:

- `learning_rate` (float) - the learning rate of the model

- `early_stopping` (bool) - whether to use early stopping or not

- `max_steps` (int) - the maximum number of steps to train for

- `optim` (str) - the optimizer to use, e.g. `adam` or `sgd`, a string from HuggingFace

For models over 3B parameters, parameter-efficient finetuning with LoRAs is turned on by default. For parameter-efficient fine-tuning (PEFT), we support the following hyperparameters:

```python
results = llm.train(peft_args={'task_type': 'CAUSAL_LM'})
```

Common hyperparameters to tune for LoRA/PEFT tuning:

- `r_value` (int)

- `lora_alpha` (int)

- `lora_dropout` (int)

- `target_modules` (list)

- `bias` (str)

- `task_type` (str)

## Returns

results: `dict` - a dictionary object with fields `job_id`, `model_name`, and `dataset_id` which can be used to fetch eval results or used to query the finetuned model. In order to query the finetuned model you may use the new `model_name` like so

```python
my_output = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf").generate("My question")
```
