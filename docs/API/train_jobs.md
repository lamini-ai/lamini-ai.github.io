# GET `/v1/lamini/train/jobs`

Get a list of running jobs and statuses. You can also see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

## Request

- HTTP Method: `GET`
- Path: `https://api.powerml.co/v1/lamini/train/jobs`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`

## Response

The response will contain an answer to the provided question.

- Success Status Code: 200
- Body (JSON):
  - `message` - A message describing whether the job was successfully cancelled or not

```json
{ "message": "cancelled {payload['job_id']}" }
```

# Example

This example cancels the training job with the ID `418`. The request is authenticated using the `test_token` bearer token.

## Request

```bash
curl --location --request GET 'https://api.powerml.co/v1/lamini/train/jobs' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json'
```

## Response

```json
{
  "message": "cancelled 418"
}
```
