# Supported Models

Lamini On-demand supports [CausalLM models from Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForCausalLM) for tuning and inference, including [Llama 3.1](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct), [Mistral 3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3), [Phi-3](https://huggingface.co/Phi-3-mini-4k-instruct), [Qwen 2](https://huggingface.co/Qwen/Qwen2-7B-Instruct), and many more.

Lamini Reserved and Self-managed supports more models. Please [contact us](https://www.lamini.ai/contact) if you need them.

Models available on Lamini On-demand for inference and tuning:
  - `EleutherAI/pythia-410m`
  - `EleutherAI/pythia-70m`
  - `hf-internal-testing/tiny-random-gpt2`
  - `meta-llama/Llama-2-13b-chat-hf`
  - `meta-llama/Llama-2-7b-chat-hf`
  - `meta-llama/Llama-2-7b-hf`
  - `meta-llama/Meta-Llama-3-8B-Instruct`
  - `meta-llama/Meta-Llama-3.1-8B-Instruct`
  - `microsoft/phi-2`
  - `microsoft/Phi-3-mini-4k-instruct`
  - `mistralai/Mistral-7B-Instruct-v0.1`
  - `mistralai/Mistral-7B-Instruct-v0.2`
  - `mistralai/Mistral-7B-Instruct-v0.3`
  - `Qwen/Qwen2-7B-Instruct`

Note: Flash Attention 2 and 3 are not yet supported.

## Model size
With [Memory Tuning](tuning/memory_tuning.md) you can achieve very high factual accuracy with 8B models, without giving up fluent generalization. Using smaller models lowers operating costs and improves latency.

Some factors to consider when thinking about model size:

- The more active parameters a model has, the more GPU memory is required to use the model.
- If a model is larger than a single GPU's memory, it needs to run across multiple GPUs. This means exchanging more data across the network, and both inference and tuning will take longer.
- Tuning requires significantly more GPU memory than inference.

## Model loading

The most popular models are preloaded on Lamini On-demand. Other models will be loaded from Hugging Face when requested in an inference or tuning call. Because models are large (usually tens of GBs), downloading them from Hugging Face and then loading them into GPU memory takes time.

**Please allow 20-30 minutes for the model to load.** Requests for models that have not yet loaded will return an error.

We recommend focusing development on one model or a small set of models, and preloading them. We've seen the highest accuracy and performance gains come from improving data quality and tuning recipes, rather than testing many models hoping to find one that works significantly better out of the box.
