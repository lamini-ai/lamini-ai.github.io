# Agentic Pipeline

## Table of Contents
* [Quick Start](#quick-start)
* [Pipeline Components](#pipeline-components)
    * [Generators and Validators](#generators-and-validators)
    * [Pipeline Steps](#pipeline-steps)
    * [Result Recording](#result-recording)
* [Pipeline Validation](#pipeline-validation)
    * [Step Logic Validation](#step-logic-validation)
    * [Pipeline Spotcheck](#pipeline-spotcheck)
* [Batch Processing](#batch-processing)
* [Serialization](#serialization)

The Agentic Pipeline orchestrates a sequence of LLM generators and validators, managing data flow between components and recording execution results. It currently supports single-item with batch processing coming in future releases. Further, the pipeline supports automatic result recording and pipeline validation capabilities.

## Quick Start

First, ensure your API key is set up as described in the [Getting Started](index.md) guide.

=== "Python SDK"

    Create a basic pipeline with a generator:

    ```python
    from lamini.experiment.generators import BaseGenerator
    from lamini.experiment.pipeline import BaseAgenticPipeline
    from lamini.experiment.base_experiment_object import ExperimentObject

    # Create a custom generator
    class QuestionGenerator(BaseGenerator):
        def __init__(self, model, name):
            super().__init__(
                name=name,
                model=model,
                instruction="Generate an interesting question based on this fact: {text}\nMake sure the question requires understanding of the fact to answer correctly.",
                output_type={"question": "str"}  # Changed to output a question
            )
        

    # Initialize generator with required parameters
    generator = QuestionGenerator(
        model="meta-llama/Llama-3.1-8B-Instruct",
        name="question_generator"
    )

    # Create pipeline
    pipeline = BaseAgenticPipeline(
        generators={"process": generator},
        record_dir="./pipeline_results"
    )

    # Execute pipeline
    experiment_obj = ExperimentObject(
        data={"text": "Hello world"}
    )
    results = pipeline(experiment_obj)
    ```

## Pipeline Components

### Generators and Validators

The pipeline supports both generators and validators. Generators require:

- A name
- An instruction template with metadata keys in curly braces
- An output type specification (either a Pydantic model or dictionary)
- Optional role prefix for the prompt
- Optional pre/post processing methods

```python
from lamini.experiment.validators import BaseValidator

# Create a validator
class LengthValidator(BaseValidator):
    def __init__(self):
        super().__init__(
            name="length_validator",
            instruction="Validate text length: {processed_text}",
            output_type={"is_valid": "bool"}
        )
    
    def postprocess(self, prompt_obj):
        # Add validation logic
        text = prompt_obj.data["processed_text"]
        prompt_obj.response = {"is_valid": len(text) > 10}
        return prompt_obj

# Create pipeline with both generator and validator
pipeline = BaseAgenticPipeline(
    generators={"process": generator},
    validators={"length_check": LengthValidator()},
    order=["process", "length_check"],  # Specify execution order
    record_dir="./pipeline_results"
)
```

### Pipeline Steps

Each component in the pipeline is wrapped in a PipelineStep, which manages:

- The worker (generator or validator)
- Queue of items to process
- Connection to the next step

### Result Recording

The pipeline automatically records results in the specified `record_dir`:

```python
pipeline = BaseAgenticPipeline(
    generators={"process": generator},
    record_dir="./experiment_results",
    record_step=True,  # Record intermediate results
    record_results=True  # Record final results
)
```

Results are saved in JSON Lines format:

- `{step_name}_full.jsonl`: Complete data including prompts and responses
- `{step_name}_data_io.jsonl`: Input/output data for each step
- `{step_name}_prompt_response.jsonl`: Prompt-response pairs
- `data_io.jsonl`: Final aggregated input/output data

## Pipeline Validation

The pipeline includes built-in validation mechanisms. These mechanisms are run automatically before the pipeline is run through the entire set of prompts provided. This is to ensure that the pipeline is working as expected early, as the pipeline may take a while to run through the entire set of prompts.

The two pipeline validation mechanisms are:
1. **Step Logic Validation**
    Verifies input/output key compatibility between steps, i.e. compile the pipeline can check input/output keys of each step are compatible.
2. **Pipeline Spotcheck**
    Tests the runtime functionality of the pipeline, by executing each step within the pipeline.

### Step Logic Validation
Verifies input/output key compatibility between steps, as a user can unknowingly change the output keys of a step but the later steps may not have been updated to handle the new keys. This validation ensures that the pipeline is working as expected.

```python
# Pipeline automatically validates that each step's required inputs
# are available from previous steps' outputs
pipeline.pipeline_step_logic(experiment_object)
```

### Pipeline Spotcheck
Tests the complete pipeline with a single sample:

```python
# Executes one sample through all steps to verify functionality
pipeline.pipline_spotcheck(experiment_object)
```

## Batch Processing

The pipeline supports batch processing of multiple inputs:

```python
# Create multiple experiment objects
experiment_objects = [
    ExperimentObject(
        data={"text": "First input"}
    ),
    ExperimentObject(
        data={"text": "Second input"}
    )
]

# Process batch
results = pipeline(experiment_objects)
```

## Serialization

Pipelines can be saved and loaded using JSON:

```python
# Save pipeline configuration
config = pipeline.to_json()

# Load pipeline from configuration
loaded_pipeline = BaseAgenticPipeline.from_json(config)
```

The Agentic Pipeline serves as the foundation for more complex experiments like MemoryExperiment and MemoryRAGExperiment, providing robust execution, validation, and recording capabilities for systematic LLM development.
