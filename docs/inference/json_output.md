
Enforcing structured JSON schema output is important for handling LLM outputs downstream with other systems and APIs in your applications.

For an in-depth technical deep dive of how we implemented this feature, see [our blog post](https://www.lamini.ai/blog/guarantee-valid-json-output-with-lamini).

=== "Python SDK"

    You can enforce JSON schema via the [`Lamini` class](../lamini_python_class/lamini.md), which is the base class for all runners. `Lamini` wraps our [REST API endpoint](../api.md).

    First, return a string:

    ```python hl_lines="6"
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Llama-3.1-8B-Instruct")
    output = llm.generate(
        "How are you?",
        output_type={"answer": "str"}
    )
    ```

=== "REST API"

    First, get a basic string output out:

    ```sh hl_lines="7-9"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-3.1-8B-Instruct",
        "prompt": "How are you?",
        "output_type": {
            "answer": "str"
        }
    }'
    ```
<details>
<summary>Expected Output</summary>
    ```
    {
        "answer":"I'm doing well, thanks for asking! How about you"
    }
    ```
</details>

### Values other than strings

You can change the output type to be a different type. This typing is strictly enforced.  We currently support `str`, `int`, `float`, `bool`, and enums structured as str lists, or int lists. For example, `"answer": ["A","B","C","D"]` would always return one of `A`, `B`, `C`, or `D` for the `answer` field. `"answer": [1, 2, 3]` would always return one of `1`, `2`, or `3` for the `answer` field.

Please let us know if there are additional types you'd like to see supported.

Examples

=== "Python SDK"

    ```python hl_lines="3"
    llm.generate(
        "How old are you?",
        output_type={"age": "int"}
    )
    ```

=== "Python SDK"

    ```python hl_lines="3"
    llm.generate(
        "Pick a color.",
        output_type={"name": ["red", "white", "blue"]}
    )
    ```

=== "Python SDK"

    ```python hl_lines="3"
    llm.generate(
        "Pick an odd digit",
        output_type={"name": [1, 3, 5, 7, 9]}
    )
    ```

=== "REST API"

    ```sh hl_lines="7-9"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-3.1-8B-Instruct",
        "prompt": "How old are you?",
        "output_type": {
            "age": "int"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        "age": 25
    }
    ```
</details>

### Multiple outputs in JSON schema

You can also add multiple output types in one call. The output is a JSON schema that is also strictly enforced.

=== "Python SDK"

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
        "model_name": "meta-llama/Llama-3.1-8B-Instruct",
        "prompt": "How old are you?",
        "output_type": {
            "age": "int",
            "units": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        "age": 25,
        "units": "years"
    }
    ```
</details>

Great! You've successfully run an LLM with structured JSON schema outputs.

## Known issue: JSON output truncation

Truncation may occur when JSON output generates double quotation marks ("). This is a known limitation with using `output_type` since a quotation at the end of the output and a quotation as a part of the output are not distinguished.

### Workaround

* Use prompt tuning instead of output type if the response may contain double quotation marks. e.g. "Only return the relevant quote, do not include any other text".
* Use prompt tuning to avoid generating double quotation marks. e.g. "Only use single quotes when there is dialogue".
* [Contact us](https://www.lamini.ai/contact) to discuss alternative solutions or workarounds for your use case.

### Future support

We are evaluating the feasibility of improving our system to handle double quotes in JSON output in the future. If we decide to support this feature, we will update our documentation and notify users.

## Known issue: Long JSON output times out

To ensure that requests complete in a reasonable amount of time, there is a time limit on all requests including json requests. If your requests exceeds the time limit, try guiding the model to generate a shorter json object, e.g. write a description in 3 sentences or less. Timed out requests may result in failed, incomplete, or missing output.

### Workaround

* Reduce the size of the output by limiting the number of fields or the prompt.
* Break down the JSON output into separate smaller requests.
* [Contact us](https://www.lamini.ai/contact) to discuss alternative solutions or workarounds for your use case.

### Future support

We are evaluating the feasibility of improving our system to handle large JSON output in the future. If we decide to support this feature, we will update our documentation and notify users.

Feel free to [contact us](https://www.lamini.ai/contact) with any questions or concerns.
