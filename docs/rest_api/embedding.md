## Endpoint Documentation: `/v1/embedding`

This endpoint allows you to make a POST request to convert a chunk of text into a vector embedding.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/inference/embedding`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):

```json
{
  "prompt": "What is the hottest day of the year?",
}
```

#### Parameters:

- `prompt`: `Union[str, List[str]]`, the prompt or batch of prompts used for inference

### Response

If the web request is successful, you will see a response with the vector embedding like below:

- Success Status Code: 200
- Body (JSON):
  ```json
  {
    "embedding": [0.013080810196697712,-0.05404408276081085, ... ,-0.016650857403874397],
  }
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.

### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/inference/embedding' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "What is the hottest day of the year?",
}'
```

#### Response

```json
{
    "embedding": [0.013080810196697712,-0.05404408276081085, ... ,-0.016650857403874397],
}
```

