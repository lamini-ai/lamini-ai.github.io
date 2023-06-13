# Getting Started

## Installation

Lamini can be installed using pip, the package manager for Python. To install Lamini, open a command prompt and type:

```sh
pip install lamini
```

This will download and install the latest version of Lamini and its dependencies.

Check if your installation was done correctly, by importing the LLM engine (called `llama`) in your python interpreter. Fun fact: Lamini is the tribe of which llamas are a part, so you can import the module `llama` to work with the LLM engine.

```python
>> from llama import LLMEngine
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
llm = LLMEngine(
    id="example_llm",
    config={"production.key": "<YOUR-KEY-HERE>"}
    )
```

See the [Authentication](/auth) page for more advanced options.

### Basic test

Run the LLM engine with a basic test to see if installation and authentication were set up correctly.

```python
from llama import LLMEngine, Type, Context

class Test(Type):
    test_string: str = Context("just a test")

llm = LLMEngine(id="my_test")

test = Test(test_string="testing 123")
llm(test, output_type=Test)
```

Now you're on your way to using the LLM engine on your specific use case!

To play with different types in an interface, you can log in at [https://lamini.ai](https://lamini.ai) and use the playground there.

## Try an example

-   [Marketing Copy Generation in Google Colab](https://colab.research.google.com/drive/1Ij5xATu0DDtQNimvhzxyP--ttPO-TFES)

-   [Tweet Generation in Google Colab](https://powerml.co/tweet)
