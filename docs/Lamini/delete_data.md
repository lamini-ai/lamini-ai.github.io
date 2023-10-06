# lamini.Lamini.delete_data

Delete datasets associated with the provided Lamini Engine id.
```python
llm = Lamini(id="example", model_name="meta-llama/Llama-2-7b-chat-hf")
response = llm.delete_data()
```

## Returns

response: `dict` - a dictionary object with field `deleted`confirming that number of datasets that were deleted. If `0` is returned, there were no datasets previously persisted. Datasets are only persisted when explicitly saved using `Lamini.save_data` or `Lamini.save_data_pairs`.

```json
{
  "deleted": 1
}
```