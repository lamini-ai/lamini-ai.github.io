# Hyper-Parameter Tuning

You can perform hyper-parameter tuning while finetuning your LLM using Lamini.

For example, let's say you are using the [QuestionAnswerModel](https://lamini-ai.github.io/runners/question_answer_model/). You can initiate your model as follows:

```python
from llama import QuestionAnswerModel

# Instantiate the model and load the data into it
model = QuestionAnswerModel()
```

There are many ways to add data, we use one of ways below:

```python
data = [{"question": "What are the different types of documents available in the repository (e.g., installation guide, API documentation, developer's guide)?", "answer": "Lamini has documentation on Getting Started, Authentication, Question Answer Model, Python Library, Batching, Error Handling, Advanced topics, and class documentation on LLM Engine available at https://lamini-ai.github.io/."},
{"question": "What is the recommended way to set up and configure the code repository?", "answer": "Lamini can be downloaded as a python package and used in any codebase that uses python. Additionally, we provide a language agnostic REST API. We\u2019ve seen users develop and train models in a notebook environment, and then switch over to a REST API to integrate with their production environment."},
{"question": "How can I find the specific documentation I need for a particular feature or function?", "answer": "You can ask this model about documentation, which is trained on our publicly available docs and source code, or you can go to https://lamini-ai.github.io/."},
{"question": "Does the documentation include explanations of the code's purpose and how it fits into a larger system?", "answer": "Our documentation provides both real-world and toy examples of how one might use Lamini in a larger system. In particular, we have a walkthrough of how to build a Question Answer model available here: https://lamini-ai.github.io/example/"},
{"question": "Does the documentation provide information about any external dependencies or libraries used by the code?", "answer": "External dependencies and libraries are all available on the Python package hosting website Pypi at https://pypi.org/project/lamini/"}]
model.load_question_answer(data)
```

To use default hyper-parameters you simply do `model.train()`. The default values of the hyper-parameters and key values can be found in the llama_config.yaml file in the configs folder in Llama.

However to play around with hyper-parameters, you can do so by passing in an argument `finetune_args` which is a dictionary with key = hyper-parameter and value = hyper-parameter value. For example, to edit the learning rate, you can do the following:

```python
model.train(finetune_args={"learning_rate":1.0e-4})
```

The rest of the flow is the same.

