Customize inference in many ways:

- Change the prompt, model, and output type.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run applications like RAG (Retrieval Augmented Generation).

## Run Lamini with Llama 3
=== "Python SDK"

    The Python SDK offers higher-level class, `Lamini`, to work with models.
    ```python hl_lines="3"
    from lamini import Lamini

    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
    print(llm.generate("How are you?", output_type={"Response":"str"}))
    ```

=== "REST API"

    You can run inference with one CURL command.

    ```sh hl_lines="5"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": "How are you?",
        "output_type": {
            "Response": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'Response': "I'm doing well, thanks for asking! How about you"
    }
    ```
</details>

Since Llama 3 assumes the Llama 3 prompt template, you will need to include it for further prompt tuning. This prompt template looks like this:
```python
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>

{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```
The `{system}` variable is a system prompt that tells your LLM how it should behave and what persona to take on. By default, it is that of a helpful assistant. The `{instruction}` variable is the instruction prompt that tells your LLM what to do. This is typically what you view as the prompt, e.g. the question you want to ask the LLM.

## Run Lamini with Mistral
=== "Python SDK"

    ```python hl_lines="3"
    from lamini import Lamini

    llm = Lamini(model_name='mistralai/Mistral-7B-Instruct-v0.2')
    print(llm.generate("How are you?", output_type={"Response":"str"}))
    ```

=== "REST API"

    ```sh hl_lines="5"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": "How are you?",
        "output_type": {
            "Response": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'Response': "I'm just a computer program, I don't have feelings or emotions. I'm here to help answer any questions you might have to the best of my ability"
    }
    ```
</details>
