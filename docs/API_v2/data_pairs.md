## Endpoint Documentation: `/v2/lamini/data_pairs`

This endpoint allows you to make a POST request to send data pairs to the LaminiTest model for processing.
If you would like to save non-paired data, please see /v2/lamini/data.

### Request

- HTTP Method: POST
- URL: `https://api.powerml.co/v2/lamini/data_pairs`
- Headers:
  - `Authorization: Bearer test_token`
  - `Content-Type: application/json`
- Example Body (JSON):
```json
{
    "id": "LaminiTest",
    "data": [
              [{"name": "Larry", "height": 4}, {"speed": 1.0}],
              [{"name": "Cici", "height": 100}, {"speed": 1.2}],
	    ]
}
```

#### Parameters:

-   `model_name: string`: The name of your model
-   `data`: A list of dict pairs.  The first dict of each pair represents an input object, and the second dict of each pair represents an output object.  The input objects must have the same keys, and the output objects must have the same keys.

### Response

The response is the dataset ID.

- Success Status Code: 200
- Body (JSON):
```json
{"dataset":"1234"}
```

### Example

#### Request

```bash
curl --location 'https://api.powerml.co/v2/lamini/data_pairs' \
--header 'Authorization: Bearer test_token' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "data": [
              [{"name": "Larry", "height": 4}, {"speed": 1.0}],
              [{"name": "Cici", ""height": 100}, {"speed": 1.2}]
	    ]
}'
```

#### Response

```json
{"dataset":"20ef5fd0375f389bc9f9a2e6615dd464"}
```