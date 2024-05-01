## Endpoint Documentation: `/v1/completions`

This endpoint allows you to make a POST request to complete a task or answer a question with a JSON output.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/completions`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):


```json
{
    "model_name": "<YOUR_MODEL_NAME>",
    "prompt": "What is the hottest day of the year?",
    "out_type": {"answer": "str"},
}
```

#### Parameters:

-   `model_name`: `str`, the name of your base or finetuned model
-   `prompt`: `str` or `List[str]` for a batch, ex.
    ```
        [
            "How old is Carl, the llama with a hat?",
            "How old is Paul, the llama with a hat?",
        ]
    ```
-   `out_type`: `Dict[str, str]`. Type Schema of the output. Ex.
    ```
        {
            "age": "int",
            "units": "str",
        }
    ```
    The valid types are `str`, `int`, `float`, and `bool`.

### Response

If the web request is successful, you will see a response with an answer to the provided questions like below:

- Success Status Code: 200
- Body (JSON):
  - Output will be formatted as specified by the `out_type` argument passed in above.
  ```json
    [
        {
            "age":10,
            "units":"years"
        },{
            "age":10,
            "units":"years"
        }
    ]
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.


### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/completions' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
    "prompt": [
            "How old is Carl, the llama with a hat?",
            "How old is Paul, the llama with a hat?"
        ],
    "out_type": {
        "age": "int",
        "units": "str"
    }
}'
```

#### Response

Note the result is a hash, so the order of keys may be different from below.

```json
[{"age":10,"units":"years"},{"age":10,"units":"years"}]
```
