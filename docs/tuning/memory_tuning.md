# Memory Tuning

Memory Tuning is a revolutionary new capability from Lamini that lets you embed precise, factual data inside the LLM’s memory by tuning the LLM with millions of adapters. Memory Tuning turns any open LLM, such as Llama 3.1 or Mistral 3, into a Mixture of Memory Experts (MoME) that can recall your facts with photographic memory by selectively routing across its experts. With a MoME, frequent hallucinations become a thing of the past.

Memory tuning allows your LLMs to keep their general reasoning capabilities while committing specific factual data to their weights as memory.

## Notebook example

We partnered with Meta to create a [notebook](https://github.com/meta-llama/llama-recipes/blob/main/recipes/3p_integrations/lamini/text2sql_memory_tuning/README.md) that shows how to use Memory Tuning to improve a text-to-SQL model from 30% to 95% accuracy.

Working through the notebook will give you a good sense of how to use Memory Tuning, and you can do it all within the Lamini Free plan.

## Memory Tuning settings

Tuning hyperparameters can be a bit of an art. We've found that the following settings work well for common use cases:

### When experimenting with a small dataset (<100 facts):

`llm.train(data_or_dataset_id=data*10, finetune_args={"max_steps": 100, "learning_rate": 0.0003}, gpu_config={"gpus": 8, "nodes": 1})`

- Note that we're multiplying the dataset by 10
- We recommend increasing `max_steps` when working with a larger dataset.

### Factual Q/A from PDFs (20 PDFs, 800+ facts)
 `"max_steps": 500, "learning_rate": 0.00009`

### Text-to-SQL (100 queries)
`"max_steps": 500, "learning_rate": 0.00001`

## Specifying GPUs and nodes

`llm.train` takes an optional `gpu_config` argument that lets you specify the number of GPUs and nodes to use for tuning.

Unless explicitly specified, the default is 1 GPU and 1 node.

On the Lamini Free plan, you can specify up to 4 GPUs and 1 node.

If you are self-managing Lamini Platform, you can specify any number of GPUs and nodes within the cluster size you've provisioned.

Your job will be queued until the requested number of nodes and GPUs are available.

## Learn more

- See how a Fortune 500 company used Memory Tuning in our [case study](https://www.lamini.ai/blog/llm-text-to-sql)
- Read more in our [blog post](http://www.lamini.ai/blog/lamini-memory-tuning)
