## Endpoint Documentation: `/v1/lamini/train/jobs`

!!! note

    You can see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

Get a list of running jobs and statuses.

## Request

**HTTP Method:** `GET`

**Path:** `https://api.lamini.ai/v1/lamini/train/jobs`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

## Response

**Body (JSON):**

- `message` - A message describing whether the job was successfully cancelled or not

```json
{ "message": "cancelled 418" }
```

## Example

This example cancels the training job with the ID `418`. The request is authenticated using the `LAMINI_API_KEY` bearer token.

### Request

```bash
curl --location --request GET 'https://api.lamini.ai/v1/lamini/train/jobs' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json'
```

### Response

```json
[]
```
