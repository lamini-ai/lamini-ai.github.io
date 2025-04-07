# Generator and Validator Prompt Engineering

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

## PromptObject Data

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