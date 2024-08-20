# Hyperparameters

Lamini tuning supports most hyperparameters in [HuggingFace's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), as well as some Lamini-specific options.

These can be set in the `tune` method:

```py
# code/hyperparameters.py#L9-L12
```

See [Memory Tuning](./memory_tuning.md/#memory-tuning-settings) for use-case specific suggestions.

## finetune_args

- **max_finetuning_examples** (int, optional)
    - Default: size of the dataset
    - Sets the maximum number of data points for fine-tuning. If not set, the model is fine-tuned on the entire dataset.

- **max_steps** (int, optional)
    - Default: `100`
    - Specifies the total number of training steps to perform.

- **gradient_accumulation_steps** (int, optional)
    - Default: `2`
    - Number of update steps to accumulate the gradients for, before performing a backward/update pass.

- **learning_rate** (float, optional)
    - Default: `9.0e-4`
    - The initial learning rate for the fine-tuning.

- **batch_size** (int, optional)
    - Default: `1`
    - The batch size per device used for training. Chunks are used during fine-tuning. Each chunk has max_length of tokens. Multiple datapoints can make up a single chunk. As chunking is position invariant it leads to stabler model training and has the ability to generalize better. The default batch_size is set to 1, allowing the model to effectively batches data points. Setting this to a value other than 1 will result in an error.

- **max_length** (int, optional)
    - Default: `2048`
    - Specifies the maximum sequence length for the forward pass, acting as the block size for the model.

- **layer_size** (int, optional)
    - Default: `128`
    - Defines the size of each layer in the model.

- **attention_dropout** (float, optional)
    - Default: `0.0`
    - The dropout ratio for the attention probabilities.

- **hidden_dropout** (float, optional)
    - Default: `0.0`
    - Dropout ratio applied to hidden states to prevent overfitting and improve generalization.

- **attention_heads** (int, optional)
    - Default: `4`
    - Number of attention heads for each attention layer in the encoder.

- **layers** (int, optional)
    - Default: `4`
    - Specifies the number of layers in the model.

- **num_train_epochs** (float, optional)
    - Default: `10`
    - Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training).

- **optim** (str, optional)
    - Default: `"adafactor"`
    - The optimizer to use: `adamw_hf`, `adamw_torch`, `adamw_torch_fused`, `adamw_apex_fused`, `adamw_anyprecision` or `adafactor`.

- **early_stopping** (bool, optional)
    - Default: `False`
    - Stops beam search when at least num_beams sentences are finished per batch.

- **num_hidden_layers** (int, optional)
    - Default: `32`
    - Number of hidden layers in the encoder.

- **hidden_size** (int, optional)
    - Default: `4096`
    - Dimension of the hidden representations.

- **index_method** (str, optional)
    - Default: `"IndexIVFPQ"`
    - The index method used for ANN search of high-dimensional vectors. IndexIVFPQ is a popular algorithm for approximate nearest neighbor search.

- **index_k** (int, optional)
    - Default: `2`
    - Determines the number of nearest neighbors to consider.

- **index_max_size** (int, optional)
    - Default: `65536`
    - Maximum size of the index.

- **index_pq_m** (int, optional)
    - Default: `8`
    - Number of factors of product quantization.

- **index_pq_nbits** (int, optional)
    - Default: `8`
    - Number of bits in which each low-dimensional vector is stored. Range: [1, 16]

- **index_ivf_nlist** (int, optional)
    - Default: `2048`
    - Number of buckets during clustering for IVFLAT.

- **index_ivf_nprobe** (int, optional)
    - Default: `48`
    - Number of buckets to search during the first step of IVFLAT.

- **index_hnsw_m** (int, optional)
    - Default: `32`
    - Range: [4, 64]. Used in HNSW (Hierarchical Navigable Small World Graph) algorithm.

- **index_hnsw_efConstruction** (int, optional)
    - Default: `16`
    - Expansion factor at construction time for HNSW. Range: [8, 512]

- **index_hnsw_efSearch** (int, optional)
    - Default: `8`
    - Expansion factor at search time for HNSW.

- **r_value** (int, optional)
    - Default: `64`
    - Specifies the size of the LoRA (Low-Rank Adaptation) component.

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

The Lamini Free plan allows a maximum of 4 GPUs and 1 node. If you are self-managing the Lamini Platform, you can specify any number of GPUs and nodes within your provisioned cluster size. Your job will be queued until the requested number of GPUs and nodes is available.

If the required GPUs and nodes are not available, the configuration defaults to the system limit, and the job is queued until the resources become available. When using multiple nodes, specify the number of GPUs required per node.

Examples:
```python
gpu_config = {"gpus": 8, "nodes": 1}  # total 8 GPUs
gpu_config = {"gpus": 8, "nodes": 2}  # total 16 GPUs
gpu_config = {"gpus": 4, "nodes": 2}  # total 8 GPUs
gpu_config = {"gpus": 9, "nodes": 1}  # total 8 GPUs, assuming max GPUs per node is 8
```

## data_or_dataset_id

- **data_or_dataset_id** (JSONL or CSV file or dataset ID of an already uploaded dataset, required)
    - Default: no default
    - Specifies the dataset to use for the tuning job.