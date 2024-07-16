# Supported Models

Lamini supports [CausalLM models from Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/auto#transformers.AutoModelForCausalLM) for tuning and inference, including [Llama 3](https://huggingface.co/docs/transformers/v4.42.0/en/model_doc/llama3), [Mistral 2](https://huggingface.co/docs/transformers/v4.42.0/en/model_doc/mistral), [Phi-3](https://huggingface.co/docs/transformers/main/en/model_doc/phi3), [Qwen 2](https://huggingface.co/docs/transformers/main/en/model_doc/qwen2), and many more.

Note: Flash Attention 2 and 3 are not yet supported. Please [contact us](https://www.lamini.ai/contact) if you need them.

## Free plan

Free plan users on [Lamini Cloud](https://app.lamini.ai) can use the following models:

- Llama 3: [`meta-llama/Meta-Llama-3-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
- Mistral v2 - [`mistralai/Mistral-7B-Instruct-v0.2`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
- Phi 3 - [`microsoft/Phi-3-mini-4k-instruct`](https://huggingface.co/Phi-3-mini-4k-instruct)
- Qwen 2- [`Qwen/Qwen2-7B-Instruct`](https://huggingface.co/Qwen/Qwen2-7B-Instruct)
- Tiny Random GPT-2 [`hf-internal-testing/tiny-random-gpt2`](https://huggingface.co/hf-internal-testing/tiny-random-gpt2)

## Model size

On [Lamini Cloud](https://app.lamini.ai) we recommend using models <=17B parameters for inference and <=8B parameters for tuning for the best performance. Lamini Platform supports larger models. Please [contact us](https://www.lamini.ai/contact) if you need them.

With [Memory Tuning](/tuning/memory_tuning) you can achieve very high factual accuracy with 8B models, without giving up fluent generalization. Using smaller models lowers operating costs and improves latency.

Some factors to consider when thinking about model size:

- The more active parameters a model has, the more GPU memory is required to use the model. 
- If a model is larger than a single GPU's memory, it needs to run across multiple GPUs. This means exchanging more data across the network, and both inference and tuning will take longer. 
- Tuning requires significantly more GPU memory than inference.

## Model loading

The most popular models are preloaded on Lamini Cloud. Other models will be loaded from Hugging Face when requested - because models are large, this can take a few minutes.