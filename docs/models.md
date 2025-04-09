## Supported Models

### Lamini On-Demand

Lamini On-Demand supports a variety of the most popular open source LLMs, including [Llama 3.2](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct), [Mistral 3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3), [Phi-3](https://huggingface.co/Phi-3-mini-4k-instruct), [Qwen 2](https://huggingface.co/Qwen/Qwen2-7B-Instruct), and many more.

Models available on Lamini On-Demand for inference and tuning:

- `EleutherAI/pythia-410m`
- `EleutherAI/pythia-70m`
- `hf-internal-testing/tiny-random-gpt2`
- `meta-llama/Llama-2-13b-chat-hf`
- `meta-llama/Llama-2-7b-chat-hf`
- `meta-llama/Llama-2-7b-hf`
- `meta-llama/Meta-Llama-3-8B-Instruct`
- `meta-llama/Llama-3.1-8B-Instruct`
- `meta-llama/Llama-3.2-3B-Instruct`
- `microsoft/phi-2`
- `microsoft/Phi-3-mini-4k-instruct`
- `mistralai/Mistral-7B-Instruct-v0.1`
- `mistralai/Mistral-7B-Instruct-v0.2`
- `mistralai/Mistral-7B-Instruct-v0.3`
- `Qwen/Qwen2-7B-Instruct`

### Lamini Reserved and Self-Managed

Lamini Reserved and Self-Managed support all [CausalLM models from Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForCausalLM) (excluding those requiring Flash Attention 2 or 3). Roughly 95% of all models on HF are supported. If you're interested in using models that aren't available in Lamini On-Demand, please [contact us](https://www.lamini.ai/contact).

## Model size and performance

With [Memory Tuning](tuning/memory_tuning.md) you can achieve very high factual accuracy with 8B models, without giving up fluent generalization. Using smaller models lowers operating costs and improves latency.

Some factors to consider when thinking about model size:

- The more active parameters a model has, the more GPU memory is required to use the model.
- If a model is larger than a single GPU's memory, it needs to run across multiple GPUs. This means exchanging more data across the network, and both inference and tuning will take longer.
- Tuning requires significantly more GPU memory than inference.

## Model loading

Lamini On-Demand only allows use of the models listed above.

If you're using Lamini Reserved or Self-Managed, you can configure your cluster to use any supported Hugging Face model.

The `batch_model_list` in `llama_config.yaml` lets you specify which models to preload onto your allocated inference GPUs. Inference requests for all other models will be handled by your allocated `catchall` GPUs, and those models will be loaded from Hugging Face when requested.

Because models are large (usually tens of GBs), downloading them from Hugging Face and then loading them into GPU memory takes time. **Please allow 20-30 minutes for non-preloaded models to load.** Requests for models that have not yet loaded will return an error.

We recommend focusing development on one model or a small set of models, and preloading them. We've seen the highest accuracy and performance gains come from improving data quality and tuning recipes, rather than testing many models hoping to find one that works significantly better out of the box.
