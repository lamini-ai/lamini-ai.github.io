# lamini.Lamini.check_job_status

Check the status of a job

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
status = llm.check_job_status(job_id)
```

## Parameters

-   job_id: `str` - unique job id

## Returns

status: `dict` - a dictionary with status information

Scheduled jobs will have the following returned

```
{'status': 'QUEUED'}
```

Just starting jobs will have the following format returned

```
{
    'status': 'TRAINING MODEL',
    'progress': 'Starting Run.',
    'starttime': 1680724301.7032173
}
```

While jobs that have made some progress will have the following format returned

```
{
    'status': 'TRAINING MODEL',
    'progress': 'Progress: 1 iterations out of 2.',
    'starttime': 1680724301.7032173,
    'time_elapsed': '8.602318525314331',
    'average_runtime': '8.602318525314331',
    'estimated_total_time': '16.602318525314331',
    'estimated_time_remaining': '8.602318525314331'
}
```

Completed jobs will have the following format returned

```
{
    'status': 'COMPLETED',
    'progress': 'Progress: 3 iterations out of 3.',
    'starttime': 1680724434.2409794,
    'time_elapsed': '20.019465446472168',
    'average_runtime': '6.673155148824056',
    'estimated_total_time': '20.019465446472168',
    'estimated_time_remaining': '0.0'
}
```

### Statuses

Possible statuses include

```
'SCHEDULED'
'QUEUED'
'LOADING DATA'
'TRAINING MODEL'
'EVALUATING MODEL'
'COMPLETED'
'PARTIALLY COMPLETED'
'FAILED'
'CANCELLED'
```

### Running Information

-   `progress` - A description of the progress made in terms of iterations. Each iteration represents an equal subset of the data.
-   `starttime` - Job starttime, unixtime in seconds
-   `time_elapsed` - Amount of time elapsed since the start time
-   `average_runtime` - Average runtime per iteration in seconds thus far
-   `estimated_total_time` - Estimated total runtime based on average runtime in seconds
-   `estimated_time_remaining` - Estimated total time remaining based on average runtime in seconds
