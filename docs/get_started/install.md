# Install

Welcome to this easy 2-step install. Estimated time: 2 minutes.

If you want to host Lamini in your VPC or on prem, check out [enterprise installer instructions](/enterprise_install) 🔗.

## 1. Get your Lamini API key 🔑
Your API key is at [https://app.lamini.ai/account](https://app.lamini.ai/account). If it's your first time, create a free account by logging in.


Add your key to your environment variables. In your terminal, run:
```bash
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

Put this line in your `~/.bash_profile` or equivalent file, so you don't have to rerun it in a new session. Remember to `source ~/.bash_profile` after you make the change.

```bash
echo "export LAMINI_API_KEY='$LAMINI_API_KEY'" >> ~/.bash_profile
source ~/.bash_profile
echo $LAMINI_API_KEY
```

## 2. Run an LLM 🦙

Run an LLM with our REST API or Python SDK.

=== "Run with REST API"

    As a test, run the following command. This makes a batch call to Llama 2 and returns structured JSON:

    ```bash
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": ["What is the hottest day of the year?", "What is for lunch?"],
        "out_type": {
            "answer": "str"
        }
    }'
    ```

    Great, you've run your first Lamini API call!

    Here is a sample response, with structured JSON schema output:
    ```json
    [
        {
            "answer": "The hottest day of the year is usually around July 21st or 22nd in the Northern Hemisphere, and January 20th or 21st in the Southern Hemisphere"
        },{
            "answer": "Sandwiches"
        }
    ]
    ```

    Now you're ready to start building your own LLMs, which includes heavier batch calls and training LLMs to learn more complex domains and tasks from your data.

=== "Run with Python SDK"
    Install the latest version of [`lamini`](https://pypi.org/project/lamini/).

    ```sh
    pip install --upgrade lamini
    ```

    This is a python wrapper around our REST API. It also includes many high-level classes and functions to make it easier to work with LLMs.

    ```python
    import lamini

    lamini.api_key = "<YOUR-LAMINI-API-KEY>"
    ```

    As a test, run the LLM and call Llama 2:
    ```python
    from lamini import LlamaV2Runner

    llm = LlamaV2Runner()
    response = llm("Tell me a story about llamas.")

    print(response)
    ```

    ## (Optional) Advanced Python setups

    #### Advanced Python setup: notebook
    You have several other options to authenticate if the above methods do not work for you.

    If you're in an iPython notebook, you can pass in your Lamini API key to any Python model class, e.g. `LLMEngine` or `LlamaV2Runner`, as shown below:

    ```python
    from lamini import LlamaV2Runner

    config = { "production.key": "<YOUR-LAMINI-API-KEY>"}
    llm = LlamaV2Runner(config=config)
    response = llm("Tell me a story about llamas.")

    print(response)
    ```

    You can also create a file at `~/.lamini/configure.yaml` with your Lamini API key in it:

    ```sh
    production:
        key: "<YOUR-LAMINI-API-KEY>"
    ```

    This will be implicitly read for any Python model class, e.g. `LLMEngine` or `LlamaV2Runner`, without needing to pass in the `config` variable. As a test:

    ```python
    from lamini import LlamaV2Runner

    llm = LlamaV2Runner()
    response = llm("Tell me a story about llamas.")

    print(response)
    ```

    #### Advanced Python setup: VPC or on premise

    If you are [running Lamini in your VPC or on prem](/enterprise_install/installer.md), you can change the URL from Lamini's hosted service to your own server URL:

    === "Python script"

        ```python
        config = {
            "production.key": "<YOUR-LAMINI-API-KEY>",
            "production.url" : "<YOUR-SERVER-URL-HERE>"
        }
        ```

        Test that it works:
        ```python
        llm = LlamaV2Runner(config=config)
        response = llm("Tell me a story about llamas.")

        print(response)
        ```

    === "In `~/.powerml/configure_llama.yaml`"
        Add the extra `url` field:

        ```sh
        production:
            key: "<YOUR-LAMINI-API-KEY>"
            url: "<YOUR-SERVER-URL-HERE>"
        ```

    #### Advanced Python setup: Google Colab

    Here's a code snippet to paste in Google Colab that automatically authenticates for you via Google by placing your Lamini API key into the yaml file, as above:

    ```python
    # @title Setup: Authenticate with Google & install the open-source [Lamini library](https://pypi.org/project/lamini) to use LLMs easily
    %%capture

    from google.colab import auth
    import requests
    import os
    import yaml

    def authenticate_lamini():
    auth.authenticate_user()
    gcloud_token = !gcloud auth print-access-token
    lamini_token_response = requests.get('https://api.powerml.co/data_studio/auth/verify_gcloud_token?token=' + gcloud_token[0])
    return lamini_token_response.json()['token']

    production_token = authenticate_lamini()
    !pip install --upgrade lamini

    keys_dir_path = '/root/.lamini'
    os.makedirs(keys_dir_path, exist_ok=True)

    keys_file_path = keys_dir_path + '/configure.yaml'
    with open(keys_file_path, 'w') as f:
    yaml.dump(config, f, default_flow_style=False)
    ```

    As a test, run this LLM call in a subsequent cell:
    ```python
    from lamini import LlamaV2Runner

    llm = LlamaV2Runner()
    response = llm("Tell me a story about llamas.")

    print(response)
    ```
