# llama.LLMEngine.evaluate

After training, quickly understand how the model has improved using this function.

```python
llm.train()
evaluation = llm.evaluate()

# Different ways to access evaluations (equivalent, also available in UI)
print(evaluation)
print(llm.evaluation)
assert evaluations == llm.evaluation
```

## Returns

evaluation: `dict` - a dict with the job ID and a list of input output pairs resulting from the evaluation of the trained model against the test set. Also available through the model class, as `llm.evaluation`.