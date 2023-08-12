# LlamaV2Runner

The `LlamaV2Runner` class is designed for running and training a Llama V2 model, using system and user prompts.

To see example usage check out the [Llama V2 walkthrough](Examples/llama_v2_example.md)


## Class Definition

```python
class LlamaV2Runner:
    """A class for running and training a Llama V2 model, using system and user prompts"""

    def __init__(
        self,
        model_name: str = "meta-llama/Llama-2-7b-chat-hf",
        default_system_prompt: str = DEFAULT_SYSTEM_PROMPT,
        enable_peft: bool=False,
        config: dict={},
    ):
        """
        Args:
            model_name (str): The name of the model to use. Default is "meta-llama/Llama-2-7b-chat-hf"
            default_system_prompt (str): a default value for the system prompt. 
            enable_peft (bool): Train models using PEFT (Parameter Efficient Fine Tuning)
            config (dict)
        """
        
```
### Methods Reference

#### `__call__(self, inputs: Union[str, List[str]]) -> Union[str, List[str]]`

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


    