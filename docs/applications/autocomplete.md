# Autocomplete

Autocomplete is a common use case for LLMs. It is also one of the easiest to implement. You can use our `AutocompleteRunner` to do this. For example, you may have custom code like Github Copilot to train your own LLM on, or you'd like to autocomplete your own emails.

The first step of doing this is similar to instruction finetuning for chat applications. However, you can instead do less preparation of your data - it can just be the text, without explicit input or output formats. We recommend 1B tokens, or about 250M words, of data for a difference in performance.

You just need a file with dictionaries with the key "text" in it, and that's it -- not target outputs. Just let the LLM read it unprocessed. One of the most common use cases is to autocomplete large technical texts, e.g. using our `AutocompleteRunner`.

```python hl_lines="3 4"
from lamini import AutocompleteRunner

llm = AutocompleteRunner(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.load_data_from_strings(["list", "of", "strings"]) 
llm.train()
llm.evaluate()
```

This runner will assess the LLM for the autocomplete task. View results in the Train tab of the [Lamini app](https://app.lamini.ai/train).
