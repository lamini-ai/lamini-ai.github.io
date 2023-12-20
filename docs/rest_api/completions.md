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
  "stop_tokens": ["\n\n"]
}
```

#### Parameters:

- `model_name`: `str`, the name of your base or finetuned model
- `prompt`: `Union[str, List[str]]`, the prompt or batch of prompts used for inference
- `out_type`: `Optional[Dict[str, str]]`. Optional type schema of the output. Ex.
  ```
      {
          "Answer": "str",
          "Answer2": "int",
      }
  ```
  The valid types are `str`, `int`, `float`, and `bool`. If no out_type is specified, the result will be returned as a string.
- `stop_tokens`: `list[str]`, a list of stop tokens to use. these are used in each field produced in the output.

### Response

If the web request is successful, you will see a response with an answer to the provided questions like below:

- Success Status Code: 200
- Body (JSON):
  - Output will be formatted as specified by the `out_type` argument passed in above.
  ```json
  {
    "Answer": "The hottest day of the year varies depending on the location, but generally, it occurs during the summer months when the sun is closest to the Earth. In many regions, July or August tend to be the hottest months.",
    "Answer2": 4
  }
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.

### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/completions' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "meta-llama/Llama-2-7b-chat-hf",
    "prompt": "What is the hottest day of the year?",
}'
```

#### Response

```json
{
  "output": "The hottest day of the year varies depending on location."
}
```
