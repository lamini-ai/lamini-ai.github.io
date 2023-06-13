# llama.LLMEngine.\_\_init\_\_

Class that instantiates the LLMEngine.

```python
LLMEngine(id, model_name, config)
```

## Attributes

-   id: `str` - name of the model you're working on.
-   model_name: `str` (Optional) - name of the base model, defaults to OpenAI's `text-davinci-003`.
-   config: `dict` (Optional) - auth-related parameters, e.g. token

## Example

```python
llm = LLMEngine(id="my_llm_name")

# With optional parameters
llm = LLMEngine(
        id="my_llm_name",
        model_name="chat-gpt",
        config={"production.key": "lamini_token"}
      )
```
