# llama.LLMEngine.get_job_results

Get the job results

```python
llm = LLMEngine(id="example", model_name="meta-llama/Llama-2-7b-chat-hf")
status = llm.get_job_results(job_id, output_type)
```

## Parameters

-   job_id: `str` - unique job id
-   output_type: `<class 'llama.types.type.Type'>` - the desired data type of returned ouput

## Returns

output: `list` - a list of Type objects
