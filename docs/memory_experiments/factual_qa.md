# Factual Question-Answering with Memory Experiment

The Memory Experiment framework provides powerful tools for creating, validating, and improving factual question-answering models. This document outlines how to use the framework for building and fine-tuning models that can accurately answer questions based on provided source materials.

## Overview

Factual QA LLMs enable users to get accurate answers from source materials. The Memory Experiment framework streamlines the process of:

1. Extracting key facts and concepts from source materials
2. Generating high-quality training questions and answers
3. Validating answer accuracy against source material
4. Fine-tuning models on generated data
5. Evaluating model performance

The complete pipeline helps you create domain-specific factual QA models with high accuracy and comprehensive coverage of source materials.

## Getting Started

### Prerequisites

Before starting, ensure you have:

- A Lamini API key (get yours at [app.lamini.ai](https://app.lamini.ai))
- Python 3.7+ with pip installed
- The Lamini Python SDK: `pip install lamini`

### Required Inputs

To build a factual QA model with Memory Experiment, you'll need:

1. **Documents**: Text documents containing ground truth information
2. **Evaluation Set**: 20-35 sample questions with corresponding answers from source materials
3. **Knowledge Base**: Structured storage of extracted facts and relationships, typically stored within a JSON lines file.

## Step-by-Step Guide

### 1. Setup Project Structure

Create a directory for your factual QA project:

```bash
mkdir factual_qa_project
cd factual_qa_project
```

Prepare your input files:

- `source_materials/`: Directory containing your documents
- `eval_set.jsonl`: Question-answer pairs for evaluation
- `knowledge_base.json`: Structured storage of extracted facts

Create a `config.yml` file to manage API keys and other settings:

```yaml
api:
  url: "https://app.lamini.ai"
  key: "YOUR_LAMINI_API_KEY"

model:
  default: "meta-llama/Llama-3.1-8B-Instruct"
  memory_tuning: "meta-llama/Llama-3.1-8B-Instruct"

paths:
  source_materials: "path/to/your/source_materials/"
  gold_test_set: "path/to/your/eval_set.jsonl"
  knowledge_base: "path/to/your/knowledge_base.json"

memory_tuning:
  max_steps: 1000
  learning_rate: 3e-5
  max_gpus: 1
  max_nodes: 1
```

### 2. Generate Training Data

Extract facts and generate questions using various generators:

```python
import os
import lamini
import pathlib
import datetime

from lamini.experiment.generators import (
    FactExtractor,
    ConceptExtractor,
    QuestionGenerator,
    AnswerGenerator,
    QuestionDecomposer
)
from lamini.experiment.validators import (
    FactualValidator,
    RelevanceValidator,
    AnswerValidator
)

# Load configuration
config = load_config("config.yml")

# Set up Lamini API credentials
lamini.api_url = config['api']['url']
lamini.api_key = config['api']['key']

# Initialize generators
generators = {
    "fact": FactExtractor(model=config['model']['default']),
    "concept": ConceptExtractor(model=config['model']['default']),
    "question": QuestionGenerator(model=config['model']['default']),
    "answer": AnswerGenerator(model=config['model']['default']),
    "decomposer": QuestionDecomposer(model=config['model']['default'])
}

# Process source materials to generate training data
# (See generate_data.py in the repository for the complete implementation)
```

### 3. Analyze Generated Data

Analyze the generated data to identify coverage gaps and validate accuracy:

```python
from lamini import ErrorAnalysis, FactualErrorAnalysis
from lamini.experiment.validators import (
    FactualValidator,
    RelevanceValidator
)

# Initialize ErrorAnalysis
error_analysis = ErrorAnalysis(
    model=config['model']['default'],
    knowledge_base=knowledge_base,
    glossary=formatted_glossary
)

# Analyze topic coverage
coverage_analysis = error_analysis.analyze_concept_coverage(
    gold_questions=gold_questions,
    generated_questions=generated_questions
)

# Generate additional questions for missing concepts
additional_questions = []
if coverage_analysis["missing_concepts"] or coverage_analysis["underrepresented_concepts"]:
    additional_questions = error_analysis.generate_additional_questions(
        coverage_analysis=coverage_analysis,
        num_questions_per_concept=2
    )

# Analyze answer accuracy
factual_error_analysis = FactualErrorAnalysis(model=config['model']['default'])
incorrect_answers = factual_error_analysis.extract_incorrect_answers(results_data)
```

### 4. Memory Tuning

Fine-tune a model on your generated data:

```python
from lamini import Lamini

# Configure Memory Tuning
model_name = config['model']['memory_tuning']
max_steps = config['memory_tuning']['max_steps']
learning_rate = config['memory_tuning']['learning_rate']

# Submit Memory Tuning job
llm = Lamini(model_name=model_name)
results = llm.tune(
    data_or_dataset_id=training_data,
    finetune_args={
        "max_steps": max_steps,
        "learning_rate": learning_rate,
    },
    gpu_config={
        "max_gpus": max_gpus,
        "max_nodes": max_nodes
    }
)
```

### 5. Evaluate Model Performance

Test your fine-tuned model against the evaluation set:

```python
from lamini.experiment.error_analysis_eval import FactualQAPipeline

# Initialize the evaluation pipeline
pipeline = FactualQAPipeline(
    model=config['model']['default'],
    knowledge_base=knowledge_base
)

# Run evaluation
evaluation_results = pipeline.evaluate_answers(
    inference_results,
    source_materials=config['paths']['source_materials']
)

# Generate and save report
report = pipeline.generate_report(evaluation_results)
```

## Custom Components

### Custom Fact Extractor

Create a custom fact extractor:

```python
from lamini.experiment.generators import BaseGenerator

class CustomFactExtractor(BaseGenerator):
    def __init__(self, model, name):
        instruction = """
        Given the following document, extract key facts and their relationships.
        
        Document:
        {source_material}
        
        Extract facts that are:
        1. Explicitly stated
        2. Important for understanding the material
        3. Can be used to answer potential questions
        """

        super().__init__(
            name=name,
            instruction=instruction,
            model=model,
            output_type={"facts": "list"}
        )
```

### Custom Answer Validator

Create a custom validator to check answer accuracy:

```python
from lamini.experiment.validators import BaseValidator

class CustomAnswerValidator(BaseValidator):
    def __init__(self, model, name, knowledge_base):
        instruction = """
        Validate if the following answer is correct according to the document.
        
        Question: {question}
        Given Answer: {answer}
        Source Material: {source}
        
        Check for:
        1. Factual accuracy
        2. Completeness
        3. Relevance to the question
        """

        super().__init__(
            name=name,
            instruction=instruction,
            model=model,
            is_valid_field="is_valid",
            output_type={"is_valid": "bool", "feedback": "str"}
        )
```

## Best Practices

1. **Quality Documents**: Ensure documents are well-organized and contain clear, factual information
2. **Comprehensive Extraction**: Extract both explicit facts and implicit relationships
3. **Diverse Question Types**: Generate questions that test different types of knowledge and reasoning
4. **Validation Chain**: Use multiple validators to ensure answer accuracy and relevance
5. **Knowledge Base Structure**: Organize extracted facts in a way that preserves relationships and context

## Troubleshooting

- **Incorrect Answers**: Review fact extraction process and knowledge base coverage
- **Poor Performance**: Increase training data diversity or adjust fine-tuning parameters
- **Missing Concepts**: Use the analyzer to identify and generate data for uncovered concepts
- **Inconsistent Answers**: Check for conflicting information in source materials

## Conclusion

The Memory Experiment framework provides a robust solution for building factual QA models that can accurately answer questions based on source materials. By following this guide, you can create, fine-tune, and evaluate models that provide reliable and accurate answers in your specific domain.
