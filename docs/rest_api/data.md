## Endpoint Documentation: `/v2/lamini/data`

This endpoint allows you to make a POST request to send an data for Lamini to use during RAG (retreival augmented generation). For training, see `/v2/lamini/train`.
If you would like to send a list or input/output pairs, please see `/v2/lamini/data_pairs`.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v2/lamini/data`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):
```json
{
    "id": "LaminiTest",
    "data": [{"document": "lorem"}, {"document": "ipsum"}]
}
```

#### Parameters:

-   `id`: `str`, an id which will allow you to iterate on finetuned models.
-   `data`: A list of dicts specifying datapoints available to the model all formatted in the same way. Each key in the dict must be a str, and each value must be a str, int, float, or bool.  The dicts must have the same keys.  In addition, `data` can also be a single dict.

### Response

If the web request is successful, you will see a response like below with the dataset ID.

- Success Status Code: 200
- Body (JSON):
  ```json
    {"dataset":"12bc9e7a36f2cad3d70ad6c55994536d"}
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.

### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v2/lamini/data' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "data": [{"name": "Larry", "height": 4}, {"name": "Cici", "height": 100}]
}'
```

#### Response

```json
{"dataset":"12bc9e7a36f2cad3d70ad6c55994536d"}
```