# Quick Tour

Get LLMs in production in minutes with Lamini!

First, get `<YOUR-LAMINI-API-KEY>` at [https://app.lamini.ai/account](https://app.lamini.ai/account).

=== "Bash (REST API)"
    Add the key to your environment variable.
    ```bash
    export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
    ```

    Add the key to your `~/.bashrc`.
    ```bash
    echo "export LAMINI_API_KEY='$LAMINI_API_KEY'" >> ~/.bashrc
    source ~/.bashrc
    echo $LAMINI_API_KEY
    ```

    Run an LLM.
    ```bash
    curl --location "https://api.powerml.co/v2/lamini/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "LaminiTest",
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt_template": "<s>[INST] <<SYS>>\n{input:system}\n<</SYS>>\n\n{input:question} [/INST]",
        "in_value": {
            "system": "You are a helpful assistant.",
            "question": "How are you?"
        },
        "out_type": {
            "Answer": "str"
        }
    }'
    ```

    Expected JSON result with key `Answer` of type `str`:
    > {
        "Answer":"  Hello! *adjusts glasses* I'm feeling quite well, thank you for asking! It's always a pleasure to assist you. How may I be of service today? Is there something specific you need help with?"
    }
    

=== "Python Library"
    Install the Python library.

    ```python
    pip install --upgrade lamini
    ```

    Set your API key.

    ```python
    import lamini
    lamini.api_key = "<YOUR-LAMINI-API-KEY>"
    ```

    Run an LLM.
    ```python
    from lamini import LlamaV2Runner
    
    llm = LlamaV2Runner()
    response = llm("How are you?")
    
    print(response)
    ```

    Expected output:
    > "Hello! I'm just an AI, I don't have feelings or emotions like humans do, but I'm here to help you with any questions or concerns you may have. I'm programmed to provide respectful, safe, and accurate responses, and I will always do my best to help you. Please feel free to ask me anything, and I will do my best to assist you. Is there something specific you would like to know or discuss?"

More details in [Install](install.md).

## Run an LLM