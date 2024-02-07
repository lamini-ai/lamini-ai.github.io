## Endpoint Documentation: `/v1/inference/embed`

This endpoint allows you to make a POST request to convert a string into a vector embedding (a List[float]).

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/inference/embed`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):


```json
{
    "prompt": Union[str, List[str]]
    "model_name": str
}
```

#### Parameters:

-   `model_name`: `str`, the name of your base or finetuned model
-   `prompt` : `str` or `List[str]`, the string to embed

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
curl --location 'https://api.lamini.ai/v1/inference/embed' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{ "prompt": "How are you?  Rate on a scale of 1 to 5." }'
```

#### Response

```json
{
   "embedding":[0.013080810196697712,-0.05404408276081085, ... ]
}
```
