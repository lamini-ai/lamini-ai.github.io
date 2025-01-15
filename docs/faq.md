# FAQ

## Core Development Questions

### How do I set up authentication?
See the [Authentication guide](authenticate.md) for getting and configuring your Lamini API key.

### How does model loading work?
- Model weights are loaded to GPU memory once and persist between requests
- Loading only happens on initial startup or after unexpected events
- Loading time scales with model size

### What systems can I develop with Lamini on?
- Recommended: Ubuntu 22.04+ with Python 3.10-3.12
- Not officially supported on Windows (use Docker with Linux container instead)

## Training & Tuning

### What models can I use?
Check the [Models](models.md) page for the full list of supported models.

### How long can training jobs run?
- Default timeout: 4 hours
- Jobs automatically checkpoint and resume if timeout occurs
- For longer runs:
  - Request more GPUs via `gpu_config`
  - Contact us for dedicated instances

### Can I disable memory tuning (MoME)?
Yes, use these settings for cases like summarization where qualitative output is preferred:
```python
finetune_args={
  "batch_size": 1,
  "index_ivf_nlist": 1,
  "index_method": "IndexFlatL2",
  "index_max_size": 1,
}
```

### How does Lamini optimize model training?
- Uses LoRAs (low-rank adapters) automatically
- 266x fewer parameters than full model finetuning
- 1.09B times faster model switching
- No manual configuration needed

## Infrastructure

### Why might my job be queued?
The On-Demand plan uses shared resources. For dedicated compute:
- Consider Lamini Reserved plans
- Contact us about running on your own infrastructure

### What GPU can Lamini run on?
- Lamini can run on AMD and NVIDIA GPUs

### How do I get started with Lamini private servers or enterprise plans?
- [Contact us](https://www.lamini.ai/contact) to learn more about our reserved plans
- Run your own jobs on dedicated compute
