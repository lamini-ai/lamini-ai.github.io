# lamini.Lamini.generate

Runs the instantiated LLM engine.

```python
from lamini import Lamini

llm = Lamini(id="example")
llm.generate(prompt, output_type)
```

## Parameters

-   prompt: `str or list[str]` - the prompt
-   output_type: `dict` - the type of the output

## Returns

output: `dict` - output of the LLM, based on `prompt`, in the type specified by `output_type`

## Example

```python
llm = Lamini(id="my_llm_name", model_name="meta-llama/Llama-2-7b-chat-hf")

prompt = "What are llamas?"
my_output = llm.generate(prompt, output_type={"output": "string"})

prompt = ["What are llamas?", "What are alpacs?"]
my_output = llm.generate(prompt, output_type={"output": "string"})
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
* base_delay: `number` - Default to 10 seconds. In each retry attempt, `delay = base_delay * 2 ** num_retry`

Example
```python
my_output = llm.generate(prompt, output_type={"output": "string"}, max_retries=3, base_delay=2)
```