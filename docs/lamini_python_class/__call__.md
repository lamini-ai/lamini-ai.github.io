# lamini.Lamini.call

Runs the instantiated LLM engine.

```
llm = Lamini()
llm.generate(prompt, output_type)
```

## Parameters

- prompt: `str` - name of the LLM engine instance
- output_type: `Optional[dict]` - the type of the output

## Returns

output: `dict` - output of the LLM, based on `prompt`, in the type specified by `output_type`

## Example

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")

my_output = llm.call(my_input)
```
