# POST `/v1/lamini/train`

Use this API endpoint to submit a training job. This will train a model using the data you've provided through the `/v1/lamini/data` api, or through adding data to an `id` using the python package's [save_data api](/LLMEngine/save_data/).

### Request

- HTTP Method: POST
- URL: `https://api.powerml.co/v1/lamini/train`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):

```json
{
  "id": "APIExample",
  "model_name": "EleutherAI/pythia-410m-deduped"
}
```

## Parameters:

- id (string): The `id` corresponding to the dataset you'd like to finetune with.
- model_name (string): The base model you'd like to finetune.

## Response:

```
{
    "job_id": ""
    "status": ""
}
```

### Example

#### Request

```bash
curl --location 'https://api.powerml.co/v1/lamini/train' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "model_name": "EleutherAI/pythia-410m-deduped"
}'
```

#### Response

```json
{
  "dataset": 7587574322307826093
}
```
