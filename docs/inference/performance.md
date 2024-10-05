Inference performance is a function of model size, prompt size, response size, and compute speed, and can be measured in a variety of ways (queries per second, tokens per second, time to first token, etc.). It's complicated!

## How to improve performance and handle truncated responses

Inference responses can be truncated (cut off, or appear incomplete) because the request could not be completed in the time allotted (timeout), or because the response size exceeded the `max_new_tokens` parameter (length).

1. First, review your prompt and requested responses: can you shorten them? When you're experimenting, it's easy to accumulate extraneous information in the prompt, or to request more output than you actually need. Prompt tuning is often a quick win, especially when combined with [structured output](json_output.md).

1. Try using [Generation Pipelines](https://github.com/lamini-ai/lamini-examples/blob/main/05_data_pipeline/README.md) for more efficient execution.

1. If you're still having trouble, check whether your request set a value for `max_new_tokens`.

Lamini's [completions API](../rest_api/completions.md) has an optional `max_new_tokens` parameter that limits the response size. Lamini uses this parameter to efficiently allocate GPU memory. However, this comes with risks:

  - If you set the token limit too short, your requests may get truncated. The LLM is not aware of the token limit.
  - Very large token limits consume substantial memory, which slows down processing, which may cause timeouts.

If you're setting a value for `max_new_tokens` and your responses are truncated at that value, you're hitting the token limit. Try a higher value for `max_new_tokens`.

If you're setting a value for `max_new_tokens` and your response was truncated at less than that value, you're probably hitting a timeout. Try a lower value for `max_new_tokens`.

