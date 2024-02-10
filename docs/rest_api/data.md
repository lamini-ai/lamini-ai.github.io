## Endpoint Documentation: `/v1/data`

This endpoint gives you the data storage URL that you will need to pass during training. For training, see `/v1/train`.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/data`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):
```json
{
    "dataset_id": "lorem_ipsum"
}
```

#### Parameters:

-   `dataset_id` (str): An identifier for the dataset you'd like to use for training.

### Response

If the web request is successful, you will see a response like below with the dataset ID.

- Success Status Code: 200
- Body (JSON):
  ```json
    {"upload_base_path":"azure","dataset_location":"https://laministorage.blob.core.windows.net/training-data/platform/testest?abcdef"}
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.

### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/data' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "dataset_id": "lorem_ipsum"
}'
```

#### Response

```json
{"upload_base_path":"azure","dataset_location":"https://laministorage.blob.core.windows.net/training-data/platform/lorem_ipsum?abcdef"}
```
