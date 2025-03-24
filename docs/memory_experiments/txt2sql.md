# Text-to-SQL with Memory Experiment

The Memory Experiment framework provides powerful tools for creating, validating, and improving text-to-SQL models. This document outlines how to use the framework for building and fine-tuning text-to-SQL models for domain-specific databases.

## Overview

Text-to-SQL LLMs enable users to query databases using natural language questions. The Memory Experiment framework streamlines the process of:

1. Generating training data based on sample questions
2. Validating generated SQL queries
3. Analyzing coverage of SQL concepts
4. Fine-tuning models on generated data
5. Evaluating model performance

The complete pipeline helps you create domain-specific text-to-SQL models with high accuracy and comprehensive coverage of database concepts.

## Getting Started

### Prerequisites

Before starting, ensure you have:

- A Lamini API key (get yours at [app.lamini.ai](https://app.lamini.ai))
- Python 3.7+ with pip installed
- The Lamini Python SDK: `pip install lamini`

### Required Inputs

To build a text-to-SQL model with Memory Experiment, you'll need:

1. **Database Schema**: SQL schema of your target database
2. **Glossary File**: JSON file with domain-specific terminology, abbreviations, and business logic
3. **Evaluation Set**: 20-35 sample questions with corresponding SQL queries
4. **SQLite Database**: For testing and validating generated queries

## Step-by-Step Guide

### 1. Setup Project Structure

Create a directory for your text-to-SQL project:

```bash
mkdir txt2sql_project
cd txt2sql_project
```

Prepare your input files:

- `glossary.json`: Key-value pairs of domain terms and their definitions
- `eval_set.jsonl`: Question-SQL pairs for evaluation
- `database.sqlite`: SQLite database for testing and fetching the schema

Create a `config.yml` file to manage API keys and other settings:

```yaml
api:
  url: "https://app.lamini.ai"
  key: "YOUR_LAMINI_API_KEY"

model:
  default: "meta-llama/Llama-3.1-8B-Instruct"
  memory_tuning: "meta-llama/Llama-3.1-8B-Instruct"

database:
  path: "path/to/your/database.sqlite"

paths:
  gold_test_set: "path/to/your/eval_set.jsonl"
  glossary: "path/to/your/glossary.jsonl"

memory_tuning:
  max_steps: 1000
  learning_rate: 3e-5
  max_gpus: 1
  max_nodes: 1
```

### 2. Generate Training Data

Generate variations of questions and SQL queries based on your evaluation set:

```python
import os
import lamini
import pathlib
import datetime

from lamini.experiment.generators import (
    SchemaToSQLGenerator,
    SQLDebuggerGenerator,
    PatternQuestionGenerator,
    VariationQuestionGenerator,
    QuestionDecomposerGenerator
)
from lamini.experiment.validators import (
    SQLValidator
)

from helpers import (
    load_config,
    process_jsonl,
    read_jsonl, 
    get_schema, 
    format_glossary, 
    save_results, 
    generate_variations,
    process_variation
)

# Load configuration
config = load_config("config.yml")

# Set up Lamini API credentials
lamini.api_url = config['api']['url']
lamini.api_key = config['api']['key']

# Initialize generators and validators
generators = {
    "pattern": PatternQuestionGenerator(model=config['model']['default']),
    "variation": VariationQuestionGenerator(model=config['model']['default']),
    "decomposer": QuestionDecomposerGenerator(model=config['model']['default'])
}

sql_gen = SchemaToSQLGenerator(
    model=config['model']['default'],
    db_type="sqlite",
    db_params=str(config['database']['path']),
    schema=get_schema(config['database']['path'])
)

# Process evaluation questions to generate training data
# (See generate_data.py in the repository for the complete implementation)
```

### 3. Analyze Generated Data

Analyze the generated data to identify missing concepts and problematic queries:

```python
import os
import json
import lamini
from typing import List, Dict
from lamini import ErrorAnalysis, SQLErrorAnalysis
from lamini.experiment.generators import (
    SchemaToSQLGenerator,
    SQLDebuggerGenerator
)
from lamini.experiment.validators import (
    SQLValidator
)

# Initialize ErrorAnalysis
error_analysis = ErrorAnalysis(
    model=config['model']['default'],
    schema=schema,
    glossary=formatted_glossary
)

# Analyze topic coverage
coverage_analysis = error_analysis.analyze_topic_coverage(
    gold_questions=gold_questions,
    generated_questions=generated_questions
)

# Generate additional questions for missing topics
additional_questions = []
if coverage_analysis["missing_topics"] or coverage_analysis["underrepresented_topics"]:
    additional_questions = error_analysis.generate_additional_questions(
        coverage_analysis=coverage_analysis,
        num_questions_per_topic=2
    )

# Analyze SQL errors
sql_error_analysis = SQLErrorAnalysis(model=config['model']['default'])
failed_queries = sql_error_analysis.extract_failed_queries(results_data)

# (See analyze_generated_data.py in the repository for the complete implementation)
```

### 4. Memory Tuning

Fine-tune a model on your generated data:

```python
import os
import lamini
from lamini import Lamini
from helpers import read_jsonl, load_config

# Load configuration
config = load_config("config.yml")

# Set up Lamini API credentials
lamini.api_url = config['api']['url']
lamini.api_key = config['api']['key']

# Read training data
input_file = "flattened_training_data.jsonl"
rows = read_jsonl(input_file)

# Configure Memory Tuning
model_name = config['model']['memory_tuning']
max_steps = config['memory_tuning']['max_steps']
learning_rate = config['memory_tuning']['learning_rate']
max_gpus = config['memory_tuning']['max_gpus']
max_nodes = config['memory_tuning']['max_nodes']

# Submit Memory Tuning job
llm = Lamini(model_name=model_name)
results = llm.tune(
    data_or_dataset_id=rows,
    finetune_args={
        "max_steps": max_steps,
        "learning_rate": learning_rate,
    },
    gpu_config={
        "max_gpus": max_gpus,
        "max_nodes": max_nodes
    }
)

# (See memory_tuning.py in the repository for the complete implementation)
```

### 5. Evaluate Model Performance

Test your fine-tuned model against the evaluation set:

```python
import json
import os
import lamini
from lamini import Lamini
from helpers import save_results_to_jsonl, load_config
from lamini.experiment.error_analysis_eval import SQLExecutionPipeline

# Load configuration
config = load_config("config.yml")

# Set up Lamini API credentials
lamini.api_url = config['api']['url']
lamini.api_key = config['api']['key']

# Initialize the model with your fine-tuned model ID
model_id = "YOUR_TUNED_MODEL_ID"  # Replace with your model ID from Memory Tuning
llm = Lamini(model_name=model_id)

# Read test cases
test_cases = read_test_set(config['paths']['gold_test_set'])

# Run inference
inference_results = run_inference(test_cases, model_id)

# Initialize SQL execution pipeline for evaluation
pipeline = SQLExecutionPipeline(
    model=config['model']['default'],
    db_type="sqlite"
)

# Run evaluation
evaluation_results = pipeline.evaluate_queries(
    inference_results,
    connection_params={"db_path": config['database']['path']}
)

# Generate and save report
report = pipeline.generate_report(evaluation_results)

# (See run_inference.py in the repository for the complete implementation)
```

## Custom Components

### Custom SQL Generator

Create a custom SQL question generator by subclassing the base generator:

```python
from lamini.experiment.generators import BaseGenerator

class CustomSQLQuestionGenerator(BaseGenerator):
    def __init__(self, model, name):
        instruction = """
        Given the following database schema and glossary, generate {num_variations} 
        variations of each question in the list of questions.
        
        Schema:
        {schema}
        
        Glossary:
        {glossary}
        
        Questions:
        {questions}
        
        Generate diverse variations that test different SQL concepts while 
        maintaining the same intent as the original questions.
        """

        super().__init__(
            name=name,
            instruction=instruction,
            model=model,
            output_type={"variations": "list"}
        )

    def postprocess(self, prompt):
        # Add any custom post-processing logic
        return prompt
```

### Custom SQL Validator

Create a custom SQL validator to check query correctness:

```python
from lamini.experiment.validators import BaseValidator

class CustomSQLValidator(BaseValidator):
    def __init__(self, model, name, db_path):
        instruction = """
        Validate if the following SQL query is correct and will run against 
        the given database schema.
        
        Schema:
        {schema}
        
        Query:
        {query}
        
        Provide detailed feedback on any issues found.
        """

        super().__init__(
            name=name,
            instruction=instruction,
            model=model,
            is_valid_field="is_valid",
            output_type={"is_valid": "bool", "feedback": "str"}
        )

        self.db_path = db_path

    def validate(self, prompt):
        # Add custom validation logic using SQLite
        # Example: Execute query against database and catch errors
        return prompt
```

## Complete Example

For a complete, working example of a text-to-SQL pipeline, visit our GitHub repository:

[SQL Generation & Analysis Pipeline](https://github.com/lamini-ai/txt2sql-examples)

The repository contains all the scripts mentioned in this documentation:

- `generate_data.py`: Generate training questions and SQL queries
- `analyze_generated_data.py`: Analyze coverage and generate additional data
- `memory_tuning.py`: Fine-tune a model on generated data
- `run_inference.py`: Evaluate model performance

## Best Practices

1. **Quality Glossary**: Create a comprehensive glossary covering domain-specific terms, abbreviations, and business logic
2. **Diverse Evaluation Set**: Include various query types (SELECT, JOIN, GROUP BY, etc.) in your evaluation set
3. **Iterative Improvement**: Analyze failed queries and use them to improve your generators, validators and glossary
4. **Schema**: Add key-value pairs about the schema to the glosary for the model to understand table relationships
5. **Validation Checks**: Use multiple validators to ensure query correctness, execution, and result accuracy

## Troubleshooting

- **Invalid SQL Generation**: Check your schema formatting and ensure glossary covers all domain terms
- **Poor Performance**: Increase the diversity of your generated data or fine-tune for more steps
- **Missing Concepts**: Use the analyzer to identify and generate data for uncovered concepts
- **Execution Errors**: Verify your SQLite database matches the schema exactly

## Conclusion

The Memory Experiment framework provides a powerful and flexible way to build text-to-SQL models for domain-specific databases. By following this guide, you can create, fine-tune, and evaluate models that accurately convert natural language questions to SQL queries in your specific domain.
