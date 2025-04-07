# Validators

Validators are components that take in a prompt and output a structured response to flag whether the output of a generator is valid or not. Validators are used to validate the output of a generator. For example, you can use a factual validator to ensure that the output of a generator is factually correct with respect to a provided text.

```python
from lamini.experiment.validators import FactualityValidator

# Create validator
factual_validator = FactualityValidator(
    name="factual_validator",
    instruction="Validate if the following concept is factually accurate: {concept}",
    model="meta-llama/Llama-3.1-8B-Instruct",
)

# Update pipeline
pipeline = BaseAgenticPipeline(
    generators={"concept": concept_generator},
    validators={"factual": factual_validator},
    order=["concept", "factual"],
    record_dir="./experiment_results"
)
```

If you want to customize a validator, you can do so by subclassing `BaseValidator` and implementing the required initialization parameters:

```python
from lamini.experiment.validators import BaseValidator

class CustomValidator(BaseValidator):
    def __init__(self):
        super().__init__(
            name="custom_validator",
            instruction="Your validation instruction here: {input}",
            is_valid_field="is_valid"  # Optional: specify custom validation field name
        )
    
    def validate(self, prompt: PromptObject) -> PromptObject:
        # Custom validation logic here
        return prompt
```

Validators are different from generators in that they must include a boolean validation field in their output. This is enforced by the `BaseValidator` class, which can handle the validation field in three ways:

1. Using the default `is_valid` field if no custom output type is specified
2. Using a custom validation field name specified by `is_valid_field`
3. Including a boolean field in a custom `output_type` dictionary

For example:

```python
# Default validation field
validator = CustomValidator(
    name="validator",
    instruction="Validate this: {input}"
)  # Uses "is_valid" field

# Custom validation field name
validator = CustomValidator(
    name="validator",
    instruction="Validate this: {input}",
    is_valid_field="passed_validation"
)

# Custom output type with validation field
validator = CustomValidator(
    name="validator",
    instruction="Validate this: {input}",
    is_valid_field="is_valid",
    output_type={
        "is_valid": "bool",
        "confidence": "float",
        "reason": "str"
    }
)
```

## Available Validators

| Validator | Description |
|-----------|-------------|
| `FactualityValidator` | Validates whether generated content is factually accurate with respect to provided reference text |
| `SQLValidator` | Validates SQL query syntax and structure |
| `SQLScoreValidator` | Validates SQL queries by comparing their execution results |
| `BaseSQLValidator` | Base class for SQL-related validators |
| `BaseValidator` | Base class for creating custom validators |

## Best Practices

1. **Start with as few validators as possible.**
For example, just 1 FactualityValidator, or 1 SQLValidator and 1 SQLScoreValidator. Run the pipeline and check the generated data, identify issues.
2. **Iterate by modifying the prompt or validators**
These pre-built validators give you a framework and a gooding starting point. However, it is very likely that you will need to modify each validator to make it work for your use case and specific data. You can experiment with modifying the prompts, decoupling a big validator into small ones, adding more validators, and so on.
3. **Test run validators**
Make sure you run tests and validate that each validator is validating correctly! You may want to iterate on the prompt and model used for the validator (anything else?)
