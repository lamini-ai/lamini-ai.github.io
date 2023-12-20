# lamini.Lamini.check_job_status

Check the status of a job

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
status = llm.check_job_status(job_id)
```

## Parameters

- job_id: `str` - unique job id

## Returns

status: `dict` - a dictionary with status information

Scheduled jobs will have the following returned

```
{
    "job_id": 1,
    "status": 'SCHEDULED',
    "start_time": 1680724301.7032173
    "model_name": <MODEL_NAME>,
    "custom_model_name": "my model",
    "is_public": false,
}
```

### Statuses

Possible statuses include

```
'NOT_SCHEDULED'
'SCHEDULED'
'RUNNING'
'DONE'
'ERRORED'
'CANCELED'
```
