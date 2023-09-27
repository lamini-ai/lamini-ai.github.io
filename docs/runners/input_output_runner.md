# InputOutputRunner

The `InputOutputRunner` class is designed for running and training any input-output model, using structured types (based on Pydantic). It provides methods to interact with the model and manage data loading and training.

## Define your own inputs and outputs, and run the model

```python
from llama import InputOutputRunner

class Input(Type):
    instruction: str = Context("instruction")

class Output(Type):
    response: str = Context("response to instruction")

model = InputOutputRunner(input_type=Input, output_type=Output)
model = model(Input(instruction="Tell me how to add data to Lamini"))
```

## Adding data to the model

There are many ways to add data to the `InputOutputRunner`. The most common way is to `load_data`. This loads data from a list of Input and Output type pairs, e.g. `[[Input, Output], [Input, Output], ...]`

Alternatively, `InputOutputRunner` provides several utility methods which will import similarly formatted data from jsonlines files, csv files, and pandas dataframes. See below for an exhaustive list of methods.

<details>
  <summary>See code examples for loading data</summary>

```python
model.load_data(
    [[
        Input(instruction="What kind of exercise is good for me?", is_question=1),
        Output(response="Running", is_positive=1),
    ]]
)

# `load_data_from_paired_dicts` - Load data from a list of paired dictionaries, e.g. `[{"input": Input, "output": Output}, {"input": Input, "output": Output}, ...]`
model.load_data_from_paired_dicts(
    [
        {
            "input": 
                {
                    "instruction": "What kind of exercise is good for me?",
                    "is_question": 1,
                }, 
            "output": {
                "response": "Running",
                "is_positive": 1,
            },
        },
    ]
)


# `load_data_from_paired_lists` - Load data from a list of paired lists, e.g. `[[input_dict, output_dict], [input_dict, output_dict], ...]`
model.load_data_from_paired_lists(
    [
        [
            {
                "instruction": "What kind of exercise is good for me?",
                "is_question": 1,
            },
            {
                "response": "Running",
                "is_positive": 1,
            },
        ],
        [
            {
                "instruction": "What kind of exercise is good for me?",
                "is_question": 1,
            },
            {
                "response": "Running",
                "is_positive": 1,
            },
        ],
    ]
)

# DataFrame with "input-" and "output-" prefix columns, matching the types above
# `load_data_from_dataframe` - Load data from a pandas DataFrame, with `input-` and `output-` prefix columns, e.g. `["input-instruction", "input-is_question", "output-response", "output-is_positive"]`
df = pd.DataFrrom_dataframe(df, verbose=True)

# Two separate dataframes, one for input and one for output
# `load_data_from_paired_dataframes` - Load data from a list of paired DataFrames, e.g. input_df and output_df
input_df = pd.DataFrame([
    {
        "instruction": "What kind of exercise is good for me?",
        "is_question": 1,
    },
    {
        "instruction": "What kind of exercise is good for me?",
        "is_question": 1,
    },
], columns=["instruction", "is_question"])
output_df = pd.DataFrame([
    {
        "response": "Running",
        "is_positive": 1,
    },
    {
        "response": "Running",
        "is_positive": 1,
    },
], columns=["response", "is_positive"])
model.load_data_from_paired_dataframes(input_df, output_df, verbose=True)

# Test loading data from a jsonlines file, two formats
# `load_data_from_jsonlines` - Load data from a jsonlines file, with `input-` and `output-` prefix keys, e.g. `{"input-instruction": "What kind of exercise is good for me?", "input-is_question": 1, "output-response": "Running", "output-is_positive": 1}`
model.load_data_from_jsonlines("tests/input_output_runner_data_flattened.jsonl", verbose=True)
model.load_data_from_jsonlines("tests/input_output_runner_data.jsonl", verbose=True)

# Other ways:

# `load_data_from_paired_jsonlines` - Load data from two jsonlines files, e.g. `input_file_path` and `output_file_path`

# `load_data_from_csv` - Load data from a csv file, with "input-" and "output-" prefix columns, e.g. `["input-instruction", "input-is_question", "output-response", "output-is_positive"]`

# `load_data_from_paired_csvs` - Load data from two csv files, e.g. `input_file_path` and `output_file_path`
```
</details>

## Training the Model

After you've added data, you can now train a model. Once the training is complete, you can view the eval results.
Training is done on Lamini servers and you can track the training job's progress at [https://app.lamini.ai/train](https://app.lamini.ai/train).

```python
model.train()
```

Optional Step: If you want to change the default values of the hyper-parameters of the model (like learning rate), you can pass the hyper-parameters you want to modify using the following code

```python
model.train(finetune_args={'learning_rate': 1.0e-4})
```
The default values of the hyper-parameters and key values can be found in the llama_config.yaml file in the configs folder in LLAMA. Currently we support most hyper-parameters in [huggingface's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments), like max_steps, batch_size, num_train_epochs, early_stopping etc. 

Once a model is trained you can check the eval results to see before and after comparisons of the base model and the trained model.

```
model.evaluate()
```

 You can also query the new trained model like so:

```python
new_input = Input(instruction="What kind of exercise is superduper for me?", is_question=1)
output = model(new_input)
print(output)
```

## Class Definition

```python
class InputOutputRunner:
    """A class for running and training any generic input-output model"""

    def __init__(self, input_type: Type, output_type: Type, model_name: str = "EleutherAI/pythia-410m-deduped"):
        """
        Initializes a new instance of the InputOutputRunner.

        Args:
            input_type (Type): The type of the input to the model.
            output_type (Type): The type of the output from the model.
            model_name (str): The name of the input-output model to use. Default is "EleutherAI/pythia-410m-deduped".
        """
```

### Methods Reference

#### `__call__(self, inputs: Union[Type, List[Type]]) -> Union[Type', List[Type']]`

Get the output to a single input, or list of inputs.

Args:

- `inputs` (str): The input(s) to go into the model for an output(s).

Returns:

- `output(s)` (str): The corresponding output(s) to the input(s).


#### `load_data(self, data)`

Load a list of Input, Output pairs.

Args:

- `data` (List[Type, Type`]): A list of Input/Output Types.
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.

#### `load_data_from_jsonlines(self, file_path: str)`

Load a jsonlines file with each line:
- a json object of the form {"input": input_dict, "output": output_dict}
- or, flattened json object with input- and output- prefixes, e.g. `{"input-key1": input_value1, "input-key2": input_value2, "output-key1": output_value1, "output-key2": output_value2}`

Args:

- `file_path` (str): The path to the jsonlines file.
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.


#### `load_data_from_dataframe(self, df: pd.DataFrame)`

Load a pandas DataFrame with "input-" and "output-" prefix columns, matching the types above.

Args:

- `df` (pd.DataFrame): The pandas DataFrame
- `input_prefix` (str): The prefix for the input columns. Default is "input-".
- `output_prefix` (str): The prefix for the output columns. Default is "output-".
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.


#### `load_data_from_csv(self, file_path: str)`

Load a CSV file with "input-" and "output-" prefix columns, matching the types above.

Args:

- `file_path` (str): The path to the CSV file.
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.

#### `load_data_from_paired_dataframes(self, input_df: pd.DataFrame, output_df: pd.DataFrame)`

Load two separate dataframes, one for input and one for output.

Args:

- `input_df` (pd.DataFrame): The pandas DataFrame for input.
- `output_df` (pd.DataFrame): The pandas DataFrame for output.
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.

#### `load_data_from_paired_jsonlines(self, input_file_path: str, output_file_path: str)`

Load two separate jsonlines files, one for input and one for output.

Args:

- `input_file_path` (str): The path to the jsonlines file for input.
- `output_file_path` (str): The path to the jsonlines file for output.
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.

#### `load_data_from_paired_csvs(self, input_file_path: str, output_file_path: str)`

Load two separate CSV files, one for input and one for output.

Args:

- `input_file_path` (str): The path to the CSV file for input.
- `output_file_path` (str): The path to the CSV file for output.
- `verbose` (bool): Whether to print sample training datapoint and how much data was processed correctly and loaded into the model. Default is False.


#### `clear_data(self)`

Clear the data from the input-output model, including loaded documents and input-output pairs.

#### `train(self, verbose: bool = False)`

Train the input-output model on the loaded data. This function blocks until training is complete.

Args:

- `verbose` (bool): Whether to print verbose training progress. Default is False.

#### `evaluate(self) -> dict

Get the evaluation results of the trained input-output model.

Returns:

- `evaluation` (List): A dict of evaluation results.

Also, sets the `self.evaluation` attribute to the evaluation results.

Please note that this documentation assumes the presence of relevant imports (e.g., `List`, `str`, `pd`) and required external dependencies like the `LLMEngine` class and other libraries.
