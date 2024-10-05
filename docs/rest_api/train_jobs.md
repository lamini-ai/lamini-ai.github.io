## `/v1/train/jobs`

!!! note

    You can see these results by going to the `train` tab at [https://app.lamini.ai/train](https://app.lamini.ai/train)

Get a list of all jobs and statuses associated with an API key.

## Request

- HTTP Method: `GET`
- URL: `https://api.lamini.ai/v1/train/jobs`
- Headers:
      - `Authorization: Bearer $LAMINI_API_KEY`
      - `Content-Type: application/json`

### Request

```bash
curl --location --request GET 'https://api.lamini.ai/v1/train/jobs' \
    --header 'Authorization: Bearer $LAMINI_API_KEY' \
    --header 'Content-Type: application/json'
```

### Response

```json
[
    {"job_id":123,"status":"CANCELLED","start_time":"2023-07-12T17:44:51.953408","model_name":null,"custom_model_name":null,"resume_count":0,"dataset_id":null,"resume_limit":1000},
    {"job_id":124,"status":"COMPLETED","start_time":"2023-07-12T17:38:28.980971","model_name":"abcdef","custom_model_name":"My first model","resume_count":0,"dataset_id":null,"resume_limit":1000},
    ...
]
```
