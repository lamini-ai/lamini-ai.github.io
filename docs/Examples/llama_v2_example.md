# Question Answer Model

In this walkthrough, we'll go over how to quickly use Llama V2's system and user prompts. If you have enterprise access, feel free to also run the [Colab notebook](https://colab.research.google.com/drive/1kc92-BjRLNa9evn_IKzEMf2z2lMzNo77).

## Import the LlamaV2Runner class

Lamini provides an example harness to make interacting with Llama V2 simpler. Import `LlamaV2Runner` to quickly get started.

```python
from llama import LlamaV2Runner

model = LlamaV2Runner()
```

## A pre-defined interface

`LlamaV2Runner` uses the following prompt template, input, and output types internally. You won't need to re-instantiate these, this class will do the instantiation for you.

<details>
  <summary>Llama V2 Types and Prompt Template</summary>

```python
from llama.prompts.prompt import BasePrompt
from llama import Type, Context


class LlamaV2Input(Type):
    system: str = Context(" ")
    user: str = Context(" ")


class LlamaV2Output(Type):
    output: str = Context(" ")


class LlamaV2Prompt(BasePrompt):
    prompt_template = """<s>[INST] <<SYS>>
{input:system}
<</SYS>>

{input:user} [/INST]"""
```

</details>


## Add example data to the model for training

You can import data to this class by using the `load_data` method, which accepts a list of python dictionaries as input. Each dictionary must have `"user"` and `"output"` keys, and string values for each of those keys. This data is similar to "prompt" and "completion" data you may have seen before. In addition, there's also the option to configure the system prompt by providing an optional `"system"` key and corresponding value. If this is not done, we will use the default sysem prompt. Expand below to see this in action.

```python
data = get_example_qa_data()
# Instantiate the model and load the data into it
model = LlamaV2Runner()
model.load_data(data)
```

<details>
  <summary>Code for <code>get_example_qa_data()</code></summary>

```python
def get_example_qa_data():
    data = [
        {
            "user": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
            "system": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.",
            "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/",
        },
        {
            "user": "Is the Lamini type system similar to a python type system?",
            "output": "Yes, the Lamini type system is built using Pydantic BaseModel.",
        },
        {
            "user": "Does Lamini have a limit on the number of API requests I can make?",
            "output": "Lamini provides each user with free tokens up front.",
        },
        {
            "user": "What does it mean to cancel a job using the `cancel_job()` function? Can we stop the machine from doing its task?",
            "output": "The `cancel_job()` function is used to stop a training job that is currently running.",
        },
        {
            "user": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does it optimize the model for a specific use case?",
            "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization process. It employs an intelligent algorithm to explore the hyperparameter space and find the optimal combination of values. This is done through techniques such as heuristics, grid search, random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes computational resources to evaluate multiple model instances with different hyperparameter configurations. It incorporates techniques like cross-validation to prevent overfitting and ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine learning workflow and improves the chances of developing high-performing models for specific use cases.",
        },
        {
            "user": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized language model?",
            "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license unless otherwise specified. You keep access and ownership of your own data, and we don't use your data to train models for anyone else but you. For more information, please reach out to Lamini directly.",
        },
    ],
    return data
```

</details>

## Train a model and evaluate the results

After you've added data, you can now train a model. Once the training is complete, you can view the eval results.
Training is done on Lamini servers and you can track the training job's progress at [https://app.lamini.ai/train](https://app.lamini.ai/train)

```python
model.train()
print("new model: " + model.model_name)
model.evaluate()
print(model.evaluation)
```

Once a model is trained you can check the eval results to see before and after comparisons of the base model and the trained model. You can also query the new trained model like so

```python
answer = model("How can I add data to Lamini?")
print(answer)
```
