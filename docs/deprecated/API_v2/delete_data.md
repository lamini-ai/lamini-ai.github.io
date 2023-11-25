# POST `/v2/lamini/delete_data`

Delete data associated with the provided Lamini Engine id.

## Request

**HTTP Method:** `POST`

**Path:** `https://api.powerml.co/v2/lamini/delete_data`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Body (JSON):**

- `id` - The Lamini Engine id you'd like to clear data from.

## Response

The response will contain the job id, job status, job start time, and model name.

**Body (JSON):**

- `deleted`: The number of datasets deleted.

## Example

This example deletes data associated with id `APIExample`.

### Request

```bash
curl --location --request POST 'https://api.powerml.co/v2/lamini/delete_data' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest"
}'
```

### Response

```json
{
  "deleted": 1
}
```
