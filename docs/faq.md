# FAQ

## What models are supported?
We support all [CausalLM models from HuggingFace](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForCausalLM) for tuning and inference.

## Why did my training / tuning job time out?
We have a time out at 4 hours and a queue for tuning jobs in order to serve all users. If your job times out, you can resume training to restart the training from the last checkpoint. If you would like more throughput, please reach out to info@lamini.ai about an enterprise contract.

## Why is my job queued?
We have a time out at 4 hours and a queue for tuning jobs in order to serve all users. If your job times out, you can resume training to restart the training from the last checkpoint. If you would like more throughput, please reach out to info@lamini.ai about an enterprise contract.

## I'm getting a missing key error!
You can get your API key from [https://app.lamini.ai/account](https://app.lamini.ai/account).

Next, make sure you set it before calling lamini:

```python
import lamini
lamini.api_key = "<YOUR-LAMINI-API-KEY>"
```
If you want different authentication options, check out [Authenticate](get_started/authenticate).
