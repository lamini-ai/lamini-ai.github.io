# lamini.Lamini.\_\_init\_\_

Class that instantiates the Lamini.

```python
Lamini(id, model_name, config, prompt_template)
```

## Attributes

-   id: `str` - name of the model you're working on.
-   model_name: `str` - name of the base model, for example `meta-llama/Llama-2-7b-chat-hf`.
-   config: `dict` (Optional) - auth-related parameters, e.g. token
-   prompt_template: `str` (Optional) - prompt template to use during inference and training. 

## Example

```python
llm = Lamini(id="my_llm_name", model_name="meta-llama/Llama-2-7b-chat-hf")

# With optional parameters
llm = Lamini(
        id="my_llm_name",
        model_name="meta-llama/Llama-2-7b-chat-hf",
        prompt_template="{input:question}" # change this based on your expected input
      )
```
