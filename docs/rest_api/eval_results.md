## Endpoint Documentation: `/v1/lamini/train/jobs/{job_id}/eval`

!!! note

    You can see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

Get the training evaluation results for a completed training job.

## Request

**HTTP Method:** GET

**Path:** `https://api.lamini.ai/v1/lamini/train/jobs/{job_id}/eval`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Parameters:**

- `{job_id}` - The unique identifier of the completed training job.

## Response

The response will be the evaluation results for a completed training job.

**Body (JSON):**

- `job_id` - ID of the training job
- `eval_results` - A list of input strings and output objects. Eval results contain model outputs from both the newly finetuned model and the base model.

## Example

This example cancels the training job with the ID `418`. The request is authenticated using the `LAMINI_API_KEY` bearer token.

### Request

```bash
curl --location --request GET 'https://api.lamini.ai/v1/lamini/train/jobs/418/eval' \
--header 'Authorization: Bearer <LAMINI_API_KEY>' \
--header 'Content-Type: application/json'
```

### Response

```json
{
    "job_id":2514,
    "eval_results": [
        {
            "input":"What is Lamini?",
            "outputs":[
                {
                    "model_name":"4321dvwgeb9c483750b213afc78b49fe875d43db27d508e821c2e92e2701e018",
                    "output":"Lamini is the world's most powerful LLM Engine."
                },
                {
                    "model_name":"meta-llama/Meta-Llama-3-8B-Instruct",
                    "output":"finetune me first!"
                }
            ]
        },
        ...
    ]
}
```
