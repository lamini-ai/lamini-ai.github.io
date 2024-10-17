# Large Data Files

If you are tuning on a large file of data, you can use the `upload_file` function to first upload the file onto the servers.

Here is an example with a `test.csv` file:

```txt
// code/test.csv

user,answer
"Explain the process of photosynthesis","Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things.
"What is the capital of USA?", "Washington, D.C."

```

You can use the Lamini to tune on this file directly by uploading the file and specifying the input and output keys.

```py
# code/large_data_files_csv.py

from lamini import Lamini

llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
dataset_id = llm.upload_file("test.csv", input_key="user", output_key="answer")

llm.tune(data_or_dataset_id=dataset_id)

```

Alternatively, you can also use `jsonlines` files

<details>
    <summary>Using <code>test.jsonl</code></summary>

    ```json5
    // code/test.jsonl
    
    {"user": "Explain the process of photosynthesis", "answer": "Photosynthesis is the process by which plants and some other organisms convert light energy into chemical energy. It is critical for the existence of the vast majority of life on Earth. It is the way in which virtually all energy in the biosphere becomes available to living things."}
    {"user": "What is the capital of USA?", "answer": "Washington, D.C."}
    
    ```

    Then tune on this file using the `tune` function.

    ```py
    # code/large_data_files_jsonl.py
    
    from lamini import Lamini
    
    llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
    dataset_id = llm.upload_file("test.jsonl", input_key="user", output_key="answer")
    
    llm.tune(data_or_dataset_id=dataset_id)
    
    ```
