# lamini.Lamini.generate

Runs the instantiated LLM engine.

```
llm = Lamini(model_name)
llm.generate(prompt, output_type)
```

## Parameters

- prompt: `str` or `List[str]` - name of the LLM engine instance
- output_type: `Optional[dict]` - the type of the output in JSON (guaranteed)
- max_tokens: `Optional[int]` - max number of tokens to generate (cannot be used with `output_type`)


## Returns

output: `dict` - output of the LLM, based on `prompt`, and if `output_type` is specified, then in the type(s) specified by `output_type`

## Example

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
my_output = llm.generate("What's your age?")
```

With `output_type` to return guaranteed JSON:

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
my_output = llm.generate(
    prompt="What's your age?",
    output_type={"age": "int", "units": "str"}
)
```

With `max_tokens` to limit the number of tokens generated:

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
my_output = llm.generate(
    prompt="What's your age?",
    max_tokens=5
)
```