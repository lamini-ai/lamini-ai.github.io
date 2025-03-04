# Memory Experiment

Memory Experiment provides a framework for running structured experiments with LLMs, combining validators and generators within an agentic pipeline. It enables systematic testing and evaluation of model performance with built-in memory capabilities.

## Quick Start with Python SDK

First, make sure your API key is set (get yours at [app.lamini.ai](https://app.lamini.ai)):

=== "Terminal"
    ```sh
    export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
    ```

=== "Python SDK"
    ```python
    import lamini
    import os

    lamini.api_key = os.environ["LAMINI_API_KEY"]
    ```

To use Memory Experiment, you'll need to set up your pipeline components and create an experiment:

=== "Python SDK"
    Set up your generators:
    ```python
    from lamini.experiment.generators import QuestionsToConceptsGenerator
    from lamini.experiment.base_agentic_pipeline import BaseAgenticPipeline

    # Create a generator
    concept_generator = QuestionsToConceptsGenerator(
        model="meta-llama/Llama-2-7b-chat",
        name="concept_generator"
    )

    # Create pipeline
    pipeline = BaseAgenticPipeline(
        generators={"concept": concept_generator},
        record_dir="./experiment_results"
    )
    ```

    Initialize the Memory Experiment:
    ```python
    from lamini.experiment import MemoryExperiment

    experiment = MemoryExperiment(
        agentic_pipeline=pipeline
    )
    ```

    Run the experiment:
    ```python
    from lamini.generation import PromptObject

    # Create input
    prompt = PromptObject(
        data={"questions": ["What is machine learning?", "How do neural networks work?"]}
    )

    # Execute experiment
    results = experiment(prompt)
    ```

A memory experiment is intended to be used to track a sinlge use case (factualQA or text-to-SQL) for LLM development using fine-tuning or RAG. This includes pipeline execution, validation, and memory tuning or RAG jobs, then finally evaluating the results. Iterating is done through enhancing the pipeline components.

## Adding Generators

A generator is a component that takes in a prompt and outputs a structured response. Generators ideally are lightweight and can be run in parallel. Keeping a generator light is important because you can have multiple generators in your pipeline. By light, we mean that the generator should be focusing on a single task and not trying to do too much. A single task can vary from extracting a concept to generating a list of questions from a piece of text.

You can iterate with generators based on the task you want to accomplish. For example, if you want to generate questions from a piece of text, you can use the `QuestionsToConceptsGenerator`. If you want to generate a list of concepts from a piece of text, you can use the `ConceptsToListGenerator`.

```python
from lamini.experiment.generators import QuestionsToConceptsGenerator, ConceptsToListGenerator

# Create a generator
concept_generator = QuestionsToConceptsGenerator(
    model="meta-llama/Llama-2-7b-chat",
    name="concept_generator"
)

concept_list_generator = ConceptsToListGenerator(
    model="meta-llama/Llama-2-7b-chat",
    name="concept_list_generator"
)
```
If you want to customize a generator, you can do so by subclassing the generator and overriding the `generate` method.

```python
class CustomGenerator(BaseGenerator):
    def generate(self, prompt: PromptObject) -> PromptObject:
        # Custom logic here
        return prompt
```

Generators also have a post-generation hook that is called after the generator has run. This is useful for any additional processing you need to do. The add this your generator, simply override the `postprocess` method.

```python
class CustomGenerator(BaseGenerator):
    def postprocess(self, prompt: PromptObject) -> PromptObject:
        # Custom logic here
        return prompt
```

## Adding Validators

Validators are components that take in a prompt and output a structured response to flag whether the output of a generator is valid or not. Validators are used to validate the output of a generator. For example, you can use a factual validator to ensure that the output of a generator is factually correct with respect to a provided text.

```python
from lamini.experiment.validators import FactualityValidator

# Create validator
factual_validator = FactualityValidator(
    model="meta-llama/Llama-2-7b-chat",
    instruction_metadata=["concept"],
    name="factual_validator"
)

# Update pipeline
pipeline = BaseAgenticPipeline(
    generators={"concept": concept_generator},
    validators={"factual": factual_validator},
    order=["concept", "factual"],
    record_dir="./experiment_results"
)
```

If you want to customize a validator, you can do so by subclassing the validator and overriding the `validate` method.

```python
class CustomValidator(BaseValidator):
    def validate(self, prompt: PromptObject) -> PromptObject:
        # Custom logic here
        return prompt
```

Validators are different from generators in that they are forced to return a boolean value. This is important because the agentic pipeline needs to know whether the output of a generator is valid or not to input for a Memory Tuning or Memory RAG job.

This boolean output is forced by the `BaseValidator` class, within the `__init__` method.

```python
class DefaultOutputType(BaseModel):
    """Default output type for validators.

    A simple Pydantic model that includes only an is_valid boolean field.

    Attributes:
        is_valid (bool): Indicates whether validation passed
    """
    is_valid: bool

class BaseValidator(BaseGenerator):
    def __init__(
        self,
        name: str,
        instruction: str,
        client: BaseOpenAIClient = None,
        output_type: Optional[Dict] = None,
        model: Optional[str] = None,
        role: Optional[str] = "",
        instruction_search_pattern: Optional[str] = r"\{(.*?)\}",
        is_valid_field: str = None,
    ):
        super().__init__(
            name=name,
            client=client,
            instruction=instruction,
            output_type=output_type,
            model=model,
            role=role,
            instruction_search_pattern=instruction_search_pattern,
        )

        self.is_valid_field = is_valid_field
        self.output[self.is_valid_field] = "bool"

        if output_type is not None:
            if is_valid_field not in output_type:
                raise ValueError(
                    f"Output format must have a boolean field, set using is_valid_field, which is currently set to '{is_valid_field}'"
                )
            if output_type[is_valid_field] != "bool":
                raise ValueError(
                    f"Output format of the field '{is_valid_field}' must be type 'bool'!"
                )
            self.output_type = self.build_dynamic_model(output_type)
        elif self.is_valid_field is not None:
            # Create an output format with a boolean field called self.is_valid_field
            self.output_type = create_model(
                "DynamicModel",
                **{self.is_valid_field: (bool, ...)},
            )
        else:
            # Create a default output format with a boolean field called "is_valid"
            self.output_type = DefaultOutputType
```

## Generator and Validator Prompt Engineering

Both Generators and Validators utilize python string formatting to inject variables into the prompt. For example, if you want to inject the `content` into the prompt, you can do so by using the following syntax:

```python
prompt = """
First, review the following content:

{chunk}

Next, extract a fact within that content above. Be sure the fact is 
only one sentence and is directly coming from the provided content above.
"""
```

Inject variables are designated by curly braces `{}`. This indicates to the generator or validator that the variable should be coming from the `data` attribute of the `PromptObject` during pipeline execution.

So before the pipeline is executed, the `PromptObject` will be populated with the `data` attribute.

```python
prompt_obj = PromptObject(
    data={"chunk": "This is a test"}
)
```

When the pipeline is executed, the `PromptObject` will be populated with the `data` attribute.

```python
results = pipeline(prompt_obj)
```

Batch processing is also supported through providing a list of `PromptObject` instances to the pipeline. All PromptObjects needs to have the same keys in the `data` attribute.

```python
prompt_objs = [
    PromptObject(data={"chunk": "This is a test"}),
    PromptObject(data={"chunk": "This is another test"})
]  

results = pipeline(prompt_objs)
```

## Memory RAG Integration

To add RAG capabilities to your experiment, you can use the `MemoryRAGExperiment` class. This class will automatically build a memory index of the RAG keys and use it to retrieve similar examples.

```python
from lamini.experiment import MemoryRAGExperiment

# Define which keys to use for RAG
rag_keys = {
    "concept_generator_input": ["questions"],
    "concept_generator_output": ["concepts_list"]
}

# Create RAG experiment
rag_experiment = MemoryRAGExperiment(
    agentic_pipeline=pipeline,
    rag_keys=rag_keys,
    record_dir="./experiment_results"
)

# Run experiment and build index
results = rag_experiment(prompt)

# Query similar examples
similar = rag_experiment.get_similar("What is deep learning?")

# Evaluate with memory augmentation
response = rag_experiment.evaluate(
    prompt="Explain machine learning concepts",
    output_type={"explanation": "str"},
    k=3  # Number of similar examples to retrieve
)
```

## Iteration

To improve your experiment results:

1. Review pipeline results in your record_dir with respect to a golden test set
2. Add or modify validators for quality control, based on what errors are occurring from the generator and validator outputs with respect to the golden test set
3. Experiment with different models and prompts, some models may perform better for certain tasks and some models require different styles of prompt engineering techniques
4. Fine-tune generator instructions based on validation results
5. Repeat

The experiment framework provides flexibility to iterate and improve your pipeline until you achieve the desired performance for your use case.