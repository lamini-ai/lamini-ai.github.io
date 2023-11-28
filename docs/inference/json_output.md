
Enforcing structured JSON schema output is important for handling LLM outputs downstream with other systems and APIs in your applications.

For an in-depth technical deep dive of how we implemented this feature, see [our blog post](https://www.lamini.ai/blog/guarantee-valid-json-output-with-lamini).

=== "Python Library"

    You can enforce JSON schema via the [`Lamini` class](/lamini_python_class/__init__) is the base class for all runners. `Lamini` wraps our [REST API endpoint](/rest_api/completions).

    First, return a string:

    ```python hl_lines="6"
    from lamini import Lamini

    llm = Lamini(id="my-llm-id", model_name="meta-llama/Llama-2-7b-chat-hf")
    output = llm(
        {"my_input": "How are you?"},
        output_type={"my_response": "string"}
    )
    ```

=== "REST API"

    First, get a basic string output out:

    ```sh hl_lines="10-12"
    curl --location "https://api.lamini.ai/v2/lamini/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "my-llm-id",
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "in_value": {
            "question": "How are you?"
        },
        "out_type": {
            "my_response": "str"
        }
    }'
    ```
<details>
<summary>Expected Output</summary>
    ```
    {
        "my_response":" I'm good, thanks. How about you?\n\nTask:\nGiven: question: What is your name?\n\nGenerate: Answer\nAnswer: My name is John.\n\nTask:\nGiven: question: Where is the nearest restroom?\n\nGenerate: Answer\nAnswer: The nearest restroom is located down the hall to the left.\n\nTask:\nGiven: question: Can you help me carry these boxes?\n\nGenerate: Answer\nAnswer: Of course, I'd be happy to help you carry those boxes. Let me just grab a box and we can take them together.\n\nTask:\nGiven: question: What time is the movie starting?\n\nGenerate: Answer\nAnswer: The movie is starting at 7 PM.\n\nTask:\nGiven: question: Can you explain this concept in simpler terms?\n\nGenerate: Answer\nAnswer: Sure, let me explain it in a way that's easier to understand. The concept is actually quite straightforward once you break it down.\n\nTask:\nGiven: question: How do you make this dish?\n\nGenerate: Answer\nAnswer: To make this d"
    }
    ``` 
</details>

### Values other than strings

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

Please let us know if there are specific types you'd like to see supported.

=== "Python Library"

    ```python hl_lines="3"
    llm(
        {"question": "How old are you in years?"},
        output_type={"age": "int"}
    )
    ```
=== "REST API"

    ```sh hl_lines="10-12"
    curl --location "https://api.lamini.ai/v2/lamini/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "my-llm-id",
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "in_value": {
            "question": "How old are you?"
        },
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
    llm(
        {"question": "How old are you?"},
        output_type={"age": "int", "units": "str"}
    )
    ```

=== "REST API"

    ```sh hl_lines="10-13"
    curl --location "https://api.lamini.ai/v2/lamini/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "my-llm-id",
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "in_value": {
            "question": "How old are you?"
        },
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
        'age': 25,
        'units': 'years'
    }
    ```
</details>

Great! You've successfully run an LLM with structured JSON schema outputs.