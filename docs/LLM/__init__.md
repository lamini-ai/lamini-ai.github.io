# llama.LLM.\_\_init\_\_

Class that instantiates the LLM engine.

```python
LLM(name, model_name, config)
```

## Attributes

-   name: `str` - name of the LLM engine instance
-   model_name: `str` (Optional) - name of the base model, defaults to OpenAI's `text-davinci-003`.
-   config: `dict` (Optional) - auth-related parameters, e.g. token

## Example

```python
llm = LLM(name="my_llm_name")

# With optional parameters
llm = LLM(
        name="my_llm_name",
        model_name="chat-gpt",
        config={"token": "my_token"}
      )
```
