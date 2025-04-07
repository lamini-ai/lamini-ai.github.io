# Memory Experiment

Memory Experiment provides a framework for running structured experiments with LLMs, combining validators and generators within an agentic pipeline. It enables systematic testing and evaluation of synthetic data generation pipelines.

The need for synthetic data comes into play when you need to build out high quality datasets for fine tuning or RAG. Many cases, there isn't enough ground truth data, the agentic pipelines from Lamini allow for the codification of manual data creation/curation/validation into an automated pipeline.

## Quick Start with Python SDK

First, make sure your API key is set (get yours at [app.lamini.ai/account](https://app.lamini.ai/account)):

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

To initialize your pipeline, you'll need to set up your pipeline components and bundle then within the BaseAgenticPipeline object:

=== "Python SDK"
    Set up your generators:

    ```python
    from lamini.experiment.generators import QuestionsToConceptsGenerator
    from lamini.experiment.pipeline import BaseAgenticPipeline

    # Create a generator
    concept_generator = QuestionsToConceptsGenerator(
        model="meta-llama/Llama-3.1-8B-Instruct",
        name="concept_generator"
    )

    # Create pipeline
    pipeline = BaseAgenticPipeline(
        generators={"concept": concept_generator},
        record_dir="./experiment_results"
    )
    ```

    Set up your validators:

    ```python
    from lamini.experiment.validators import BaseValidator

    # Create a validator
    concept_validator = BaseValidator(
        name="concept_validator",
        instruction="Validate if the following concepts are clear and well-defined: {concepts}",
        model="meta-llama/Llama-3.1-8B-Instruct",
        output_type={"is_valid": "bool", "feedback": "str"},
        is_valid_field="is_valid"
    )

    # Update pipeline with validator
    pipeline = BaseAgenticPipeline(
        generators={"concept": concept_generator},
        validators={"concept": concept_validator},
        record_dir="./experiment_results"
    )
    ```

    Run the pipeline:
    ```python
    from lamini.experiment import ExperimentObject

    # Create input
    experiment_obj = ExperimentObject(
        experiment_step="generation",
        data={"questions": ["What is machine learning?", "How do neural networks work?"]}
    )

    # Execute experiment
    results = pipeline(experiment_obj)
    ```
You can further track your AgenticPipeline experiments within the MemoryExperiment object. Memory experiment is intended to be used to track a sinlge use case (factualQA or text-to-SQL) for LLM development using fine-tuning or RAG. This includes pipeline execution, validation, and memory tuning or RAG jobs, then finally evaluating the results. Iterating is done through enhancing the pipeline components.
Track your experiment progress using the MemoryExperiment class:

```python
from lamini.experiment import MemoryExperiment

# Create a memory experiment to track your pipeline
memory_experiment = MemoryExperiment(
    agentic_pipeline=pipeline,
    model="meta-llama/Llama-3.1-8B-Instruct",  # Model for evaluation/memory tasks
    record_dir="./experiment_results"
)

# Run the experiment
results = memory_experiment(experiment_obj)

# Evaluate results with structured output
response = memory_experiment.evaluate(
    experiment_obj=ExperimentObject(
        experiment_step="evaluation",
        data={"prompt": "Explain the concepts of machine learning"}
    ),
    output_type={"explanation": "str", "confidence_score": "float"}
)
```

## Iteration

To improve your experiment results:

1. Review pipeline results in your record_dir with respect to a golden test 
set
2. Add or modify validators for quality control, based on what errors are 
occurring from the generator and validator outputs with respect to the 
golden test set
3. Experiment with different models and prompts, some models may perform 
better for certain tasks and some models require different styles of prompt 
engineering techniques
4. Fine-tune generator instructions based on validation results
5. Repeat

The experiment framework provides flexibility to iterate and improve your 
pipeline until you achieve the desired performance for your use case.