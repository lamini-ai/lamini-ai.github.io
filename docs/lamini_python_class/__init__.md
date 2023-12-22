# lamini.Lamini.\_\_init\_\_

Class that instantiates the Lamini class for calling and training models.

```python
Lamini(model_name, config)
```

## Attributes

- model_name: `str` - name of the base model, for example `meta-llama/Llama-2-7b-chat-hf`.
- config: `dict` (Optional) - auth-related parameters, e.g. token

## Example

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
```

With optional paramters:
```python
import os
key = os.environ.get("LAMINI_API_KEY")

llm = Lamini(
    model_name="meta-llama/Llama-2-7b-chat-hf",
    config={
        "production": {
            "key": key,
        }
    },
)
```

See [advanced authentication options](../advanced_auth.md) for more details.
