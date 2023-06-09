# GET `/v1/lamini/train/jobs/{job_id}/eval`

Get the training evaluation results for a completed training job. You can also see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

## Request

**HTTP Method:** GET

**Path:** `https://api.powerml.co/v1/lamini/train/jobs/{job_id}/eval`

**Headers:**

- `Authorization: Bearer <LAMINI_API_KEY>`
- `Content-Type: application/json`

**Parameters:**

- `{job_id}` - The unique identifier of the completed training job.

## Response

The response will be the evaluation results for a completed training job.

**Body (JSON):**

- `job_id` - ID of the training job
- `eval_results` - A dictionary of prompt to completions.

## Example

This example cancels the training job with the ID `418`. The request is authenticated using the `test_token` bearer token.

### Request

```bash
curl --location --request GET 'https://api.powerml.co/v1/lamini/train/jobs/418/eval' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json'
```

### Response

```json
{
    "job_id": 418,
    "eval_results": {"What's your name?": {"4321dvwgeb9c483750b213afc78b49fe875d43db27d508e821c2e92e2701e018":"I'm a Teapot!"}, {"EleutherAI/pythia-410m-deduped":"finetune me first!"}},
}
```
