# lamini.Lamini.upload_file

This function can be used to upload a large file to the server for finetuning on it.

```python
llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
llm.upload_file(<file_path>)
```

Make sure that the data in the file is in the following format:

```json
[
{"input": "What's your favorite animal?","output": "dog"},
{"input": "What's your favorite color?","output": "blue"},
    ...
]
```

You can subsequently train on this data using the `train` function.

```python
llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
llm.upload_file(<file_path>)
llm.train()
```
