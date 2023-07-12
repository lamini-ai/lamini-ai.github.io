# llama.LLMEngine.eval

After training, quickly understand how the model has improved using this function.

```python
results = llm.train()
eval_results = llm.eval(results['job_id'])
print(eval_results)
```

## Returns

eval_results: `list` - a list of input output pairs resulting from the evaluation of the trained model against the test set.
