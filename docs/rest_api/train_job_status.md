## Endpoint Documentation: `/v1/train/jobs/{job_id}`

!!! note

    You can see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

Get the status of a training job.

## Request

- HTTP Method: `GET`
- Path: `https://api.lamini.ai/v1/train/jobs/{job_id}`
- Headers:
    - `Authorization: Bearer <LAMINI_API_KEY>`
    - `Content-Type: application/json`

**Parameters:**

- `{job_id}` - The unique identifier of the training job to be cancelled.

## Response

The response will contain the job id, job status, job start time, and model name.

**Body (JSON):**

- `job_id`: The job id
- `status`: "SCHEDULED" | "CREATED" | "QUEUED" | "LOADING DATA" | "TRAINING MODEL" | "SAVING MODEL" | "EVALUATING MODEL" | "COMPLETED" | "PARTIALLY COMPLETED" | "CANCELED" | "FAILED"
- `start_time`: Start time of the object
- `model_name`: The finetuned model name, available after model is saved

#### While Training

```
{"job_id":2514,"status":"TRAINING MODEL","start_time":"2023-08-09T19:42:46.857931","model_name":null,"custom_model_name":null}
```

### When Completed

```
{"job_id":2514,"status":"COMPLETED","start_time":"2023-08-09T19:42:46.857931","model_name":"abcde","custom_model_name":""}
```

### Request

```bash
curl --location --request GET 'https://api.lamini.ai/v1/train/jobs/$JOB_ID' \
  --header 'Authorization: Bearer $LAMINI_API_KEY' \
  --header 'Content-Type: application/json'
```

### Response

```json
{
  "job_id": "123",
  "status": "COMPLETED",
  "start_time": "2023-08-11T03:16:38.899729",
  "model_name": "abcde",
  "custom_model_name": "",
  "is_public": false,
  "history": "[{\"loss\": 4.5333, \"learning_rate\": 1e-05, \"epoch\": 0.1, \"iter_time\": 0.0, \"flops\": 0.0, \"remaining_time\": 0.0, \"step\": 10}, ...]",
  "resume_count": 0,
  "dataset_id": null,
  "resume_limit": 1000
}
```
