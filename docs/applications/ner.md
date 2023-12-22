
# Named entity recognition with LLMs

Named entity recognition (NER) is the task of identifying and classifying named entities in text. Named entities are typically proper nouns, such as people, places, organizations, or dates. NER is a common task in natural language processing (NLP) and information retrieval (IR), and is used in many applications, such as question answering, text summarization, and machine translation.

You can use LLMs for NER. Here are several tools in your Lamini toolbox for doing so.

Note: These tools are in order of increasing difficulty to get right:

1. JSON output
2. LLM Classifier
3. Finetuning

We recommend starting with the first one, and moving onto the next one, if you need to get better results.


- [LLM - JSON output](../inference/json_output.md)

The simplest first pass is to use Lamini's JSON output harness, which takes any LLM and makes it output a guaranteed JSON schema of your choosing.

* Easy input: you can prompt-engineer it
* Reliable output: guaranteed JSON schema to your specs (simple structure)
* Extract arbitrary named entities, not just fixed labels/classes
* Main downside: You can only add data through prompt-engineering (includes adding RAG outputs), but you cannot teach the model new information from lots of data

Here is some sample code of how to use the JSON output harness for NER. The task here is to label noun phrases in a sentence with the type of noun phrase it is. The output is a JSON object with the label as a string.

```python
from lamini import Lamini

llm = Lamini("meta-llama/Llama-2-7b-chat-hf")
output_type = {"label": "string"}

prompt = """Labels:
"Anatomy": "Refers to the physical structure and parts of animals."
"Foreign Substance/Organism": "Anything not naturally part of the animal's body, including parasites and foreign objects."
"Body Substance": "Bodily fluids or tissues, like blood or tissue samples."
"Patient": "The animal receiving care."
"Demographic": "Type of animal."

Sentence: Brewer is a canine patient.

Noun Phrase: Brewer
Label (as JSON object):"""

out = llm.generate(prompt, output_type=output_type)
print(out)
# {'label': 'Patient'}
```

The response was from Llama 2-7B and labeled Brewer as 'Patient' correctly. The output is valid JSON of the type specified in the output_type parameter (in this case, a 'label' as a string).

Notice that the prompt includes the label options, the sentence, and the noun phrase. You can prompt-engineer this, until you get the output you want. For example, you can add examples of correct input-output pairs to the prompt. This is easy, but also a limitation of the JSON harness because you can't add large numbers of datapoints to it (which if you have, you might want to do). 

To run many noun phrases at a time (e.g. ~10 to start), you can submit this as a batch call, meaning you could create a list of prompts, for every noun phrase in the sentence and then submit that into `generate`:

```python
out = llm.generate(list_of_prompts, output_type=output_type)
# [{'label': 'Patient'}, {'label': 'Anatomy'}, ...]
```

JSON output is great in that it encourages the model to output the right thing, but it's not teaching it on any new data yet, so there could still be a performance gap. That said, if you run this at a larger scale (~30 examples), you can score how well the model does (% correct out of ~30) and that can guide whether you can just use it as is, or you should advance to the next step.

- [LLM Classifier](../applications/classifier.md)

While the JSON harness mainly deals with prompts (you can "add data" to prompts to some extent), the LLM Classifier can handle BOTH prompts and data. Regarding data, you can put an unlimited amount in.

For this use case, if you have a fixed set of labels, then the classifier can be effective in a similar way to how the JSON harness was used above, but can offer the added benefits of:
* Learning on your data (that can be a lot, esp over time)
* Running extremely fast at inference (faster than the JSON harness, once trained, but needs more time, on the order of usually minutes, to train)

```python
from lamini import LaminiClassifier

llm = LaminiClassifier()

prompts={
  "Anatomy": "Refers to the physical structure and parts of animals.",
  "Foreign Substance/Organism": "Anything not naturally part of the animal's body, including parasites and foreign objects.",
  "Body Substance": "Bodily fluids or tissues, like blood or tissue samples.",
  "Patient": "The animal receiving care.",
  "Demographic": "Type of animal."
}

llm.add_data_to_class("Patient", "Text: Brewer is a canine patient. Noun Phrase: patient")
llm.add_data_to_class("Demographic", "Text: Brewer is a canine patient. Noun Phrase: canine")

llm.prompt_train(prompts)

out = llm.predict(["Text: Brewer is a canine patient. Noun Phrase: Brewer"])
print(out)
# ['Patient']
```

Notice that you can prompt-engineer via the prompts with entity label and description pairs. 

Your other tool is adding data, which is optional. You can add data via the `llm.add_data_to_class` method, before training (`llm.prompt_train` on the prompts). 

You can add as much data as you want. For every class, e.g. `Patient`, you can add a list of strings to it in one call of `add_data_to_class`, e.g. 

```python
llm.add_data_to_class("Patient", ["Text: Brewer is a canine patient. Noun Phrase: patient", "Text: Brewer is a canine patient. Noun Phrase: Brewer"])
```

Note that the example shows adding the context in the datapoints, with the text (sentence) and the noun phrase. 

Like the JSON harness, you can pass in multiple prompts in a list of prompts, e.g.

```python
llm.predict(["Text: Brewer is a canine patient. Noun Phrase: Brewer", "Text: Brewer is a canine patient. Noun Phrase: patient"])
```

- [Finetuning](../training/finetuning.md)

The premise of finetuning is to give you maximum control over the output behavior of the model and the content it learns. It takes the LLM Classifier and JSON harness to overdrive. But with maximal flexibility, it is also much harder to get right, because there's so much you can do. It also needs more data. 

Whereas the JSON harness and LLM Classifier can be effective with no data (just prompt-engineering), finetuning needs ~100 to ~1000 examples to see results. It's an iterative process of finding what the right number of data points is for your specific application.

```python
from lamini import Lamini

input1 = """Labels:
"Anatomy": "Refers to the physical structure and parts of animals."
"Foreign Substance/Organism": "Anything not naturally part of the animal's body, including parasites and foreign objects."
"Body Substance": "Bodily fluids or tissues, like blood or tissue samples."
"Patient": "The animal receiving care."
"Demographic": "Type of animal."

Sentence: Brewer is a canine patient.

Noun Phrase: Brewer
Label (as JSON object):"""

output1 = "{'label': 'Patient'}"

data = [
    {"input": input1, "output": output1}
    # you should pass in way more data in this list, but this is the format, mirroring the above with the JSON harness
]

llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
llm.train(data=data)
```

The `Lamini` class handles any model, string in, string out. Notice that the desired output here is formatted like the JSON harness output. This is so that you can later use the JSON harness on top of this finetuned model.
