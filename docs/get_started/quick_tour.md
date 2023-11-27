# Quick Tour

Get LLMs in production in 2 minutes with Lamini!

First, get `<YOUR-LAMINI-API-KEY>` at [https://app.lamini.ai/account](https://app.lamini.ai/account).

Add the key as an environment variable. Or, authenticate via the Python library below.
```bash
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

Next, run an LLM:

=== "Python Library"
    Install the Python library.

    ```python
    pip install --upgrade lamini
    ```

    Run an LLM with a few lines of code.
    ```python
    import lamini

    lamini.api_key = "<YOUR-LAMINI-API-KEY>" # or set as environment variable above
    
    llm = lamini.LlamaV2Runner()
    print(llm("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>

    > "Hello! I'm just an AI, I don't have feelings or emotions like humans do, but I'm here to help you with any questions or concerns you may have. I'm programmed to provide respectful, safe, and accurate responses, and I will always do my best to help you. Please feel free to ask me anything, and I will do my best to assist you. Is there something specific you would like to know or discuss?"

    </details>

    That's it! 🎉

=== "Bash (REST API)"

    Run an LLM with one CURL command.

    ```bash
    curl --location "https://api.lamini.ai/v2/lamini/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "LaminiTest",
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt_template": "<s>[INST] <<SYS>>\n{input:system}\n<</SYS>>\n\n{input:instruction} [/INST]",
        "in_value": {
            "system": "You are a helpful assistant.",
            "instruction": "How are you?"
        },
        "out_type": {
            "Answer": "str"
        }
    }'
    ```
    <details>
    <summary>Expected Output</summary>

    JSON result with key `Answer` of type `str`:
    
    > {
        "Answer":"  Hello! *adjusts glasses* I'm feeling quite well, thank you for asking! It's always a pleasure to assist you. How may I be of service today? Is there something specific you need help with?"
    }
    </details>
    
    That's it! 🎉



More details and options in [Install](install.md).

You just ran inference. What's next?
* Better inference: customize your inference call
* Bigger inference: batching requests
* Training: build your own LLM with finetuning and more
* Better training: customize your training call
* Bigger training: efficiently train LoRAs and more advanced methods

## Better inference

Customize inference in many ways. Easy ways:
* Change the prompt template.
* Change the model.
* Change the input and output types.
* Output multiple values.

More json schema.

## Bigger inference

Batch processes.

## Training