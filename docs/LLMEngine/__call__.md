# llama.LLMEngine.\_\_call\_\_

Runs the instantiated LLM engine.

```
llm = LLMEngine(id="example")
llm(input, output_type, input_type)
```

## Parameters

-   input: `<class llama.Type>` - name of the LLM engine instance
-   output_type: `<class llama.Type>` - the type of the output
-   input_type: `<class llama.Type>` (Optional) - the type of the input (also inferred by the engine with `input`, so it is optional)

## Returns

output: `<class 'llama.Type>` - output of the LLM, based on `input`, in the type specified by `output_type`

## Example

```python
llm = LLMEngine(id="my_llm_name", model_name="meta-llama/Llama-2-7b-chat-hf")

my_output = llm(my_input, output_type=MyOutputType)
```
