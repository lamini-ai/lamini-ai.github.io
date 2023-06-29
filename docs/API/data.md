# POST `/v1/lamini/data`

Use this API endpoint to persist data for any model, finetuned or otherwise, based on the `id` provided.
When you query a model with the same `id`, we'll use that data if it's relevant to your query.
When finetuning a model, we'll use all the relevant data provided.

### Request

- HTTP Method: POST
- URL: `https://api.powerml.co/v1/lamini/data`
- Headers:
  - `Authorization: Bearer <LAMINI_API_KEY>`
  - `Content-Type: application/json`
- Example Body (JSON):

```json
{
  "id": "APIExample",
  "data": [
    {
      "Document": {
        "text": "On average the hottest day of the year is July 8"
      }
    },
    {
      "Document": {
        "text": "Yearly average temperatures show a gradual rise over the past ten years."
      }
    }
  ],
  "data_type": {
    "Document": {
      "text": "A single document"
    }
  }
}
```

#### Parameters:

- `model_name: string`: The name of your model
- `data: list`: A list of datapoints available to the model all formatted in the same way. We expect the format to be as follows:

```
  [
    {
      "<OBJECT_NAME>": {
          "<FIELD_NAME>": "<FIELD_VALUE>",
      }
    },...
  ]
```

- `data_type: dict`: Formatting of the data, matching each of the datapoints in the `data` list. We expect the format to be as follows

  ```
  {
      "<OBJECT_NAME>": {
          "<FIELD_NAME>": "<FIELD_DESCRIPTION>",
      }
  }
  ```

### Response

The response is the dataset ID.

- Success Status Code: 200
- Body (JSON):

```json
{
  "dataset": 7587574322307826093
}
```

### Example

#### Request

```bash
curl --location 'https://api.powerml.co/v1/lamini/data' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "data": [
        {
            "Document": {
                "text": "On average the hottest day of the year is July 8"
            }
        },
        {
            "Document": {
                "text": "Yearly average temperatures show a gradual rise over the past ten years."
            }
        }
    ],
    "data_type": {
        "Document": {
            "text": "A single document"
        }
    }
}'
```

#### Response

```json
{
  "dataset": 7587574322307826093
}
```
