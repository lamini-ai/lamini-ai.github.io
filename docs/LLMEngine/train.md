# llama.LLMEngine.train

Train a LLM. This function will submit a training job and continuously poll until the job is completed. You can monitor the job at [https://app.lamini.ai/train](https://app.lamini.ai/train).

```python
llm = LLMEngine(id="example")
llm.save_data(data)
results = llm.train()
```

## Returns

results: `list` - a list of input output pairs resulting from the evaluation of the trained model against the test set.
