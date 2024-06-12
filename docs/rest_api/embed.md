## Endpoint Documentation: `/v1/inference/embedding`

This endpoint allows you to make a POST request to convert a string into a vector embedding (a List[float]).

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/inference/embedding`
- Headers:
      - `Authorization: Bearer $LAMINI_API_KEY`
      - `Content-Type: application/json`
- Example Body (JSON):


```json
{
    "prompt": "How old is Carl, the llama with a hat?",
    "model_name": "sentence-transformers/all-MiniLM-L6-v2"
}
```

#### Parameters:

-   `prompt` : `str` or `List[str]`, the string to embed
-   `model_name` (optional): `str`, the name of a base or finetuned model. Default is `sentence-transformers/all-MiniLM-L6-v2`.

### Response

If the web request is successful, you will see a response with an answer to the provided questions like below:

- Success Status Code: 200
- Body (JSON):
  ```json
     {
        "embedding":[0.013080810196697712,-0.05404408276081085, ... ]
     }
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.


### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/inference/embedding' \
   --header 'Authorization: Bearer $LAMINI_API_KEY' \
   --header 'Content-Type: application/json' \
   --data '{ "prompt": "How are you?  Rate on a scale of 1 to 5." }'
```

#### Response

```json
{
   "embedding":[0.013080810196697712,-0.05404408276081085, ... ]
}
```
