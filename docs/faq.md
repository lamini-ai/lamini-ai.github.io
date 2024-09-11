# FAQ

## What models are supported?
The [Models](models.md) page has details on the (many) models you can use with Lamini.

## Will my training / tuning job time out?
We have a default 4-hour timeout for all tuning jobs. If your job times out, it will be automatically added back to the queue and run from the last checkpoint - Lamini automatically saves checkpoints so your progress isn't lost. This is to allow other jobs to run. If you want to run longer jobs, consider requesting more GPUs via `gpu_config` for a speed up or [contact us](https://www.lamini.ai/contact) for a dedicated instance.

## Why is my job queued?
Our On-demand plan uses shared resources. We queue tuning jobs in order to serve all users. To reserve your own dedicated compute or run on your own GPUs, please [contact us](https://www.lamini.ai/contact).

## I'm getting a missing key error! What do I do?
The [Authenticate](authenticate.md) page has details on getting and setting your Lamini API key.

## Does Lamini run on Windows?
Lamini has not been tested on Windows and is not officially supported. While it may be possible to run Lamini on Windows, we cannot guarantee its functionality or stability. If you are using Windows, we strongly recommend using Docker to run Lamini on a Linux-based image.

## What systems can run Lamini?
Lamini is tested and developed on Linux-based systems. Specifically, we recommend using Ubuntu 22.04 or later with Python 3.10, 3.11, or 3.12.

## Can I turn off memory tuning / MoME?
Yes, if your use case needs a more qualitative output, like summarization where there are many possible answers, then memory tuning may be hurting performance (but still worth trying). You can set the following finetuning args to disable MoME:
```python
finetune_args={
  "batch_size": 1,
  "index_ivf_nlist": 1,
  "index_method": "IndexFlatL2",
  "index_max_size": 1,
}
```

## Does Lamini use LoRAs?
Yes, Lamini tunes LoRAs (low-rank adapters) on top of a pretrained LLM to get the same performance as finetuning the entire model, but with 266x fewer parameters and 1.09 billion times faster model switching. Read [our blog post](https://www.lamini.ai/blog/one-billion-times-faster-finetuning-with-lamini-peft) for more details.

Lamini applies this optimization (and others) automatically - you don't have to configure anything.

## Can I run my job on an MI300?
Yes! Lamini On-demand currently uses MI250s, but we have MI300s available for our Lamini Reserved plans. Please [contact us](https://www.lamini.ai/contact) to learn more about Lamini Reserved and our MI300 cluster.
