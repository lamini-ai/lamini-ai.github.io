# Authentication

Welcome to Lamini's exciting and secure world of authentication!

To access Lamini's services, you'll need an API key, which you can retrieve from your [Lamini account page](https://app.lamini.ai). This API key is your secret, so be sure not to share it with anyone or expose it in any client-side code.

To keep your API key safe, production requests should always be routed through your own backend server, where your API key can be securely loaded from an environment variable or key management service.

Lamini offers several ways to provide your API key:

- [Config file](#config-file)
- [Python API](#python-api)
- [Authorization HTTP header](#authorization-http-header)

### Config file

Ready to configure your Lamini API key? It's easy-peasy! Create a secret config file and put your key in it to get started.

First, navigate to your [Lamini account page](https://app.lamini.ai) to retrieve your unique API key. Remember to keep this key a secret and don't expose it in any client-side code or share it with others.

Next, create a `~/.powerml/configure_llama.yaml` file and place your key in it, like so:

```sh
production:
    key: "<YOUR-KEY-HERE>"
```

The best part? The [Lamini python package](https://pypi.org/project/lamini) will automatically load your key from this config file for you, so you don't have to worry about it.

If you're running Lamini in a docker container, make sure to copy/mount this file inside the container.

Configuring your Lamini API key has never been so easy!

### Python API

Feeling new to coding? Don't worry, we've got you covered with our awesome Python API.

To get started, simply import our API client and initialize it with your API key:

```python
from llama import LLMEngine

llm = LLMEngine(
    model_name="meta-llama/Llama-2-7b-chat-hf",
    config={
        "production": {
            "key": "<YOUR-KEY-HERE>",
        }
    },
)
```

After you've set up, it's time to flex your coding skills by making some epic calls to our API! You'll be a pro in no time!

### Authorization HTTP header

All Lamini REST API requests should include your API key in an Authorization HTTP header as follows:

```
Authorization: Bearer <YOUR-KEY-HERE>
```

### Local mode

If you are hosting your own Lamini servers, you need to point your client at the correct server.

In the config file:

```sh
production:
    key: "<YOUR-KEY-HERE>"
    url: "<YOUR-SERVER-URL-HERE>:<YOUR-SERVER-PORT-HERE>"
```

In the python client:

```python
from llama import LLMEngine

llm = LLMEngine(
    model_name="meta-llama/Llama-2-7b-chat-hf",
    config={
        "production": {
            "key": "<YOUR-KEY-HERE>",
            "url": "<YOUR-SERVER-URL-HERE>:<YOUR-SERVER-PORT-HERE>"
        }
    },
)
```

## Accounts

### Create an account

Yo, listen up! Creating an account with Lamini is easy peasy, lemon squeezy. All you need is a Gmail address to sign in with [Google single sign-on](https://app.lamini.co), and voila! We'll set up an account and token for you in no time.

### Organizations

If you're running a large organization and need to manage multiple users on the same account, you should totally hit us up for an enterprise account. Just [sign up](https://lamini.ai/contact) and we'll get you sorted.

## Google Colab

We got your back when it comes to integrating with Google Colab, no sweat. Say goodbye to storing your API key in a notebook, and say hello to our effortless snippet for automatic login:

```python
# @title Setup: Authenticate with Google & install the open-source [Lamini library](https://pypi.org/project/lamini) to use LLMs easily
%%capture

from google.colab import auth
import requests
import os
import yaml

def authenticate_powerml():
  auth.authenticate_user()
  gcloud_token = !gcloud auth print-access-token
  powerml_token_response = requests.get('https://api.powerml.co/data_studio/auth/verify_gcloud_token?token=' + gcloud_token[0])
  return powerml_token_response.json()['token']

production_token = authenticate_powerml()
!pip install --upgrade --force-reinstall --ignore-installed lamini

keys_dir_path = '/root/.powerml'
os.makedirs(keys_dir_path, exist_ok=True)

keys_file_path = keys_dir_path + '/configure_llama.yaml'
with open(keys_file_path, 'w') as f:
  yaml.dump(config, f, default_flow_style=False)
```

This code snippet stores your API key in the production_token variable and writes it to the config file for you. Easy, right? If you prefer, you can also pass your API key to the LLM object using the Python API.

## Comparison of authentication methods

Authentication methods can be a real head-scratcher, especially if you're new to the game. But fear not, my fellow memers! Lamini has got you covered with three different authentication methods: config file, Python API, and Authorization HTTP header.

### Config file

The config file is perfect for small-scale applications and personal projects, as it's easy to set up and configure. But beware, storing your API key in plain text on your machine is like putting your password on a post-it note. Keep that file to yourself, and don't let anyone else get their grubby little hands on it.

### Python API

If you need flexibility and scalability for large-scale applications, the Python API method is the way to go. You can dynamically set your API key based on your app's requirements, and you can use it with various environments and applications. But still, don't go sharing your key with anyone or commit it to a version control system.

### Authorization HTTP header

The Authorization HTTP header method is for the big boys, the ones with larger-scale apps and stringent security requirements. This method is secure because the API key isn't stored in plain text, but it requires additional implementation effort to set up correctly. Plus, managing and rotating API keys can be a real pain in the butt.

In the end, you'll have to weigh the pros and cons of each method to determine which one is the best fit for your needs. Just remember, always keep your API key safe and secure like a secret meme stash.
