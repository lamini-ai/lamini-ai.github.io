# QuestionAnswerModel

The `QuestionAnswerModel` class is designed for running and training a question answering model. It provides methods to interact with the model and manage data loading and training.

## Ask the Model a Question

```python
from llama import QuestionAnswerModel

# Run the base model
model = QuestionAnswerModel()
model = model.get_answer("How can I add data to Lamini?")
```

## Adding Data to a Model

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

## Training the Model

After you've added data, you can now train a model. Once the training is complete, you can view the eval results.
Training is done on Lamini servers and you can track the training job's progress at [https://app.lamini.ai/train](https://app.lamini.ai/train)

```python
model.train()
results = model.evaluate()
print(results)
```

Optional Step: If you want to change the default values of the hyper-parameters of the model (like learning rate), you can pass the hyper-parameters you want to modify using the following code

```python
model.train(finetune_args={'learning_rate': 1.0e-4})
```
The default values of the hyper-parameters and key values can be found in the llama_config.yaml file in the configs folder in LLAMA. Currently we support most hyper-parameters in [huggingface's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc. 


Once a model is trained you can check the eval results to see before and after comparisons of the base model and the trained model. You can also query the new trained model like so

```python
answer = model.get_answer("How can I add data to Lamini?")
print(answer)
```

## Class Definition

```python
class QuestionAnswerModel:
    """A class for running and training a question answering model"""

    def __init__(self, model_name: str = "EleutherAI/pythia-410m-deduped"):
        """
        Initializes a new instance of the QuestionAnswerModel.

        Args:
            model_name (str): The name of the question answering model to use. Default is "EleutherAI/pythia-410m-deduped".
        """
```

### Methods Reference

#### `get_answer(self, question: str) -> str`

Get the answer to a single question.

Args:

- `question` (str): The question to be answered.

Returns:

- `answer` (str): The answer to the question.

#### `get_answers(self, questions: List[str]) -> List[str]`

Get answers to a batch of questions.

Args:

- `questions` (List[str]): A list of questions.

Returns:

- `answers` (List[str]): A list of answers corresponding to the input questions. The order of answers matches the order of questions.

#### `load_question_answer(self, data)`

Load a list of JSON objects with question-answer pairs into the question answering model. Each object must have "question" and "answer" as keys.

Args:

- `data` (List[dict]): A list of dictionaries representing question-answer pairs.

#### `load_question_answer_from_jsonlines(self, file_path: str)`

Load a jsonlines file with question-answer pairs into the question answering model. Each line in the file must be a JSON object with "question" and "answer" as keys.

Args:

- `file_path` (str): The path to the jsonlines file.

#### `load_question_from_dataframe(self, df: pd.DataFrame)`

Load a pandas DataFrame with question-answer pairs into the question answering model. Each row must have "question" and "answer" as keys.

Args:

- `df` (pd.DataFrame): The pandas DataFrame containing the question-answer pairs.

#### `load_question_answer_from_csv(self, file_path: str)`

Load a CSV file with question-answer pairs into the question answering model. Each row must have "question" and "answer" as keys.

Args:

- `file_path` (str): The path to the CSV file.

#### `clear_data(self)`

Clear the data from the question answering model, including loaded documents and question-answer pairs.

#### `train(self, verbose: bool = False)`

Train the question answering model on the loaded data. This function blocks until training is complete.

Args:

- `verbose` (bool): Whether to print verbose training progress. Default is False.

#### `evaluate(self) -> dict

Get the evaluation results of the trained question answering model.

Returns:

- `evaluation` (List): A dict of evaluation results.

Also, sets the `self.evaluation` attribute to the evaluation results.

Please note that this documentation assumes the presence of relevant imports (e.g., `List`, `str`, `pd`) and required external dependencies like the `LLMEngine` class and other libraries.
