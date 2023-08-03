# BasicModelRunner

The `BasicModelRunner` class is designed for running and training a basic model without any prompt templates or frills. It provides methods to interact with the model and manage data loading and training.

## Run the model

```python
from llama import BasicModelRunner

# Run the base model
model = BasicModelRunner()
output = model("How can I add data to Lamini?")
```

## Adding data to a model

There are many ways to add data to the `BasicModelRunner`.

The easiest way is just through dictionaries of input-output pairs, using the method `load_data`:

```python
model.load_data(data)
```

where `data` here is:
```python
data = [
    {
        "input": "What are the different types of documents available in the repository (e.g., installation guide, API documentation, developer's guide)?", 
        "output": "Lamini has documentation on Getting Started, Authentication, Question Answer Model, Python Library, Batching, Error Handling, Advanced topics, and class documentation on LLM Engine available at https://lamini-ai.github.io/."
    },
    {
        "input": "What is the recommended way to set up and configure the code repository?", 
        "output": "Lamini can be downloaded as a python package and used in any codebase that uses python. Additionally, we provide a language agnostic REST API. We\u2019ve seen users develop and train models in a notebook environment, and then switch over to a REST API to integrate with their production environment."
    }
]
```

Alternatively, `BasicModelRunner` provides several utility methods which will import similarly formatted data from jsonlines files, csv files, and pandas dataframes. See below for an exhaustive list of methods.

## Training the model

After you've added data, you can now train a model. Once the training is complete, you can view the eval results.
Training is done on Lamini servers and you can track the training job's progress at [https://app.lamini.ai/train](https://app.lamini.ai/train)

```python
model.train()
model.evaluate()
```

Once a model is trained you can check the eval results to see before and after comparisons of the base model and the trained model. You can also query the new trained model like so

```python
output = model("How can I add data to Lamini?")
print(output)
```

## Class Definition

```python
class BasicModelRunner:
    """A class for running and training a basic model"""

    def __init__(self, model_name: str = "EleutherAI/pythia-410m-deduped"):
        """
        Initializes a new instance of the BasicModelRunner.

        Args:
            model_name (str): The name of the model to use. Default is "EleutherAI/pythia-410m-deduped".
        """
```

### Methods Reference

#### `__call__(self, input: Union[str, List[str]]) -> Union[str', List[str']]`

Get the output to a single input or list of inputs (batched).

Args:

- `input` (str): The input to the model.

Returns:

- `output` (str): The output of the model.

#### `load_data(self, data)`

Load a list of dictionaries with input-output pairs into the model. Each dictionary must have "input" and "output" as keys.

Args:

- `data` (List[dict]): A list of dictionaries representing input-output pairs.

#### `load_data_from_jsonlines(self, file_path: str)`

Load a jsonlines file with input-output pairs into the model. Each line in the file must be a JSON object with "input" and "output" as keys.

Args:

- `file_path` (str): The path to the jsonlines file.

#### `load_data_from_dataframe(self, df: pd.DataFrame)`

Load a pandas DataFrame with input-output pairs into the model. Each row must have "input" and "output" as keys.

Args:

- `df` (pd.DataFrame): The pandas DataFrame containing the input-output pairs.

#### `load_data_from_csv(self, file_path: str)`

Load a CSV file with input-output pairs into the model. Each row must have "input" and "output" as keys.

Args:

- `file_path` (str): The path to the CSV file.

#### `clear_data(self)`

Clear the data from the model, including loaded documents and input-output pairs.

#### `train(self, verbose: bool = False)`

Train the model on the loaded data. This function blocks until training is complete.

Args:

- `verbose` (bool): Whether to print verbose training progress. Default is False.

#### `evaluate(self) -> dict

Get the evaluation results of the trained model.

Returns:

- `evaluation` (List): A dict of evaluation results.

Also, sets the `self.evaluation` attribute to the evaluation results.

Please note that this documentation assumes the presence of relevant imports (e.g., `List`, `str`, `pd`) and required external dependencies like the `LLMEngine` class and other libraries.
