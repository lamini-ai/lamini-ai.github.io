# POST `/v1/lamini/completions`

This endpoint allows you to make a POST request to obtain a model completion. Input and Output data types are required for the model to properly ingest input data and produce properly formatted output data.

## Request

- HTTP Method: POST
- URL: `https://api.powerml.co/v1/lamini/completions`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):

```json
{
    “id”: “APIExample”,
    “model_name”: "openaccess-ai-collective/wizard-mega-13b",
    “input_type”: {
        “title”: “Question”,
        “properties”: {
            “question”: {
                “description”: “A question”,
                “type”: “string”
            }
        }
    },
    “output_type”: {
        “title”: “Answer”,
        “properties”: {
            “answer”: {
                “description”: “An answer to the question”,
                “type”: “string”
            }
        }
    },
    “input_value”: {
        “question”: “What’s the hottest day of the year?”
    }
}
```

## Parameters

- `id: string`: An id which will allow you to iterate on finetuned models
- `model_name: string`: The name of your base or finetuned model. This can be any openai or huggingface model name.
- `input_type: dict`: Type Schema of the input. Input type must be a dictionary with format
  ```
  {
      “title”: <TYPE_NAME>,
      “properties”: {
          <FIELD_NAME>: {
              “description”: <FIELD_DESCRIPTION>,
              “type”: “string” | “integer” | “number” | “boolean”
          }, ...
      }
  }
  ```
- `output_type: dict`: Type Schema of the output. Output type has the same format as input type.
- `input_value: dict`: An Input Datapoint. Input value must be a dictionary with format
  ```
  {
      <FIELD_NAME>: “Brainstorm 20 compelling headlines for a Facebook ad promoting the Best Business Financing Options for [Business Owners]. Format the output as a table.“,
      ...
  }
  ```

## Response

The response will contain an answer to the provided question.

- Success Status Code: 200
- Body (JSON):
  - Output will be formatted as specified by the `output_type` argument passed in above.

```json
{
    “answer”: “The hottest day of the year varies depending on the location, but generally, it occurs during the summer months when the sun is closest to the Earth. In many regions, July or August tend to be the hottest months.”
}
```

# Example

## Request

```bash
curl --location ‘https://api.powerml.co/v1/lamini/completions’ \
--header ‘Authorization: Bearer <LAMINI_API_KEY>` \
--header ‘Content-Type: application/json’ \
--data ‘{
    “id”: “LaminiTest”,
    “model_name”: “text-davinci-003",
    “input_type”: {
        “title”: “Question”,
        “properties”: {
            “question”: {
                “description”: “A question”,
                “type”: “string”
            }
        }
    },
    “output_type”: {
        “title”: “Answer”,
        “properties”: {
            “answer”: {
                “description”: “An answer to the question”,
                “type”: “string”
            }
        }
    },
    “input_value”: {
        “question”: “What’\’’s the hottest day of the year?”
    }
}'
```

## Response

```json
{
    “answer”: “The hottest day of the year varies depending on location, but typically falls in the summer months.”
}
```
