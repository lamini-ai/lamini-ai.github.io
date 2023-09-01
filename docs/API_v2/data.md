## Endpoint Documentation: `/v2/lamini/data`

This endpoint allows you to make a POST request to send an input list to the LaminiTest model for processing.
If you would like to send a list or input/output pairs, please see `/v2/lamini/data_pairs`.

### Request

- HTTP Method: POST
- URL: `https://api.powerml.co/v2/lamini/data`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):
```json
{
    "id": "LaminiTest",
    "data": [{"name": "Larry", "height": 4}, {"name": "Cici", "height": 100}]
}
```

#### Parameters:

-   `id: string`: An id which will allow you to iterate on finetuned models.
-   `data`: A list of dicts specifying datapoints available to the model all formatted in the same way. Each key in the dict must be a str, and each value must be a str, int, float, or bool.  The dicts must have the same keys.  In addition, `data` can also be a single dict.

### Response

The response is the dataset ID.

- Success Status Code: 200
- Body (JSON):
```json
{"dataset":"20ef5fd0375f389bc9f9a2e6615dd464"}
```

### Example

#### Request

```bash
curl --location 'https://api.powerml.co/v2/lamini/data' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "data": [{"name": "Larry", "height": 4}, {"name": "Cici", "height": 100}]
}'
```

#### Response

```json
{"dataset":"20ef5fd0375f389bc9f9a2e6615dd464"}
```