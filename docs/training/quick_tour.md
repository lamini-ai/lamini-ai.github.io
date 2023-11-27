When running inference, with prompt-engineering and RAG, is not enough for your LLM, you can train it. This is harder but will result in better performance, better leverage of your data, and increased knowledge and reasoning capabilities.

There are many ways to train your LLM. We'll cover the most common ones here:

* Finetuning: train your LLM on a specific task, e.g. question-answering, summarization, etc.
* Training LoRAs: more efficiently train your LLM
* Pretraining: train your LLM on a large dataset, e.g. Wikipedia, to improve its general knowledge


* Training: build your own LLM with finetuning and more
* Better training: customize your training call and evaluate your LLM
* Faster training: efficiently train LoRAs
* Bigger training: pretraining

* `AutocompleteRunner`: Run any model with autocomplete for your application - this class helps with evaluating your model, mostly for training.