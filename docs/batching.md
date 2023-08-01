# Batching

Sometimes you'd like to submit a lot of input data for processing. Our batching interface
is the best way to do so. This interface is not constrained by our API timeout.
Results are made available at set intervals as portions of the job are completed.

```
llm = LLMEngine(id="batch_example")
```

## Submitting a job

Begin by submitting a job for processing. Upon submission, a job id will be returned.

```python
job = llm.submit_inference_job(self, input, output_type, *args, **kwargs)
```

## Checking the status of a job

Use this utility to check the status of a job.

```python
status = llm.check_job_status(self, job_id)
```

Possible statuses include

```
'NOT_SCHEDULED'
'SCHEDULED'
'RUNNING'
'DONE'
'ERRORED'
'CANCELED'
```

-   `NOT_SCHEDULED` - That job is not scheduled to run. Submit another job
-   `SCHEDULED` - That job is in our queue
-   `RUNNING` - Job is currently running
-   `DONE` - Job is completed
-   `ERRORED` - Job encountered an error. This job will be retried and rescheduled automatically.
-   `CANCELED` - Job was canceled. Submit another job.

## Get job results

Once the job is completed, or once progress has been made, get those results with this utility.

```python
results = llm.get_job_results(job_id, output_type)
```

## Cancelling a job

At any point in the job execution, you can cancel the running job.

```python
llm.cancel_job(job_id)
```

You'll still be able to get job results after canceling.
