# POST `/v1/train`

Use this API endpoint to train a model. This will train a model with the data path provided through `/v1/data` api. The response will include a job id, dataset id, and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

## Request

**HTTP Method:** POST

**URL:** `https://api.lamini.ai/v1/train`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Example Body (JSON):**

```json
{
  "model_name": "meta-llama/Llama-2-7b-chat-hf",
  "data": [
    {
        "input": "What are you wearing?",
        "output": "A hat, thank you for asking."
    },
    {
        "input": "What is the hottest day of the year?",
        "output": "Im not sure, but I think its in the summer."
    },
    {
        "input": "What is for lunch?",
        "output": "I want boba."
    }
  ],
  "upload_file_path": "https://laministorage.blob.core.windows.net/training-data/platform/lorem_ipsum?abcdef",
}
```

## Parameters:

- model_name (string): The model you'd like to train on.
- data (list): The data you'd like to train on. This should be a list of dictionaries with input and output keys.
- upload_file_path (string): The data path given from `/v1/data` api.

## Response:

The response will include a job id and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train). There are a number of statuses possible, each representing a different stage in the training process.

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
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "meta-llama/Llama-2-7b-chat-hf",
    "data": [
      {
          "input": "What are you wearing?",
          "output": "A hat, thank you for asking."
      },
      {
          "input": "What is the hottest day of the year?",
          "output": "Im not sure, but I think its in the summer."
      },
      {
          "input": "What is for lunch?",
          "output": "I want boba."
      }
    ],
  "upload_file_path": "https://laministorage.blob.core.windows.net/training-data/platform/lorem_ipsum?abcdef"
}'
```

### Response

```json
{
  "job_id": "1512",
  "status": "SCHEDULED"
}
```
