## Endpoint Documentation: `/v1/train/jobs/{job_id}/eval`

!!! note

    You can see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

Get the training evaluation results for a completed training job.

## Request

- HTTP Method: GET
- URL: `https://api.lamini.ai/v1/train/jobs/{job_id}/eval`
- Headers:
    - `Authorization: Bearer $LAMINI_API_KEY`
    - `Content-Type: application/json`

**Parameters:**

- `{job_id}` - The unique identifier of the completed training job.

## Response

The response will be the evaluation results for a completed training job.

### Request

```bash
curl --location --request GET 'https://api.lamini.ai/v1/train/jobs/123/eval' \
    --header 'Authorization: Bearer $LAMINI_API_KEY' \
    --header 'Content-Type: application/json'
```

### Response

```json
{
    "job_id":123,
    "eval_results": [
        {
            "input":"What is Lamini?",
            "outputs":[
                {
                    "model_name":"abcde",
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
