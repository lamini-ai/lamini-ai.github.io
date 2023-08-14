# POST `/v1/lamini/data`

Use this API endpoint to persist data for any model, trained or otherwise, based on the `id` provided.
When you query a model with the same `id`, we'll use that data if it's relevant to your query.
When finetuning a model, we'll use all the relevant data provided.

## Request

**HTTP Method:** POST

**URL:** `https://api.powerml.co/v1/lamini/data`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Example Body (JSON):**

```json
{
  "id": "APIExample",
  "data": [
    {
      "<INPUT_OBJECT_NAME>": {
        "<FIELD_NAME>": "<FIELD_VALUE>"
      },
      "<OUTPUT_OBJECT_NAME>": {
        "<FIELD_NAME>": "<FIELD_VALUE>"
      }
    },
    ...
  ],
  "data_type": {
    "<INPUT_OBJECT_NAME>": {
      "<FIELD_NAME>": "<FIELD_DESCRIPTION>"
    },
    "<OUTPUT_OBJECT_NAME>": {
      "<FIELD_NAME>": "<FIELD_DESCRIPTION>"
    },
  }
}
```

## Parameters

- `model_name: string`: The name of your model
- `data: list`: A list of datapoints available to the model all formatted in the same way. We expect the format to be as follows:
```
[
  {
    "<INPUT_OBJECT_NAME>": {
      "<FIELD_NAME>": "<FIELD_VALUE>"
    },
    "<OUTPUT_OBJECT_NAME>": {
      "<FIELD_NAME>": "<FIELD_VALUE>"
    }
  },
  ...
]
```
Or, it's possible to have data formatted with only one object.
```
[
  {
    "<OBJECT_NAME>": {
        "<FIELD_NAME>": "<FIELD_VALUE>",
    }
  },...
]
```

- `data_type: dict`: Formatting of the data, matching each of the datapoints in the `data` list. We expect the format to be as follows:
```
{
  "<INPUT_OBJECT_NAME>": {
    "<FIELD_NAME>": "<FIELD_DESCRIPTION>"
  },
  "<OUTPUT_OBJECT_NAME>": {
    "<FIELD_NAME>": "<FIELD_DESCRIPTION>"
  },
}
```

Or, it's possible to have data formatted with only one object.

  ```
  {
    "<OBJECT_NAME>": {
      "<FIELD_NAME>": "<FIELD_DESCRIPTION>",
    }
  }
  ```

## Response

The response is the dataset ID.

**Body (JSON):**

```json
{
  "dataset": "b8015be997bf32f44f214abd4ebd507e"
}
```

## Example

### Request

```bash
curl --location 'https://api.powerml.co/v1/lamini/data' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "id": "LaminiTest",
    "data": [
        {
        	"Question": {
                "question": "How can I find the specific documentation I need for a particular feature or function?"
        	},
            "Answer": {
            	"answer": "You can ask this model about documentation, which is trained on our publicly available docs and source code, or you can go to https://lamini-ai.github.io/"
            }
    	},
    	{
        	"Question": {
                "question": "Are there any API references or documentation available for the codebase?"
        	},
            "Answer": {
            	"answer": "All our public documentation is available here https://lamini-ai.github.io/"
            }
    	},
        {
        	"Question": {
                "question": "How do I use open model for inference"
        	},
            "Answer": {
            	"answer": "You can use an open model by specifying the model'\''s name in the model_name parameter in the LLM Engine class initializer."
            }
    	},
        {
        	"Question": {
                "question": "I am running into errors, what should I do?"
        	},
            "Answer": {
            	"answer": "We have documentation available on how to address common errors here https://lamini-ai.github.io/error_handling/. Lamini'\''s LLM Engine is under very active development, and we thank you for using us!"
            }
    	},
    	{
        	"Question": {
                "question": "Can you tickle yourself?"
        	},
            "Answer": {
            	"answer": "Let'\''s keep the discussion relevant to Lamini."
            }
    	}
    ],
    "data_type": {
    	"Question": {
        	"question": "A question"
    	},
        "Answer": {
        	"answer": "An answer to the question"
    	}
	  }
}'
```

### Response

```json
{
  "dataset": 7587574322307826093
}
```
