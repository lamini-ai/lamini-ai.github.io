# Generators

A generator is a component that takes in a prompt and outputs a structured response. Generators ideally are lightweight and can be run in parallel. Keeping a generator light is important because you can have multiple generators in your pipeline. By light, we mean that the generator should be focusing on a single task and not trying to do too much. A single task can vary from extracting a concept to generating a list of questions from a piece of text.

You can create a simple question generator that takes a piece of text and generates a question that can be answered using that text. Here's an example:

```python
from lamini.experiment.generators import BaseGenerator

# Create a simple question generator
question_generator = BaseGenerator(
    name="question_generator",
    model="meta-llama/Llama-3.1-8B-Instruct",
    instruction="Generate a question that can be answered using this text: {text}",
    output_type={"question": "str"}
)

# Use the generator
text = "The first human to walk on the moon was Neil Armstrong in 1969."
result = question_generator(PromptObject(data={"text": text}))
print(result.response["question"])
# Example output: "Who was the first person to walk on the moon?"
```

You can iterate with generators based on the task you want to accomplish. For example, if you want to extract high level concepts from multiple questions, you can use the `QuestionsToConceptsGenerator`. 

```python
from lamini.experiment.generators import QuestionToConceptGenerator

# Create a generator
concept_generator = QuestionToConceptGenerator(
    name="concept_generator",
    model="meta-llama/Llama-3.1-8B-Instruct",
    instruction="Extract a key concept from this question: {question}",
    output_type={"concept": "str"}
)
```

If you want to customize a generator, you can do so by subclassing the BaseGenerator. Here's a complete example:

```python
from lamini.experiment.generators import BaseGenerator
from lamini.generation.base_prompt_object import PromptObject
from pydantic import BaseModel

class ConceptOutput(BaseModel):
    concept: str
    confidence: float

class CustomGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(
            name="custom_generator",
            instruction="Analyze this text and extract the main concept: {text}",
            model="meta-llama/Llama-3.1-8B-Instruct",
            output_type=ConceptOutput
        )
    
    def preprocess(self, prompt_obj: PromptObject) -> PromptObject:
        # Optional: Modify the prompt before generation
        return prompt_obj

    def postprocess(self, prompt_obj: PromptObject) -> PromptObject:
        # Optional: Process the results after generation
        return prompt_obj
```

The BaseGenerator provides several key features:
- Structured input/output handling
- Template-based instructions with metadata injection
- Pre and post-processing hooks
- Error handling and logging
- Result storage and transformation

## Available Generators

| Generator | Description |
|-----------|-------------|
| `QuestionsToConceptsGenerator` | Extracts concepts from multiple questions |
| `QuestionToConceptGenerator` | Extracts concepts from a single question |
| `ConceptToSQLInterpretationGenerator` | Converts concepts into SQL interpretations |
| `SchemaToSQLGenerator` | Generates SQL queries based on database schema |
| `SQLDebuggerGenerator` | Helps debug and fix SQL queries |
| `ComparativeQuestionGenerator` | Generates questions that compare different aspects |
| `EdgeCaseQuestionGenerator` | Creates questions focusing on edge cases and boundary conditions |
| `GranularQuestionGenerator` | Generates detailed, specific questions |
| `ParaphrasingQuestionGenerator` | Rephrases questions in different ways |
| `PatternQuestionGenerator` | Creates questions based on specific patterns |
| `QuestionDecomposerGenerator` | Breaks down complex questions into simpler components |
| `VariationQuestionGenerator` | Generates variations of existing questions |
| `SaveGenerator` | Handles saving and persistence of generator outputs |

## Best Practices

1. **Start with as few generators as possible.**
For example, just 1 QuestionAnswerGenerator, or 1 QuestionGenerator and 1 AnswerGenerator. Run the pipeline and check the generated data, identify issues.
2. **Iterate by modifying the prompt or generators**
These pre-built generators give you a framework and a gooding starting point. However, it is very likely that you will need to modify each generator to make it work for your use case and specific data. You can experiment with modifying the prompts, decoupling a big generator into small ones, adding more generators, and so on.

