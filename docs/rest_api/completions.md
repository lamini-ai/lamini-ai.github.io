## `/v2/completions`

The v2 completions endpoint allows you to make a POST request to get an LLM inference response to a prompt, optionally with a specified JSON output structure, and provides a `finish_reason` field in the response indicating why each inference request finished.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v2/completions`
- Headers:
    - `Authorization: Bearer $LAMINI_API_KEY`
    - `Content-Type: application/json`
- Example Body (JSON):


```json
{
    "model_name": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "prompt": "What is the hottest day of the year?",
    "output_type": {"answer": "str"},
    "max_new_tokens": 500
}
```

#### Parameters

- Required
    -   `model_name`: `str`, the name of your base or finetuned model. See [Models](../models.md) for a list of available base models.
    -   `prompt`: `str` or `List[str]` for a batch. Ex.
        ```
            [
                "How old is Carl, the llama with a hat?",
                "How old is Paul, the llama with a hat?",
            ]
        ```
- Optional
    -   `output_type`: `Dict[str, str]`. Type schema of the output. Ex.
        ```
        {
            "age": "int",
            "units": "str",
        }
        ```
    The valid types are `str`, `int`, `float`, and `bool`.
    -   `max_new_tokens`: `int`, the maximum number of tokens to generate.
        - Default: `null` (no limit)
        - Setting this value improves pipeline execution speed (knowing the max size of each request+response allows for more efficient scheduling), and improves quality of service for batched requests (it prevents one long response from delaying all other responses).
        - Setting this value too low can lead to cut off responses. If you're also using `output_type`, truncated responses can lead to invalid JSON output.

### Response

If the web request is successful, you will see a response with an answer to the provided questions like below:

- Success Status Code: 200
- Body (JSON):
  - `outputs`: `str` or `List[str]` (if multiple prompts were submitted in the inference request). Contains the inference response for each prompt.
  ```json
    "outputs": [
        {
            "age":10,
            "units":"years"
        },{
            "age":10,
            "units":"years"
        }
    ]
  ```
  - `finish_reason`: `str` or `List[str]` (if multiple prompts were submitted in the inference request - each finish reason corresponds to the prompt at the same index in the `outputs` array).  Indicates the ending state of the inference request.
  ```json
    "finish_reason": ["stop", "stop"]
  ```
  The values for `finish_reason` can be:
    - `stop`: The model completed the response with an EOS or equivalent token. This means the model finished generating the response.
    - `length`: The response reached the maximum number of tokens as set by `max_new_tokens` or other token limit. 
    - `timeout`: The time taken to generate the response exceeded the configured Lamini Platform inference timeout.
  See [Performance](../inference/performance.md) for how to use this information to debug problems and improve performance.

If the request is unsuccessful, the API will return an error code, and the response JSON will contain details about the specific error.

### Example

#### Request

```sh
curl --location 'https://api.lamini.ai/v1/completions' \
    --header 'Authorization: Bearer $LAMINI_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "prompt": [
                "How old is Carl, the llama with a hat?",
                "How old is Paul, the llama with a hat?"
            ],
        "output_type": {
            "age": "int",
            "units": "str"
        }
    }'
```

#### Response

Note the result is a hash, so the order of keys may be different from below.

```json
{
  "outputs": [
    {
      "age": 10,
      "units": "years"
    },
    {
      "age": 10,
      "units": "years"
    }
  ],
  "finish_reason": ["stop", "stop"]
}
```


## `/v1/completions`

This endpoint allows you to make a POST request to complete a task or answer a question with a JSON output.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/completions`
- Headers:
    - `Authorization: Bearer $LAMINI_API_KEY`
    - `Content-Type: application/json`
- Example Body (JSON):


```json
{
    "model_name": "meta-llama/Meta-Llama-3.1-8B-Instruct",
    "prompt": "What is the hottest day of the year?",
    "output_type": {"answer": "str"},
    "max_new_tokens": 1000
}
```

#### Parameters

- Required
    -   `model_name`: `str`, the name of your base or finetuned model
    -   `prompt`: `str` or `List[str]` for a batch, ex.
        ```
            [
                "How old is Carl, the llama with a hat?",
                "How old is Paul, the llama with a hat?",
            ]
        ```
- Optional
    -   `output_type`: `Dict[str, str]`. Type Schema of the output. Ex.
        ```
        {
            "age": "int",
            "units": "str",
        }
        ```
    The valid types are `str`, `int`, `float`, and `bool`.
    -   `max_new_tokens`: `int`, the maximum number of tokens to generate.
        - Default: `null` (no limit)
        - Setting this value improves pipeline execution speed (knowing the max size of each request+response allows for more efficient scheduling), and improves quality of service for batched requests (it prevents one long response from delaying all other responses).
        - Setting this value too low can lead to cut off responses. If you're using `output_type` this can lead to invalid JSON output.

### Response

If the web request is successful, you will see a response with an answer to the provided questions like below:

- Success Status Code: 200
- Body (JSON):
  - Output will be formatted as specified by the `output_type` argument passed in above.
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

```sh
curl --location 'https://api.lamini.ai/v1/completions' \
    --header 'Authorization: Bearer $LAMINI_API_KEY' \
    --header 'Content-Type: application/json' \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "prompt": [
                "How old is Carl, the llama with a hat?",
                "How old is Paul, the llama with a hat?"
            ],
        "output_type": {
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
