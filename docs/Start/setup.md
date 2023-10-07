# Set up

Looking to host Lamini on prem? Check out [the installer instructions](/Start/installer) 🔗.
## Installation

Lamini can be installed using pip, the package manager for Python. To install Lamini, open a command prompt and type:

```sh
pip install lamini
```

We recommend that you keep up to date with the most recent stable version of lamini which can be found here: [https://pypi.org/project/lamini/](https://pypi.org/project/lamini/). This package is a python wrapper around our REST API.

This will download and install the latest version of Lamini and its dependencies.

Check if your installation was done correctly, by importing the LlamaV2Runner in your python interpreter. Fun fact: Lamini is the tribe of which llamas are a part, so you can import the module `lamini` to work with the LLM engine.

```python
>> from lamini import LlamaV2Runner
```

## Setup your keys

Go to [https://lamini.ai](https://lamini.ai). Log in to get your API key and purchase credits (under the Account tab).

Create `~/.powerml/configure_llama.yaml` and put a key in it.

```sh
production:
    key: "<YOUR-KEY-HERE>"
```

Another option is to pass in your production key to the config parameter of the `LLMEngine` class

```python
model = LlamaV2Runner(
    config={"production.key": "<YOUR-KEY-HERE>", "production.url" : "<YOUR-SERVER-URL-HERE>"}
    )
```

See [the Authentication page](/start/auth) 🔗 for more advanced options.

### Basic test

Run the LLM engine with a basic test to see if installation and authentication were set up correctly.

```python
from lamini import LlamaV2Runner

model = LlamaV2Runner()

answer = model("Tell me a story about llamas.")
print(answer)
```

Now you're on your way to building your own LLM for your specific use case!

To play with different types in an interface, you can log in at [https://lamini.ai](https://lamini.ai) and use the playground there.