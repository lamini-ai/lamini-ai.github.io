# Getting Started

## Installation

Llama can be installed using pip, the package manager for Python. To install Llama, open a command prompt and type:

```sh
pip install llama-llm
```

This will download and install the latest version of Llama and its dependencies.

Check if your installation was done correctly, by importing the LLM engine in your python interpreter.

```python
>> from llama import LLM
```

## Setup your keys

Go to [https://lamini.ai](https://lamini.ai).  Log in to get your API key and purchase credits.

Create `~/.powerml/configure_llama.yaml` and put a key in it.

```sh
production:
    key: "<YOUR-KEY-HERE>"
```

See the [Authentication](/auth) page for more advanced options.

### Basic test

Run the LLM engine with a basic test to see if installation and authentication were set up correctly.

```python
from llama import LLM, Type, Context

class Test(Type):
    test_string: str = Context("just a test")

llm = LLM(name="my_test")

test = Test(test_string="testing 123")
llm(test, output_type=Test)
```

Now you're on your way to using the LLM engine on your specific use case!

## Try an example

- [Marketing Copy Generation in Google Colab](https://colab.research.google.com/drive/1Ij5xATu0DDtQNimvhzxyP--ttPO-TFES)

- [Tweet Generation in Google Colab](https://powerml.co/tweet)

