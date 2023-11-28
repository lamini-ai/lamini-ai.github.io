
A common use case is to pretrain your LLM on a large dataset, e.g. Wikipedia, to improve its general knowledge. This is called "continued pretraining" or "domain adaptation" for learning this content on top of the basic language skills of a pretrained LLM, or "pretraining from scratch" if you're starting from a randomly initialized LLM.

The first step of doing this is similar to finetuning. However, you can instead do less preparation of your data. However, we recommend 1B tokens, or about 250M words, of data for a difference in performance.

You just need a file with dictionaries with the key "text" in it, and that's it -- not target outputs. Just let the LLM read it unprocessed. One of the most common use cases is to autocomplete large technical texts, e.g. using our `AutocompleteRunner`.

```python hl_lines="3 4"
from lamini import AutocompleteRunner

llm = AutocompleteRunner(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.load_data_from_strings(["list", "of", "strings"]) 
llm.train()
```

Please sign into your Organizations Tier account to access further content.
