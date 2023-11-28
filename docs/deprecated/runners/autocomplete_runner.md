# AutocompleteRunner

The `AutocompleteRunner` class is designed for running and training a Llama V2 model, using system and user prompts.

### Methods Reference

#### `__call__(self, inputs: Union[str, List[str]]) -> Union[str, List[str]]`

Get the output to a single input or list of inputs (batched).

Args:

- `input` (str): The input to the model.

Returns:

- `output` (str): The output of the model.

#### `evaluate_autocomplete(self, data: Union[str, List[str]]) -> Union[str, List[str]](self, data)`

Return dictionary of paired prompts, targets, and predictions

Args:

- `data` (List[dict]): A list of dictionaries representing input-output pairs.

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
- (Optional) `finetune_args` (dict): key=hyper-parameter name, value=parameter value. Same as [huggingface's training arguments](https://huggingface.co/docs/transformers/v4.33.3/en/main_classes/trainer#transformers.TrainingArguments)

#### `evaluate(self)` -> dict

Get the evaluation results of the trained model.

Returns:

- `evaluation` (List): A dict of evaluation results.

Also, sets the `self.evaluation` attribute to the evaluation results.

Please note that this documentation assumes the presence of relevant imports (e.g., `List`, `str`, `pd`) and required external dependencies like the `LLMEngine` class and other libraries.


    