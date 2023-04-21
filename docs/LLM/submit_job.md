# llama.LLM.submit_job

Submits a job for processing.

```python
job = LLM.submit_job(input, output_type, *args, **kwargs)
```

## Parameters

-   input: `Union[Type, List[Type]]` - input data
-   output_type: `<class 'llama.types.type.Type'>` - the desired data type of returned ouput

## Returns

job: `dict` - a dictionary with `status` and `job_id` string fields

```
{
    'status': 'SCHEDULED',
    'job_id': '-1579724389638199208'
}
```
