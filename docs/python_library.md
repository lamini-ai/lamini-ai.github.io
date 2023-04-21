# Python library

Llama is a Python package designed to build Language Learning Models (LLMs) for natural language processing tasks. It provides an engine for creating and running your own LLMs. With Llama, you can train language models on large text corpora and improve them following your guidelines, which can then be used for generating and extracting text.

## Input and output types

First, you want to construct some data types: (1) input types as arguments into the LLM and (2) output types as return values from the LLM.

You can use the `Type` and `Context` classes in the library create them.

For example, you can create an `Animal` type as follows:

```python
from llama import Type, Context

class Animal(Type):
    name: str = Context("name of the animal")
    n_legs: int = Context("number of legs that animal has")

llama_animal = Animal(name="Larry", n_legs=4)
```

Each `Type` requires at least one attribute, such as `name` and `n_legs` here. They can be anything you would like. Be sure to add a `Context` field to each attribute, with a natural language description of the attribute. That is required to tell the model what you mean by each attribute.

## Running the LLM

Next, you want to instantiate your LLM engine with `LLM`.

```python
llm = LLM(name="animal_stories")

# If you want to use a different base model or add your config options here
llm = LLM(
    name="my_llm_name",
    model_name="chat-gpt",
    config={
        "production": {
            "key": "<API-KEY-HERE>",
            "url": "https://api.powerml.co",
        }
    },
)
```

Now, you can now run your LLM.

```python
# Define an output type
class Story(Type):
    story: str = Context("Story of an animal")

llama_animal = Animal(name="Larry", n_legs=4)
llama_story = llm(llama_animal, output_type=Story)
```

## Adding data

You have data on different inputs and outputs, and in some cases, you have pairs of inputs and outputs that you want the LLM to model after.

Getting data of good inputs:
```python
llama_animal = Animal(name="Larry", n_legs=4)
centipede_animal = Animal(name="Cici", n_legs=100)

my_data = [llama_animal, centipede_animal]
```

Getting data of a good input-output pair:
```python
dog_animal = Animal(name="Nacho", n_legs=4)
dog_speed = Story(story="There once was a cute doggo named Nacho. She was a golden retriever who liked to run. All four of her paws were adorable.")

my_data.append([dog_animal, dog_speed])
```

Now add all that data to your LLM:
```python
llm.add_data(my_data)
```

With the same call to the LLM engine, it should now produce a story that is more aligned with your data.
```python
llama_story = llm(llama_animal, output_type=Story)
```

## Improving with criteria

Now that you've added data, you want to improve the model's outputs further. Another way to do that is to supply `improve` statements on different attributes of a model's output type to improve on. You can use natural language to tell the model how it should improve.

```python
llm.improve(on="story", to="specify the number of legs in a subtle way")
```

## Full example

Start with data.

```python
class Animal(Type):
    name: str = Context("name of the animal")
    n_legs: int = Context("number of legs that animal has")

class Speed(Type):
    speed: float = Context("how fast something can run")

llama_animal = Animal(name="Larry", n_legs=4)
centipede_animal = Animal(name="Cici", n_legs=100)

my_data = [llama_animal, centipede_animal]

dog_animal = Animal(name="Nacho", n_legs=4)
dog_speed = Story(story="There once was a cute doggo named Nacho. She was a golden retriever who liked to run. All four of her paws were adorable.")

my_data.append([dog_animal, dog_speed])
```

Instantiate the LLM engine, add data, add improvements (as many as you like), and run the LLM engine.

```python
llm = LLM(name="animal_stories")

llm.add_data(my_data)
llm.improve(on="story", to="specify the number of legs in a subtle way")

story = llm(llama_animal, output_type=Story)
```

A common workflow is to run the LLM engine and see issues in the LLM outputs, then add an improve statement and run the LLM engine again.
