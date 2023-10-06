# lamini.Lamini.\_\_call\_\_

Runs the instantiated LLM engine.

```
llm = Lamini(id="example")
llm(input, output_type)
```

## Parameters

-   input: `dict` - name of the LLM engine instance
-   output_type: `dict` - the type of the output

## Returns

output: `dict` - output of the LLM, based on `input`, in the type specified by `output_type`

## Example

```python
llm = Lamini(id="my_llm_name", model_name="meta-llama/Llama-2-7b-chat-hf")

my_output = llm(my_input, output_type={"output": "string"})
```
