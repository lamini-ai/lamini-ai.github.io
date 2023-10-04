# llama.LLMEngine.\_\_init\_\_

Class that instantiates the LLMEngine.

```python
LLMEngine(id, model_name, config)
```

## Attributes

-   id: `str` - name of the model you're working on.
-   model_name: `str` - name of the base model, for example `meta-llama/Llama-2-7b-chat-hf`.
-   config: `dict` (Optional) - auth-related parameters, e.g. token

## Example

```python
llm = LLMEngine(id="my_llm_name", model_name="meta-llama/Llama-2-7b-chat-hf")

# With optional parameters
llm = LLMEngine(
        id="my_llm_name",
        model_name="meta-llama/Llama-2-7b-chat-hf",
        config={"production.key": "lamini_token"}
      )
```
