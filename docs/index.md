# Quick Start

Start using LLMs in just 2 steps with Lamini!

First, get `<YOUR-LAMINI-API-KEY>` at [https://app.lamini.ai/account](https://app.lamini.ai/account).

Next, run an LLM:

=== "Python SDK"

    Install the Python SDK.

    ```python
    pip install --upgrade lamini
    ```

    Run an LLM with a few lines of code.

    ```python
    import lamini
    lamini.api_key = "<YOUR-LAMINI-API-KEY>"

    llm = lamini.Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
    print(llm.generate("How are you?", output_type={"Response":"str"}))
    ```

    <details>
    <summary>Expected Output</summary>
        ```
        {'Response': "I'm doing well, thanks for asking! How about you"}
        ```
    </details>

    That's it! 🎉

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

More details and options in [Authenticate](get_started/authenticate).

## Inference

Customize inference in many ways:

- Change the prompt, model, and output type.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run applications like RAG (Retrieval Augmented Generation).

You can step through all of these in the [Inference section](inference/quick_tour.md).


## Tuning

When running inference, with prompt-engineering and RAG, is not enough for your LLM, you can tune it. This is harder but will result in better performance, better leverage of your data, and increased knowledge and reasoning capabilities.

There are many ways to tune your LLM. We'll cover the most common ones here:

- Basic tuning: build your own LLM for specific domain knowledge or task with finetuning, domain adaptation, and more
- Better tuning: customize your tuning call and evaluate your LLM
- Bigger tuning: pretrain your LLM on a large dataset, e.g. Wikipedia, to improve its general knowledge

You can learn how to do these in the [Tuning section](training/quick_tour.md).

## Examples

Want to see full code examples? Check out [our SDK Repo on Github](https://github.com/lamini-ai/lamini-sdk/tree/main)!
