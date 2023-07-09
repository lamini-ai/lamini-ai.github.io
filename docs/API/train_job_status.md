# GET `/v1/lamini/train/jobs/{job_id}`

Get the status of a training job. You can also see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

## Request

**HTTP Method:** `GET`

**Path:** `https://api.powerml.co/v1/lamini/train/jobs/{job_id}`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Parameters:**

- `{job_id}` - The unique identifier of the training job to be cancelled.

## Response

The response will contain the job id, job status, job start time, and model name.

**Body (JSON):**

- `job_id`: The job id
- `status`: "SCHEDULED" | "CREATED" | "QUEUED" | "LOADING DATA" | "TRAINING MODEL" | "SAVING MODEL" | "EVALUATING MODEL" | "COMPLETED" | "CANCELED" | "FAILED"
- `start_time`: Start time of the object
- `model_name`: The finetuned model name, available after model is saved

## Example

This example cancels the training job with the ID `418`. The request is authenticated using the `test_token` bearer token.

### Request

```bash
curl --location --request GET 'https://api.powerml.co/v1/lamini/train/jobs/418' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json'
```

### Response

```json
{
  "job_id": "418",
  "status": "SCHEDULED" | "CREATED" | "QUEUED" | "LOADING DATA" | "TRAINING MODEL" | "SAVING MODEL" | "EVALUATING MODEL" | "COMPLETED" | "CANCELED" | "FAILED",
  "start_time": "",
  "model_name": "4321dvwgeb9c483750b213afc78b49fe875d43db27d508e821c2e92e2701e018",
}
```
