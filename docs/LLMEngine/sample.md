# LLMEngine.sample

Generate a list of unique outputs.

```python
llm = LLMEngine(id="example")
job = llm.sample(input, output_type, n, *args, **kwargs)
```

## Parameters

-   input: `Union[Type, List[Type]]` - input data
-   output_type: `<class 'llama.types.type.Type'>` - the desired data type of returned ouput
-   n: `int` - number of samples to generate

## Returns

output: `list` - a list of Type objects
