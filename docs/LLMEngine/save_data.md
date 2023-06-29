# llama.LLMEngine.save_data

Adds data to the LLMEngine.

```python
llm.save_data(my_data)

llm.save_data([my_data, my_other_data, ...])

llm.save_data([[input_data, output_data], [more_input_data, more_output_data], ...])
```

## Parameters

- data: `<class 'llama.types.type.Type'>` or `List[<class 'llama.types.type.Type'>]` or `List[List[<class 'llama.types.type.Type'>]]` - data structured as `Type`'s, grouped in lists because they're related to each other, and added in bulk through lists. 1-100k data elements are recommended at a time.

## Example

```python
llama_animal = Animal(name="Larry", n_legs=4)
centipede_animal = Animal(name="Cici", n_legs=100)

my_data = [llama_animal, centipede_animal]

dog_animal = Animal(name="Sally", n_legs=4)
dog_speed = Speed(speed=30.0)

my_data.append([dog_animal, dog_speed])

llm.save_data(my_data)
```
