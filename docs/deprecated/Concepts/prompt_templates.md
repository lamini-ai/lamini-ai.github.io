# Prompt Templates

Under the hood, Lamini's LLM Engine converts your structured data into a string for the LLM to ingest. Then, the Lamini class uses the model output to produce structured output.

The engine provides tuned default conversion, but you may want greater control over the input to the model. To do this, Lamini provides a `prompt_template` interface. Let's look at an example.

## Question Example

The following `prompt_template` has the notation `{input:question}`, indicating that the field `question` from the `input` in each `llm()` inference call will be the entirety of the prompt.

```python
llm = Lamini(
    id="prompt_example",
    model_name="meta-llama/Llama-2-7b-chat-hf",
    prompt_template="{input:question}",
)
```
For example, when we do 
```python
returned_value = llm(input={"question":"What is my name?"}, output_type={"output": "str"})
```
The final prompt that is evaluated by the model is
```
What is my name?
```
Then, we will receive a dictionary back from the Lamini API that is formatted exactly as `output_type` specifies.
```python
print(returned_value)

{"output": "I am a language model and do not know your name. Would you like to tell me what it is?"}
```

<details>
  <summary>Strictly Typed interface via LLMEngine</summary>

In this example, we're extending a simple utility class `BasePrompt` which just validates that the `prompt_template` is a string. We can name our class `QAPrompt` and write a template inspired by the Alpaca dataset.

```python
from llama.prompts.prompt import BasePrompt

class QAPrompt(BasePrompt):
    prompt_template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.
### Instruction: {input:question}

### Response:"""
```

`QAPrompt` can now be used with `LLMEngine` by passing the object into the `prompt` field of the class init like so

```python
prompt = QAPrompt()
llm = LLMEngine(
    id="prompt_example",
    model_name="meta-llama/Llama-2-7b-chat-hf",
    prompt_template=prompt.prompt_template,
)
```

### Syntax
In order to form the prompt, our service uses this 'f-string'-esque notation to substitute fields from the input object into the `prompt_template`.

This template
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.
### Instruction: {input:question}

### Response:
```

in conjunction with this `Type`

```python
from llama import Type, Context

class Question(Type):
    question: str = Context("a question")

class Answer(Type):
    answer: str = Context("the response to the question")

ans = llm(Question(question="What are prompts?"), Answer)
```

will produce this "hydrated" prompt.

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.
### Instruction: What are prompts?

### Response:
```

Including more fields is simply a matter of adding `{input:<FIELD_NAME>}` into the `prompt_template` string.

### Training
During training, the custom prompt is also used. **Make sure to use the same `prompt_template` during inference** if you have finetuned a model with a custom prompt.
</details>



## Llama 2 Example

Llama 2 has a more complex prompt.
The following `prompt_template` has the notation 
```
[INST] <<SYS>>
{input:system}
<</SYS>>
{input:user} [/INST]
```
indicating that the fields `system` and `user` are required fields in the `input` for each `llm()` inference call. The values in those fields will be substituted into the prompt template, as if you were calling a simple python f-string (format) operation.

```python
llm = Lamini(
    id="llama2_example",
    model_name="meta-llama/Llama-2-7b-chat-hf",
    prompt_template="{input:question}",
)
```
For example, when we do 
```python
returned_value = llm(input={"system": "You are an all-knowing ai assistant", "user":"What is my name?"}, output_type={"output": "str"})
```
The final prompt that is evaluated by the model is
```
[INST] <<SYS>>
You are an all-knowing ai assistant
<</SYS>>
What is my name? [/INST]
```
Then, we will receive a dictionary back from the Lamini API that is formatted exactly as `output_type` specifies.
```python
print(returned_value)

{"output": "I am a language model and your name is Alice."}
```

<details>
  <summary>Strictly Typed interface via LLMEngine</summary>
Here's an example of the Llama V2 prompt

```python
from llama.prompts.prompt import BasePrompt
from llama import Type, Context


class LlamaV2Input(Type):
    system: str = Context(" ")
    user: str = Context(" ")


class LlamaV2Output(Type):
    output: str = Context(" ")


class LlamaV2Prompt(BasePrompt):
    prompt_template = """[INST] <<SYS>>
{input:system}
<</SYS>>
{input:user} [/INST]"""
```

You can try this out by importing `LlamaV2Prompt` from the python package

```python
from llama.prompts.llama_v2_prompt import LlamaV2Prompt, LlamaV2Input, LlamaV2Output
```
Or, try it out by using the convenience class `LlamaV2Runner` we've provided
```python
from llama.runners.llama_v2_runner import LlamaV2Runner
```
</details>