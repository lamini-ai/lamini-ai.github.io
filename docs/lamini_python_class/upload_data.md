# lamini.Lamini.upload_data

Upload data for training. This method gets called inside `lamini.Lamini.train`. You can use this method directly to get dataset id's and upload data for training without kicking off a training job.

Specify the data as an argument to `lamini.Lamini.upload_data`

```python
data = [
    {"input": "What's your favorite animal?", "output": "dog"},
    {"input": "What's your favorite color?", "output": "blue"},
    ...
]
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.upload_data(data)
```

This will print out a `dataset_id` which can be used to persist the data across multiple runs.

```
Your dataset id is: 85e27a2e28bbfd526d0f7bb902b2a987b1f7632b556d77c02ca06dad76e57fcc . Consider using this in the future to train using the same data.
Eg: llm.train(dataset_id='85e27a2e28bbfd526d0f7bb902b2a987b1f7632b556d77c02ca06dad76e57fcc')

Uploading data....
Upload to blob completed for data.
Data pairs uploaded to blob.
```

Persisted data will be evicted after a month of storage, and we recommend that you manage your data separately.
