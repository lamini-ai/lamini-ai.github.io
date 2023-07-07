# POST `/v1/lamini/delete_data`

Delete data associated with the provided Lamini Engine id.

## Request

- HTTP Method: `GET`
- Path: `https://api.powerml.co/v1/lamini/delete_data`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Body (JSON):
  - `id` - The Lamini Engine id you'd like to clear data from.

## Response

The response will contain the job id, job status, job start time, and model name.

- Success Status Code: 200
- Body (JSON):
  - `deleted`: The number of datasets deleted.

# Example

This example deletes data associated with id `APIExample`.

## Request

```bash
curl --location --request GET 'https://api.powerml.co/v1/lamini/delete_data' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json'
```

## Response

```json
{
  "deleted": 1
}
```
