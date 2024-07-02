## Endpoint Documentation: `/v1/train`

Use this API endpoint to train a model. This will train a model with the `dataset_id`. The response will include a job id, dataset id, and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

## Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/train`
- Headers:
      - `Authorization: Bearer $LAMINI_API_KEY`
      - `Content-Type: application/json`

- Example Body (JSON):
To train on an already uploaded dataset

```json
{
  "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
  "dataset_id": "$YOUR_DATASET_ID"
}
```

## Parameters:

- model_name (string): The model you'd like to train on.
- data_or_dataset_id (string): The dataset id you'd like to train on.
## Response:

The response will include a job id and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train). There are a number of statuses possible, each representing a different stage in the tuning process.

```
{
    "job_id": "<JOB_ID>",
    "status": "SCHEDULED" | "CREATED" | "LOADING DATA" | "TRAINING MODEL" | "EVALUATING MODEL" | "SAVING MODEL" | "COMPLETED" | "PARTIALLY COMPLETED" | "FAILED"
}
```

## Example

### Request

```bash
curl --location 'https://api.lamini.ai/v1/train' \
  --header 'Authorization: Bearer $LAMINI_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
      "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
      "data_or_dataset_id": "$YOUR_DATASET_ID",
  }'
```

### Response

```json
{
  "job_id": "55555",
  "status": "SCHEDULED"
}
```
