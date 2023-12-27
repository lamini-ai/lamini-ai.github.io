# GET `/v1/train/jobs/{job_id}`

Get the status of a training job. You can also see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

## Request

**HTTP Method:** `GET`

**Path:** `https://api.lamini.ai/v1/train/jobs/{job_id}`

**Headers:**

- `Authorization: Bearer $LAMINI_API_KEY`
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

#### While Training

```
{"job_id":2514,"status":"TRAINING MODEL","start_time":"2023-08-09T19:42:46.857931","model_name":null,"custom_model_name":null}
```

### When Completed

```
{"job_id":2514,"status":"COMPLETED","start_time":"2023-08-09T19:42:46.857931","model_name":"3aa98c32d6e9b10f93cd50023cd4befff2085705c32adedb73d4dc217592ef78","custom_model_name":""}
```

## Example

This example cancels the training job with the ID `418`. The request is authenticated using the `LAMINI_API_KEY` bearer token.

### Request

```bash
curl --location --request GET 'https://api.lamini.ai/v1/train/jobs/418' \
--header 'Authorization: Bearer $LAMINI_API_KEY' \
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
