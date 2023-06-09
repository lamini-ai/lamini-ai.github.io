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

## QuestionAnswerModel

The `QuestionAnswerModel` class is designed for running and training a question answering model. It provides methods to interact with the model and manage data loading and training.

### Ask the Model a Question

```python
from llama import QuestionAnswerModel

# Run the base model
model = QuestionAnswerModel()
model = model.get_answer("How can I add data to Lamini?")
```

### Adding Data to a Model

There are many ways to add data to the QuestionAnswerModel.

You can import data to this class by using the `load_question_answer` method, which accepts a list of python dictionaries as input. Each dictionary must have `"question"` and `"answer"` keys, and string values for each of those keys. This data is similar to "prompt" and "completion" data you may have seen before. For example,

```python
from llama import QuestionAnswerModel

data = [{"question": "What are the different types of documents available in the repository (e.g., installation guide, API documentation, developer's guide)?", "answer": "Lamini has documentation on Getting Started, Authentication, Question Answer Model, Python Library, Batching, Error Handling, Advanced topics, and class documentation on LLM Engine available at https://lamini-ai.github.io/."},
{"question": "What is the recommended way to set up and configure the code repository?", "answer": "Lamini can be downloaded as a python package and used in any codebase that uses python. Additionally, we provide a language agnostic REST API. We\u2019ve seen users develop and train models in a notebook environment, and then switch over to a REST API to integrate with their production environment."},
{"question": "How can I find the specific documentation I need for a particular feature or function?", "answer": "You can ask this model about documentation, which is trained on our publicly available docs and source code, or you can go to https://lamini-ai.github.io/."},
{"question": "Does the documentation include explanations of the code's purpose and how it fits into a larger system?", "answer": "Our documentation provides both real-world and toy examples of how one might use Lamini in a larger system. In particular, we have a walkthrough of how to build a Question Answer model available here: https://lamini-ai.github.io/example/"},
{"question": "Does the documentation provide information about any external dependencies or libraries used by the code?", "answer": "External dependencies and libraries are all available on the Python package hosting website Pypi at https://pypi.org/project/lamini/"}]
# Instantiate the model and load the data into it
model = QuestionAnswerModel()
model.load_question_answer(data)
```

Alternatively, QuestionAnswerModel provides several utility methods which will import similarly formatted data from jsonlines files, csv files, and pandas dataframes.

### Training the Model

After you've added data, you can now train a model. Once the training is complete, you can view the eval results.
Training is done on Lamini servers and you can track the training job's progress at [https://app.lamini.ai/train](https://app.lamini.ai/train)

```python
model.train()
results = model.get_eval_results()
print(results)
```

Once a model is trained you can check the eval results to see before and after comparisons of the base model and the trained model. You can also query the new trained model like so

```python
answer = model.get_answer("How can I add data to Lamini?")
print(answer)
```

## Try an example

- Colab Link: [Lamini: Finetuning For Free](https://colab.research.google.com/drive/1QMeGzR9FnhNJJFmcHtm9RhFP3vrwIkFn?usp=sharing)
