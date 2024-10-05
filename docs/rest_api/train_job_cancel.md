## `/v1/train/jobs/{job_id}/cancel`

!!! note

    You can cancel a job by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

Cancel a scheduled or running training job.

## Request

- HTTP Method: `POST`
- URL: `https://api.lamini.ai/v1/train/jobs/{job_id}/cancel`
- Headers:
    - `Authorization: Bearer $LAMINI_API_KEY`
    - `Content-Type: application/json`

**Parameters**

- `{job_id}` - The unique identifier of the training job to be cancelled.

## Example

This example cancels the training job with the ID `418`. The request is authenticated using the `$LAMINI_API_KEY` bearer token.

### Request

```bash
curl --location --request POST 'https://api.lamini.ai/v1/train/jobs/418/cancel' \
  --header 'Authorization: Bearer $LAMINI_API_KEY' \
  --header 'Content-Type: application/json'
```

### Response

```json
{
  "message": "cancelled 418"
}
```
