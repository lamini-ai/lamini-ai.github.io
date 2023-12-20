## Endpoint Documentation: `/v1/data`

This endpoint allows you to make a POST request to send input/output pairs to use during RAG (retreival augmented generation). For training, see `/v1/train`.
If you would like to send an input list, please see /v1/data.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/data`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):

```json
{
  "data": [
    { "name": "Larry", "height": 4, "speed": 1.0 },
    { "name": "Cici", "height": 100, "speed": 1.2 }
  ]
}
```

#### Parameters:

- `id`: `str`, an id which will allow you to iterate on finetuned models.
- `data`: A list of dict pairs. The first dict of each pair represents an input object, and the second dict of each pair represents an output object. The input objects must have the same keys, and the output objects must have the same keys.

### Response

If the web request is successful, you will see a response like below with the dataset ID.

- Success Status Code: 200
- Body (JSON):
  ```json
  { "dataset": "1abdc1e146c9d657336ed39ddbf31532" }
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.

### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/data' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "data": [
              [{"name": "Larry", "height": 4}, {"speed": 1.0}],
              [{"name": "Cici", "height": 100}, {"speed": 1.2}]
	    ]
}'
```

#### Response

```json
{ "dataset": "1abdc1e146c9d657336ed39ddbf31532" }
```
