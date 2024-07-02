# Large Data Files

If you are tuning on a large file of data, you can use the `upload_file` function to first upload the file onto the servers.

Here is an example with a `test.csv` file:

```txt
// code/test.csv
```

You can use the Lamini to tune on this file directly by uploading the file and specifying the input and output keys.

```py
# code/large_data_files_csv.py
```

Alternatively, you can also use `jsonlines` files

<details>
    <summary>Using <code>test.jsonl</code></summary>

    ```json5
    // code/test.jsonl
    ```

    Then tune on this file using the `tune` function.

    ```py
    # code/large_data_files_jsonl.py
    ```
