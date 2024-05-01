# lamini.Lamini.generate

Runs the instantiated LLM engine.

```python
llm = Lamini(model_name=model_name)
llm.generate(prompt)
```

## Parameters

-   prompt: `str or list[str]` - the prompt
-   (optional) output_type: `dict` - the type of the output

## Returns

output: `dict` - output of the LLM, based on `prompt`, in the type specified by `output_type`. If not specified, output will be what the model chooses to return (most commonly a String).

## Example

```python
from lamini import Lamini

llm = Lamini(model_name="mmeta-llama/Meta-Llama-3-8B-Instruct")

prompt = "What are llamas?"
my_output = llm.generate(prompt)
my_output_str = llm.generate(prompt, output_type={"output": "string"})

prompts = ["What are llamas?", "What are alpacas?"]
my_outputs = llm.generate(prompts)
```

## Fault Tolerance

### Local Cache File

You can use `local_cache_file` to specify a path on your local machine to store the inference results.
In the event of a failure during a set of inference jobs, restarting will quickly retrieve existing results from the local cache, significantly speeding up the process compared to fetching results from the server again.

Example
```python
my_output = llm.generate(prompt, output_type={"output": "string"}, local_cache_file='my_cache.txt')
```

### Retries

`max_retries` and `base_delay` can be used to automatically retry inference.

* max_retries: `int` - Default to 0. Max number of attempts to retry inference
* base_delay: `number` - Default to 10 seconds. In each retry attempt, `delay = base_delay * 2 ** iteration_num`

Example
```python
my_output = llm.generate(prompt, output_type={"output": "string"}, max_retries=3, base_delay=2)
```
