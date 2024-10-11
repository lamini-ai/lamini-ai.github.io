# Model Management

Lamini Platform supports a [variety of models](../models.md). When self-managing Lamini, you control which models are preloaded, and how dynamic model loading will work.

## Preloaded models

To edit the list of preloaded models for your Lamini Self-Managed deployment, you need to modify the `llama_config.yaml` file.

To edit the list of preloaded models:

1. Locate the `llama_config.yaml` file in your Lamini deployment's configuration directory.

1. Look for the `batch_model_list` key under `multi_node_inference`. This list contains the models that are preloaded.

1. Edit the `batch_model_list` to add or remove models as needed. Each model must be specified by its Hugging Face model identifier (e.g. `meta-llama/Meta-Llama-3.1-8B-Instruct` for Llama 3.1).

Be conservative with the number of models you preload - each model requires a significant amount of memory.

## Dynamic model loading

Your inference GPU settings (defined in `helm_config.yaml` [for Kubernetes installations](../self_managed/kubernetes_install.md/#1-update-helm_configyaml)) affect how dynamic model loading will perform.

Inference requests for models that are not preloaded will be routed to `catchall` pods first. If a `catchall` pod is available, it will download the requested model from Hugging Face and load it into memory. If no `catchall` pods are available, requests will be routed to the other inference pods, which will download the requested model and load it into memory.

Downloading and loading a model takes significant time. We recommend allowing 20-30 minutes for a model to become available after it's first requested. Loading a new model into memory can also mean that other models will be evicted from memory. This means that rapidly requesting many different models will result in poor performance.

If you are experimenting with many different models, make sure to allocate enough `catchall` pods to handle the load without disrupting your other inference pods.

We recommend focusing development on one model or a small set of models, and preloading them. We've seen the highest accuracy and performance gains come from improving data quality and tuning recipes, rather than testing many models hoping to find one that works significantly better out of the box.

## Model downloading

Model downloading is allowed only for Lamini Platform operator.
Free user on [Lamini Cloud](https://app.lamini.ai/) is not allowed to make such calls.
You can use the following curl command to request Lamini Platform to download a model:

```shell
curl -X POST "[YOUR_API]/v1/downloaded_models/" \
    --header "Authorization: Bearer [YOUR_API_KEY]" \
    --header "Content-Type: application/json" \
    --data '{"hf_model_name": "[YOUR_MODEL]"}'
```

You can also use the `Lamini.download_model()`, see [model_download.py](../code_examples/model_download.py)
for an example.
