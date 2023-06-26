# Filters

Clean your data with our dataset filters, or add your own custom ones! Here is an example of how to do so:

```python
from llama.tools.filters import dedupe, dedupe_with_indices, balance

# Input
class Question(Type):
    question: str = Context("a question")

# Output
class Answer(Type):
    answer: str = Context("a response to question")

dataset = [[Question(question='What is Lamini?'), Answer(answer='Lamini is the LLM platform for every developer to build customized, private models: easier, faster, and better-performing than any general purpose LLM..')], ...]

# filter out duplicates from dataset
deduped_dataset = dedupe(dataset, mode='exact') # default, choose from ['exact', 'minimal', 'aggressive']
deduped_indices = dedupe_with_indices(dataset, mode='exact') # default, choose from ['exact', 'minimal', 'aggressive']
print(deduped_indices) # see which indices were removed

# balance deduped dataset
deduped_and_balanced_dataset = balance(deduped_dataset, field='answer', mode='exact') # balance dataset using 'answer' field of output
```