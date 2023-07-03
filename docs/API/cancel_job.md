# POST `/v1/lamini/train/jobs/{job_id}/cancel`

Cancel a scheduled or running training job.

## Request

- HTTP Method: `POST`
- Path: `https://api.powerml.co/v1/lamini/train/jobs/{job_id}/cancel`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Parameters:
  - `{job_id}` - The unique identifier of the training job to be cancelled.

## Response

The response will contain an answer to the provided question.

- Success Status Code: 200
- Body (JSON):
  - `message` - A message describing whether the job was successfully cancelled or not

```json
{ "message": "cancelled {payload['job_id']}" }
```

# Example

This example cancels the training job with the ID `440`. The request is authenticated using the `test_token` bearer token.

## Request

```bash
curl --location --request POST 'https://api.powerml.co/v1/lamini/train/jobs/440/cancel' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json'
```

## Response

```json
{
  "message": "cancelled 440"
}
```
