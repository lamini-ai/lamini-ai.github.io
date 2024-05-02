# lamini.Lamini.\_\_init\_\_

Class that instantiates the Lamini.

```python
Lamini(model_name, config)
```

## Attributes

-   model_name: `str` - name of the base model, for example `meta-llama/Meta-Llama-3-8B-Instruct`.
-   config: `dict` (Optional) - auth-related parameters, e.g. token
-   api_key: `str' (Optional) - API key
-   api_url: `str' (Optional) - API URL
-   local_cache_file: `str' (Optional) - Local cache dile

## Example

```python
llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")

# With optional parameters
llm = Lamini(
        model_name="meta-llama/Meta-Llama-3-8B-Instruct",
        api_key=lamini_api_key
      )
```
