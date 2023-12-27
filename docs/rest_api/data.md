## Endpoint Documentation: `/v1/data`

This endpoint allows you to make a POST request to send input/output pairs to use during RAG (retreival augmented generation). For training, see `/v1/train`.
If you would like to send an input list, please see /v1/data.

### Request

- HTTP Method: POST
- URL: `https://api.lamini.ai/v1/data`
- Headers:
  - `Authorization: Bearer $LAMINI_API_KEY`
  - `Content-Type: application/json`
- Example Body (JSON):

```json
{
  "data": [
    {
      "input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nAre there any step-by-step tutorials or walkthroughs available in the documentation?[/INST]",
      "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/"
    },
    {
      "input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nDoes Lamini have a limit on the number of API requests I can make?",
      "output": "Lamini provides each user with free tokens up front."
    }
  ]
}
```

#### Parameters:

- `id`: `str`, an id which will allow you to iterate on finetuned models.
- `data`: A list of dict pairs. The first dict of each pair represents an input object, and the second dict of each pair represents an output object. The input objects must have the same keys, and the output objects must have the same keys.

### Response

If the web request is successful, you will see a response like below with the dataset ID.

- Success Status Code: 200
- Body (JSON):
  ```json
  { "dataset": "1abdc1e146c9d657336ed39ddbf31532" }
  ```

Otherwise, the request will return an error code, and the response json will contain specific error details like invalid token or incompatible data.

### Example

#### Request

```bash
curl --location 'https://api.lamini.ai/v1/data' \
--header 'Authorization: Bearer $LAMINI_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "data": [
                {"input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nAre there any step-by-step tutorials or walkthroughs available in the documentation?[/INST]", "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/"},
                {"input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nDoes Lamini have a limit on the number of API requests I can make?", "output": "Lamini provides each user with free tokens up front."}
            ]
}'
```

#### Response

```json
{ "dataset": "1abdc1e146c9d657336ed39ddbf31532" }
```
