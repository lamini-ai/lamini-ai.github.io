# POST `/v1/lamini/train`

Use this API endpoint to train a model. This will train a model using the data you've provided through the `/v1/lamini/data` api, or through adding data to an `id` using the python package's [save_data api](/LLMEngine/save_data/). The response will include a job id and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

## Request

**HTTP Method:** POST

**URL:** `https://api.powerml.co/v1/lamini/train`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Example Body (JSON):**

```json
{
  "id": "APIExample",
  "model_name": "EleutherAI/pythia-410m-deduped"
}
```

## Parameters:

- id (string): The `id` corresponding to the dataset you'd like to train with.
- model_name (string): The base model you'd like to train.

## Response:

The response will include a job id and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train). There are a number of statuses possible, each representing a different stage in the training process.

```
{
    "job_id": "<JOB_ID>",
    "status": "SCHEDULED" | "CREATED" | "LOADING DATA" | "TRAINING MODEL" | "EVALUATING MODEL" | "SAVING MODEL" | "COMPLETED" | "FAILED"
}
```

## Example

### Request

```bash
curl --location 'https://api.powerml.co/v1/lamini/train' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "model_name": "EleutherAI/pythia-410m-deduped"
}'
```

### Response

```json
{
  "job_id": "1512",
  "status": "SCHEDULED"
}
```
