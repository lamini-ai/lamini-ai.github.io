Different models have different system prompt templates. Using the correct template when prompt tuning can have a large effect on model performance.

When you're trying a [new model](../models.md), it's a good idea to review the model card on Hugging Face to understand what (if any) system prompt template it uses.

## Llama 3

The [Llama 3](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) prompt template looks like this:
```python
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>

{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```
The `{system_prompt}` variable is a system prompt that tells your LLM how it should behave and what persona to take on. By default, it is that of a helpful assistant. The `{user_message}` variable is the instruction prompt that tells your LLM what to do. This is typically what you view as the prompt, e.g. the question you want to ask the LLM.

=== "Python SDK"

    ```py
    # code/llama_3_prompt.py
    ```

=== "REST API"

    ```sh hl_lines="6"
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
            "prompt": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n You are a pirate. Say arg matey! <|eot_id|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
            "output_type": {
                "Response": "str"
            }
        }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {'Response': "Ahoy, matey! I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. The sun be shinin' bright, the wind be blowin' strong, and me trusty cutlass be by me side. What more could a pirate ask for, eh? Arrr"}
    ```
</details>

## Mistral v2

[Mistral v2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) uses a different format. In order to leverage instruction fine-tuning, your prompt should be surrounded by [INST] and [/INST] tokens.

=== "Python SDK"

    ```py
    # code/mistral.py
    ```

=== "REST API"

    ```sh hl_lines="5"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": "<s>[INST] How are you? [/INST]",
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
