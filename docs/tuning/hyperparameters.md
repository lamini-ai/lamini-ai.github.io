# Hyperparameters

Lamini tuning supports most hyperparameters in [HuggingFace's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), as well as some Lamini-specific options.

These can be set in the `tune` method:

```py
# code/hyperparameters.py
```

See [Memory Tuning](./memory_tuning.md/#example-memory-tuning-settings) for use-case specific suggestions.

## finetune_args

- **max_finetuning_examples** (int, optional)
    - Default: size of the dataset
    - Sets the maximum number of data points for fine-tuning. If not set, the model is fine-tuned on the entire dataset.

- **max_steps** (int, optional)
    - Default: `100`
    - Specifies the total number of training steps to perform.
    - This parameter is passed to [HuggingFace's Transformers TrainingArguments](https://huggingface.co/docs/transformers/v4.44.2/en/main_classes/trainer#transformers.TrainingArguments.max_steps).

- **gradient_accumulation_steps** (int, optional)
    - Default: `2`
    - Number of update steps to accumulate the gradients for, before performing a backward/update pass.
    - Usage note: a higher setting can improve memory efficiency and thus reduce training time, often with a neutral effect on model accuracy.
    - This parameter is passed to [HuggingFace's Transformers TrainingArguments](https://huggingface.co/docs/transformers/v4.44.2/en/main_classes/trainer#transformers.TrainingArguments.gradient_accumulation_steps).

- **learning_rate** (float, optional)
    - Default: `9.0e-4`
    - The initial learning rate for the fine-tuning.
    - This parameter is passed to [HuggingFace's Transformers TrainingArguments](https://huggingface.co/docs/transformers/v4.44.2/en/main_classes/trainer#transformers.TrainingArguments.learning_rate).
    - Usage note: see the [Memory Tuning](./memory_tuning.md/#example-memory-tuning-settings) section for tips on setting learning rate.

- **save_steps** (int or float, optional)
    - Default: `60`
    - Number of update steps between two checkpoint saves.
    - This parameter is passed to [HuggingFace's Transformers TrainingArguments](https://huggingface.co/docs/transformers/v4.44.2/en/main_classes/trainer#transformers.TrainingArguments.save_steps).

- **max_length** (int, optional)
    - Default: `2048`
    - Specifies the maximum sequence length for the forward pass, acting as the block size for the model.
    - Should be a power of 2, no larger than `8192`.
    - Usage note: `max_length` should be at least as large as the size of your datapoints. If training with large datapoints is not converging, increasing this value may help. However, larger values of `max_length` increase training time, and very large values will exhaust GPU memory. There's often room to reduce the size of your datapoints so a smaller `max_length` can be used.

- **optim** (str, optional)
    - Default: `"adafactor"`
    - The optimizer to use: `adamw_hf`, `adamw_torch`, `adamw_torch_fused`, `adamw_apex_fused`, `adamw_anyprecision` or `adafactor`.
    - This parameter is passed to [HuggingFace's Transformers TrainingArguments](https://huggingface.co/docs/transformers/main/en/main_classes/trainer#transformers.TrainingArguments.optim).

- **r_value** (int, optional)
    - Default: `64`
    - Specifies the size of the LoRA (Low-Rank Adaptation) component.

- **index_method** (str, optional)
    - Default: `"IndexIVFPQ"`
    - The index method used for approximate nearest neighbor search of high-dimensional vectors: `IndexIVFPQ`, `IndexHNSWPQ`,`IndexHNSWFlat`, `IndexFlatL2`, `IndexPQ`

- **index_k** (int, optional)
    - Default: `2`
    - Determines the number of nearest neighbors to consider.

- **index_max_size** (int, optional)
    - Default: `65536`
    - Maximum size of the index.

- **index_pq_m** (int, optional)
    - Default: `8`
    - Number of factors of product quantization.
    - Only used when `index_method` is `IndexIVFPQ` or `IndexPQ`. Ignored otherwise.

- **index_pq_nbits** (int, optional)
    - Default: `8`
    - Number of bits in which each low-dimensional vector is stored. Range: [1, 16]
    - Only used when `index_method` is `IndexIVFPQ` or `IndexPQ`. Ignored otherwise.

- **index_ivf_nlist** (int, optional)
    - Default: `2048`
    - Number of buckets during clustering for IVFLAT.
    - Only used when `index_method` is `IndexIVFPQ`. Ignored otherwise.

- **index_ivf_nprobe** (int, optional)
    - Default: `48`
    - Number of buckets to search during the first step of IVFLAT.
    - Only used when `index_method` is `IndexIVFPQ`. Ignored otherwise.

- **index_hnsw_m** (int, optional)
    - Default: `32`
    - Range: [4, 64]. Used in HNSW (Hierarchical Navigable Small World Graph) algorithm.
    - Only used when `index_method` is `IndexHNSWPQ` or `HNSWFlat`. Ignored otherwise.

- **index_hnsw_efConstruction** (int, optional)
    - Default: `16`
    - Expansion factor at construction time for HNSW. Range: [8, 512]
    - Only used when `index_method` is `IndexHNSWPQ` or `HNSWFlat`. Ignored otherwise.

- **index_hnsw_efSearch** (int, optional)
    - Default: `8`
    - Expansion factor at search time for HNSW.
    - Only used when `index_method` is `IndexHNSWPQ` or `HNSWFlat`. Ignored otherwise.

### Immutables
The following configs are only supported at their default values:
- **batch_size: 1**
- **early_stopping: false**
- **num_train_epochs**: Will be overriden by `max_steps`
- **temperature: 0**

## gpu_config

- **gpus**: (int, optional)
    - Default: `1`
    - Number of GPUs per node to use for the tuning job.
- **nodes**: (int, optional)
    - Default: `1`
    - Number of nodes (machines containing multiple GPUs) to use for the tuning job.

```python
gpu_config = {
    "gpus": 4,
    "nodes": 1,
}
```

The Lamini On-Demand allows a maximum of GPUs and nodes based on our server availability. If you are on Lamini Reserved or Self-managed, you can specify any number of GPUs and nodes within your provisioned cluster size. Your job will be queued until the requested number of GPUs and nodes is available.

If the required GPUs and nodes are not available, the configuration defaults to the system limit, and the job is queued until the resources become available. When using multiple nodes, specify the number of GPUs required per node.

Examples:
```python
gpu_config = {"gpus": 8, "nodes": 1}  # total 8 GPUs
gpu_config = {"gpus": 8, "nodes": 2}  # total 16 GPUs
gpu_config = {"gpus": 4, "nodes": 2}  # total 8 GPUs
gpu_config = {"gpus": 9, "nodes": 1}  # error, assuming max GPUs per node is 8
```

## data_or_dataset_id

- **data_or_dataset_id** (JSONL or CSV file or dataset ID of an already uploaded dataset, required)
    - Default: no default
    - Specifies the dataset to use for the tuning job.
