Enforcing structured JSON schema output is important for handling LLM outputs downstream with other systems and APIs in your applications.

For an in-depth technical deep dive of how we implemented this feature, see [our blog post](https://www.lamini.ai/blog/guarantee-valid-json-output-with-lamini).

### Values other than strings

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

Please let us know if there are specific types you'd like to see supported.

=== "Python Library"

    ```python hl_lines="3"
    llm.generate(
        "How old are you in years?",
        output_type={"age": "int"}
    )
    ```

=== "REST API"

    ```sh hl_lines="7-9"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
        "out_type": {
            "age": "int"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'age': 25
    }
    ```
</details>

### Multiple outputs in JSON schema

You can also add multiple output types in one call. The output is a JSON schema that is also strictly enforced.

=== "Python Library"

    ```python hl_lines="3"
    llm.generate(
        "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
        output_type={"age": "int", "units": "str"}
    )
    ```

=== "REST API"

    ```sh hl_lines="7-10"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
        "out_type": {
            "age": "int",
            "units": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'age': 27,
        'units': 'years'
    }
    ```
</details>

Great! You've successfully run an LLM with structured JSON schema outputs.

!!! tip

    Make sure your output type keys are prompt-tuned to produce the desired output!
    For example:

    ```
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
        "out_type": {
                "age": "int",
                "units": "str"
            }
    ```

    returns

    ```
    {"age":30,"units":"years"}
    ```

    But

    ```
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
        "out_type": {
                "response": "int",
                "units": "str"
            }
    ```

    returns

    ```
    {"response":404,"units":"meters"}
    ```
