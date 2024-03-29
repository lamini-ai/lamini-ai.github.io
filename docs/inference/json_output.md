
Enforcing structured JSON schema output is important for handling LLM outputs downstream with other systems and APIs in your applications.

For an in-depth technical deep dive of how we implemented this feature, see [our blog post](https://www.lamini.ai/blog/guarantee-valid-json-output-with-lamini).

=== "Python Library"

    You can enforce JSON schema via the [`Lamini` class](/lamini_python_class/__init__) is the base class for all runners. `Lamini` wraps our [REST API endpoint](/rest_api/completions).

    First, return a string:

    ```python hl_lines="6"
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
    output = llm.generate(
        "How are you?",
        output_type={"my_response": "string"}
    )
    ```

=== "REST API"

    First, get a basic string output out:

    ```sh hl_lines="7-9"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "How are you?",
        "out_type": {
            "my_response": "str"
        }
    }'
    ```
<details>
<summary>Expected Output</summary>
    ```
    {
        'my_response': "I'm good, thanks for asking! How about you"
    }
    ```
</details>

### Values other than strings

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

Please let us know if there are specific types you'd like to see supported.

=== "Python Library"

    ```python hl_lines="3"
    llm.generate(
        "How old are you?",
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
        "prompt": "How old are you?",
        "out_type": {
            "response": "int"
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
        "How old are you?",
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
        "prompt": "How old are you?",
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
        'age': 30,
        'units': 'years'
    }
    ```
</details>

Great! You've successfully run an LLM with structured JSON schema outputs.
