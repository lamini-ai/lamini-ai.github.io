# lamini.Lamini.train

Train a LLM. This function will submit a training job and continuously poll until the job is completed. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

Specify the data as an argument to `lamini.Lamini.train` then Lamini will train *only* on that data. Additionally, you may optionally specify the prompt template used to produce training prompts, based on the input data that you have. For more information on prompt templates see [prompt templates](/deprecated/Concepts/prompt_templates).

```python
data = [
    [{"input": "What's your favorite animal?"}, {"output": "dog"}],
    [{"input": "What's your favorite color?"}, {"output": "blue"}],
    ...
]
llm = Lamini(id="example", model_name="meta-llama/Llama-2-7b-chat-hf", prompt_template="{input:input}")
results = llm.train(data)
```

Or we can choose to persist the data (additive) across multiple `save_data` calls and then train on the accumulated data.
```python
llm = Lamini(id="example", model_name="meta-llama/Llama-2-7b-chat-hf")
llm.save_data(data)
results = llm.train()
```
Persisted data will be evicted after a month of storage, and we recommend that you manage your data separately.

Optional Step: If you want to change the default values of the hyper-parameters of the model (like learning rate), you can pass the hyper-parameters you want to modify using the following code

```python
results = llm.train(finetune_args={'learning_rate': 1.0e-4})
```
The default values of the hyper-parameters and key values can be found in the llama_config.yaml file in the configs folder in LLAMA. Currently we support most hyper-parameters in [huggingface's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc. 

## Returns

results: `dict` - a dictionary object with fields `job_id` and `model_name` which can be used to fetch eval results or used to query the finetuned model. In order to query the finetuned model you may use the new `model_name` like so

```python
my_output = llm(my_input, output_type={"output": "string"}, model_name=results['model_name'])
```
