# Hyperparameters

Lamini is designed to have good default hyperparameters, so you don't need to tune them. If, however, you would like the flexibility to, you can do so through the `tune` method:

```python hl_lines="3"
results = llm.tune(
    data_or_dataset_id=data,
    finetune_args={'learning_rate': 1.0e-4}
    )
```

Currently we support most hyperparameters in [HuggingFace's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc.

Common hyperparameters to tune include:

- `learning_rate` (float) - the learning rate of the model

- `early_stopping` (bool) - whether to use early stopping or not

- `max_steps` (int) - the maximum number of steps to train for

- `optim` (str) - the optimizer to use, e.g. `adam` or `sgd`, a string from HuggingFace
