# Memory Tuning

Memory Tuning is a revolutionary new capability from Lamini that lets you embed precise, factual data inside the LLM’s memory by tuning the LLM with millions of adapters. Memory Tuning turns any open LLM, such as Llama 3.1 or Mistral 3, into a Mixture of Memory Experts (MoME) that can recall your facts with photographic memory by selectively routing across its experts. With a MoME, frequent hallucinations become a thing of the past.

Memory tuning allows your LLMs to keep their general reasoning capabilities while committing specific factual data to their weights as memory.

## Notebook example

We partnered with Meta to create a [notebook](https://github.com/meta-llama/llama-recipes/blob/main/recipes/3p_integrations/lamini/text2sql_memory_tuning/README.md) that shows how to use Memory Tuning to improve a text-to-SQL model from 30% to 95% accuracy.

Working through the notebook will give you a good sense of how to use Memory Tuning, and you can do it all within the Lamini On-demand plan.

## Principles for Memory Tuning

Andrej Karpathy's [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/) is a great summary of the phased, iterative approach you should take to Memory Tuning (even though many of the specific examples in that article don't apply to Memory Tuning).

1. Become one with the data
    - Deeply understand your dataset and your eval, and refine them to high quality

1. Set up the end-to-end training/evaluation skeleton

    Before you start Memory Tuning, measure the baseline accuracy on:

    1. the base model
    1. base model + prompt tuning
    1. base model + prompt tuning + RAG

1. Overfit
    - Find a Memory Tuning recipe that's accurate on your facts, even just for one example, before scaling up your data

1. Regularize
    - Scale up your data and check generalization performance

1. Optimize
    - Continue iterating now that you have a solid foundation

Don't skip any of these steps!

## Example Memory Tuning settings

Tuning hyperparameters can be a bit of an art. Where should you start experimenting?

- `learning rate`
- `max_finetuning_examples`
- `max_steps`
- `gradient_accumulation_steps`

See [Hyperparameters](hyperparameters.md) for the complete list of options.

### When experimenting with a small dataset (<100 facts):

```python
llm.train(data_or_dataset_id=data, finetune_args={"max_steps": 50, "r_value": 32, "learning_rate": 0.0003})
```

- We recommend increasing `max_steps` when working with a larger dataset.

### Factual Q/A from PDFs (20 PDFs, 800+ facts)
```json
{
  "max_steps": 500,
  "learning_rate": 0.00009
}
```

### Text-to-SQL (100 queries)
```json
{
  "max_steps": 500,
  "learning_rate": 0.00001
}
```

### Factual Q/A on 10,000 facts:
```json
{
  "gradient_accumulation_steps": 4,
  "index_k": 2,
  "index_max_size": 65536,
  "index_method": "IndexFlatL2",
  "learning_rate": 0.0003,
  "max_length": 512,
  "max_steps": 10000,
  "index_ivf_nlist": 2048,
  "max_finetuning_examples": 10000,
  "r_value": 64
}
```

## Experiment with learning rate

For training jobs with less than 300 steps, a grid search approach can be effective. You can run multiple jobs on a subset of the data with a range of learning_rates to find which learning rate has a better loss curve. Once that is found, you can expand the training to the larger dataset with this best learning_rate.

```python
from lamini import Lamini

lamini.api_key = "<key>"

def main():
    llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")

    dataset = your_dataset_goes_here

    try:
        start = time.time()
        dataset_id = llm.upload_data(dataset)
        end = time.time()
        print(f"Uploaded dataset in {end - start} seconds")
    except Exception as e:
        print(f"Failed to upload dataset: {e}")
        return

    learning_rates = [0.0009, 0.0003, 0.00009,  0.00003, 0.000003, 0.000009]

    for lr in learning_rates:
        print(f"Training with lr={lr}")

        try:
            results = llm.train(
                dataset_id,
                use_cached_model=False,
                finetune_args={
                    "learning_rate": lr,
                    "max_steps":300,
                },
                gpu_config={
                    "gpus": 2,
                    "nodes": 1,
                }
            )
            print(f"Training results: {results}")
        except Exception as e:
            print(f"Failed to train model: {e}")
            continue

def load_training_data():
    <——code to gather data——>
```

## Specifying GPUs and nodes

Specifying additional GPUs and/or nodes can significantly reduce model tuning time, which is especially beneficial when working with large datasets.

`llm.train` takes an optional `gpu_config` argument that lets you specify the number of GPUs and nodes to use for tuning. See [Hyperparameters](hyperparameters.md/#gpu_config) for more details.

If you are self-managing Lamini Platform, you can specify any number of GPUs and nodes within the cluster size you've provisioned.

Your job will be queued until the requested number of nodes and GPUs are available.

## Learn more

- See how a Fortune 500 company used Memory Tuning in our [case study](https://www.lamini.ai/blog/llm-text-to-sql)
- Read more in our [blog post](http://www.lamini.ai/blog/lamini-memory-tuning)
