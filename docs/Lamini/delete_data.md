# lamini.Lamini.train

Train a LLM. This function will submit a training job and continuously poll until the job is completed. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

We can choose to persist the data (additive) across multiple `save_data` calls and then train on the accumulated data.
```python
llm = Lamini(id="example", model_name="meta-llama/Llama-2-7b-chat-hf")
llm.save_data(data)
results = llm.train()
```

Or, if you specify the data as an argument to `llama.Lamini.train` then Lamini will train *only* on that data.

```python
llm = Lamini(id="example", model_name="meta-llama/Llama-2-7b-chat-hf")
results = llm.train(data)
```

Optional Step: If you want to change the default values of the hyper-parameters of the model (like learning rate), you can pass the hyper-parameters you want to modify using the following code

```python
results = llm.train(finetune_args={'learning_rate': 1.0e-4})
```
The default values of the hyper-parameters and key values can be found in the llama_config.yaml file in the configs folder in LLAMA. Currently we support most hyper-parameters in [huggingface's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc. 

## Returns

results: `dict` - a dictionary object with fields `job_id` and `model_name` which can be used to fetch eval results or used to query the finetuned model. In order to query the finetuned model you need to use the new `model_name`

```python
my_output = llm(my_input, output_type=MyOutputType, model_name=results['model_name'])
```
