# FAQ

## What models are supported?
We support all [CausalLM models from HuggingFace](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForCausalLM) for tuning and inference.

## Does Lamini use LoRAs?
In combination with a few techniques, we tune LoRAs (low-rank adapters) on top of a pretrained LLM to get the same performance as finetuning the entire model, but with 266x fewer parameters and 1.09 billion times faster model switching.

This efficiency gain is on and handled by default.

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

## How do I design my LLM app?
Here are some common questions that may help you reason about the design of your
first LLM app.

1. Who are your intended users?

2. How will this application be deployed?

3. What data is available to train the LLM?

4. What data is available online vs offline?

5. What are the gaps between the out of the box
   performance of the LLM, and your requirements?
