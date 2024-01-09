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

    As a test, run the following command. This calls Llama 2 and returns structured JSON:

    ```bash
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nWhat is the hottest day of the year? [/INST]"
    }'
    ```

    Great, you've run your first Lamini API call!

    Here is a sample response:
    ```json
    {
        "output": "The hottest day of the year is July 21st, according to NASA "
    }
    ```

    Now you're ready to start building your own LLMs, which includes heavier batch calls and training LLMs to learn more complex domains and tasks from your data.

=== "Run with Python SDK"

    Install the latest version of [`lamini`](https://pypi.org/project/lamini/).

    ```sh
    pip install --upgrade lamini
    ```

    Note: if you run into issues, try to include the [latest version number](https://pypi.org/project/lamini/), see an example below. Please share your environment info with us at [info@lamini.ai](mailto:info@lamini.ai), so we can help debug.

    ```sh
    pip install lamini==2.0.5
    ```

    This is a python wrapper around our REST API. It also includes many high-level classes and functions to make it easier to work with LLMs.

    As a test, run the following command. This calls Llama 2 and returns a string:

    ```python
    import lamini

    lamini.api_key = "<YOUR-LAMINI-API-KEY>"
    ```

    As a test, run the LLM:
    ```python
    from lamini import LlamaV2Runner

    llm_runner = LlamaV2Runner()
    response = llm_runner.call("Tell me a story about llamas.")

    print(response)
    ```

## (Optional) Advanced Python setups

#### Advanced Python setup: notebook

You have several other options to authenticate, if the above methods don't work for you.

If you're in a iPython notebook, you can pass in your Lamini API key to any Python model class, e.g. `LLMEngine` or `LlamaV2Runner`, as shown below:

```python
from lamini import LlamaV2Runner

config = { "production.key": "<YOUR-LAMINI-API-KEY>"}
llm_runner = LlamaV2Runner(config=config)
response = llm_runner.call("Tell me a story about llamas.")

print(response)
```

You can also create a file at `~/.powerml/configure_llama.yaml` with your Lamini API key in it:

```sh
production:
    key: "<YOUR-LAMINI-API-KEY>"
```

This will be implicitly read for any Python model class, e.g. `LLMEngine` or `LlamaV2Runner`, without needing to pass in the `config` variable. As a test:

```python
from lamini import LlamaV2Runner

llm_runner = LlamaV2Runner()
response = llm_runner.call("Tell me a story about llamas.")

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
    llm_runner = LlamaV2Runner(config=config)
    response = llm_runner.call("Tell me a story about llamas.")

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

keys_dir_path = '/root/.powerml'
os.makedirs(keys_dir_path, exist_ok=True)

keys_file_path = keys_dir_path + '/configure_llama.yaml'
with open(keys_file_path, 'w') as f:
yaml.dump(config, f, default_flow_style=False)
```

As a test, run this LLM call in a subsequent cell:

```python
from lamini import LlamaV2Runner

llm_runner = LlamaV2Runner()
response = llm_runner.call("Tell me a story about llamas.")

print(response)
```
