# POST `/v1/train`

Use this API endpoint to train a model. This will train a model using the data you've provided through the `/v1/data` api, or through adding data to an `id` using the python package's [Paired data api](/rest_api/data/). The response will include a job id and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

## Request

**HTTP Method:** POST

**URL:** `https://api.lamini.ai/v1/train`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Example Body (JSON):**

```json
{
  "model_name": "EleutherAI/pythia-410m-deduped",
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

## Parameters:

- model_name (string): The base model you'd like to train.
- data (list): The data you'd like to train on. This should be a list of datapoints, with each datapoint a json object with keys `input` and `output`. Each input and output should have string values.

## Response:

The response will include a job id and the status of the job. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train). There are a number of statuses possible, each representing a different stage in the training process.

```
{
    "job_id": "<JOB_ID>",
    "status": "SCHEDULED" | "CREATED" | "LOADING DATA" | "TRAINING MODEL" | "EVALUATING MODEL" | "SAVING MODEL" | "COMPLETED" | "FAILED"
}
```

## Example

### Request

```bash
curl --location 'https://api.lamini.ai/v1/train' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "EleutherAI/pythia-410m-deduped"
    "data": [
                {"input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nAre there any step-by-step tutorials or walkthroughs available in the documentation?[/INST]", "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/"},
                {"input": "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n<</SYS>>\n\nDoes Lamini have a limit on the number of API requests I can make?", "output": "Lamini provides each user with free tokens up front."}
            ]
}'
```

### Response

```json
{
  "job_id": "1512",
  "status": "SCHEDULED"
}
```
