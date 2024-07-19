Start using LLMs in just 2 steps with Lamini!

## 1. Authenticate

First, get `<YOUR-LAMINI-API-KEY>` at [https://app.lamini.ai/account](https://app.lamini.ai/account). Need help? Check out [API Auth](/authenticate).

## 2. Run inference
Next, run Lamini:

=== "Python SDK"

    Install the Python SDK.

    ```python
    pip install --upgrade lamini
    ```

    Run an LLM with a few lines of code.

    ```py
    # code/quick_start.py
    ```

=== "REST API"

    Run an LLM with one CURL command.

    ```bash
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
            "prompt": "How are you?",
            "output_type": {"Response": "str"}
        }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {"Response":"I'm doing well, thanks for asking! How about you"}
    ```
</details>

That's it! 🎉

Now you can try:

- Changing the prompt, model, and output type.
- Output multiple values in [structured JSON](./json_output.md).
- [Batching your inference calls](./batching.md) to get high throughput.
- Run applications like [RAG (Retrieval Augmented Generation)](https://github.com/lamini-ai/lamini-examples/blob/main/04_rag_tuning/README.md).
