# lamini.Lamini.upload_file

This function can be used to upload a large file to the server for finetuning on it. Currently, it supports `jsonlines` or `csv` file.

## Parameters:

- file_path (string): The path of the file containing the data.
- input_key  (string): The column name of the input data. It defaults to `input`.
- output_key (string): The column name of the output data. It defaults to `output`.


Example file structure:

`data.jsonlines`
```json
{"input": "What's your favorite animal?","output": "dog"}
{"input": "What's your favorite color?","output": "blue"}
```

To upload the above jsonlines file, you would do:
```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.upload_file("data.jsonlines")
```


`data.csv`
```csv
user,answer
"Explain the process of photosynthesis","Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things.
"What is the capital of USA?", "Washington, D.C."
```

To upload the above csv file, you would do:

```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.upload_file("data.csv", input_key="user", output_key="answer")
```

You can subsequently train on this file using the `train` function.
```python
llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.upload_file(<file_path>)
llm.train()
```