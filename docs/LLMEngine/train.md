# llama.LLMEngine.train

Train a LLM. This function will submit a training job and continuously poll until the job is completed. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

```python
llm = LLMEngine(id="example")
llm.save_data(data)
results = llm.train()
```

## Returns

results: `dict` - a dictionary object with fields `job_id` and `model_name` which can be used to fetch eval results or used to query the finetuned model. In order to query the finetuned model you need to use the new `model_name`

```python
my_output = llm(my_input, output_type=MyOutputType, model_name=results['model_name'])
```
