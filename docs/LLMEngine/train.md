# llama.LLMEngine.train

Train a LLM. This function will submit a training job and continuously poll until the job is completed. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

We can choose to persist the data (additive) across multiple `save_data` calls and then train on the accumulated data.
```python
llm = LLMEngine(id="example")
llm.save_data(data)
results = llm.train()
```

Or, if you specify the data as an argument to `llama.LLMEngine.train` then Lamini will train *only* on that data.

```python
llm = LLMEngine(id="example")
results = llm.train(data)
```

## Returns

results: `dict` - a dictionary object with fields `job_id` and `model_name` which can be used to fetch eval results or used to query the finetuned model. In order to query the finetuned model you need to use the new `model_name`

```python
my_output = llm(my_input, output_type=MyOutputType, model_name=results['model_name'])
```
