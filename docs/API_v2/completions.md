## Endpoint Documentation: `/v2/lamini/completions`

This endpoint allows you to make a POST request to complete a task or answer a question.

### Request

- HTTP Method: POST
- URL: `https://api.powerml.co/v2/lamini/completions`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):


```json
{
    "id": "<YOUR_LLMENGINE_ID>",
    "model_name": "<YOUR_MODEL_NAME>",
    "in_value": {"question": "What is the hottest day of the year?"},
    "out_type": {"Answer": "An answer to the question"}
}
```

#### Parameters:

-   `id: string`: An id which will allow you to iterate on finetuned models
-   `model_name: string`: The name of your base or finetuned model
-   `in_value`: `Dict[str, T]`, where `T` can be `str`, `int`, `float` or `bool`. Ex.
    ```
        {
            "question": "What is the hottest day of the year?",
            "question2": "What is for lunch?",
        }
    ```
-   `out_type`: Dict[str, str]. Type Schema of the output. Ex.
    ```
        {
            "Answer": "An answer to the question",
            "Answer2": "An answer to the question2",
        }
      You can optionally specify the type by appending `#<type>` to the key.  For example,
        ```
            "Answer#int": "An answer to the question",
        ```
      The default type is `str`.  The valid types are `int`, `float`, `bool`, and `str`.
    ```

### Response

The response will contain an answer to the provided questions.

- Success Status Code: 200
- Body (JSON):
  - Output will be formatted as specified by the `out_type` argument passed in above. 
```json
{
    "Answer": "The hottest day of the year varies depending on the location, but generally, it occurs during the summer months when the sun is closest to the Earth. In many regions, July or August tend to be the hottest months.",
    "Answer2": "..."
}
```


### Example

#### Request

```bash
curl --location 'https://api.powerml.co/v2/lamini/completions' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{                                                                                                        
    "id": "LaminiTest",                                                                                          
    "model_name": "text-davinci-003",                                                                            
    "in_value": {                                                                                                
      "question": "What is the hottest day of the year?",                                                        
      "question2": "What is for lunch?",                                                                         
      "question3": "How many inches in a foot?"
    },                                                                                                           
    "out_type": {                                                                                                
      "Answer": "An answer to the question",                                                                     
      "Answer2": "An answer to the question2",                                                                   
      "Answer3#int": "An answer to the question3"                                                               
    }                                                                                                            
}'
```

#### Response

```json
{
 "Answer3": 12,
 "Answer2": "Lunch options depend on individual preferences.",
 "Answer":"The hottest day of the year varies depending on location."
}
```

