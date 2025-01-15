# Classifier Agent Toolkit

The Lamini Classifier Agent Toolkit (CAT) allows you to create and refine a key building block for agentic workflows: classifiers that can quickly categorize a large number of text inputs across any number of pre-defined categories.

What sets CAT apart from other LLMs and classification tools:

- Accuracy for many classes: >99% accuracy on evals even with >500 classes

- High throughput: process 100k tokens/s

- Consistent latency: sub-2s latency, with 1000s of inputs and 100s of classes

- Confidence scores: for more accurate workflows

- Built for iteration: compare models with metrics to measure progress


You can use CAT via Lamini's [REST API](../api.md), [Python SDK](../lamini_python_class/lamini.md#laminiclassifylamini_classifier), or [web interface](https://app.lamini.ai/classify). Or step through an  [example notebook](https://github.com/lamini-ai/lamini-examples/blob/main/classify/classify.ipynb).

| Step | Action | Best Practices |
|------|--------|---------------|
| 1 | Create project | Set up new classifier |
| 2 | Add examples | ~3 diverse examples per class, balanced number of examples per class |
| 3 | Train & predict | Get predictions with confidence scores (~1 min/class) |
| 4 | Evaluate | Validate metrics and test performance |
| 5 | Iterate | Add examples and retrain to improve accuracy |

## Quick Start with Python

First, make sure your API key is set (get yours at app.lamini.ai):

```sh
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

Create a new classifier project:
```python
from lamini.classify.lamini_classifier import LaminiClassifier

cls = LaminiClassifier("MyClassifierProject")
```

Once the project is created, we define the classes. The more detailed the description, the higher your accuracy will be.

```python
classes = {
    "cat": """The cat (Felis catus), also referred to as domestic cat or house cat, is a small domesticated carnivorous mammal. It is the only domesticated species of the family Felidae. Advances in archaeology and genetics have shown that the domestication of the cat occurred in the Near East around 7500 BC. It is commonly kept as a pet and farm cat, but also ranges freely as a feral cat avoiding human contact. Valued by humans for companionship and its ability to kill vermin, the cat's retractable claws are adapted to killing small prey like mice and rats. It has a strong, flexible body, quick reflexes, and sharp teeth, and its night vision and sense of smell are well developed. It is a social species, but a solitary hunter and a crepuscular predator. Cat communication includes vocalizations—including meowing, purring, trilling, hissing, growling, and grunting–as well as body language. It can hear sounds too faint or too high in frequency for human ears, such as those made by small mammals. It secretes and perceives pheromones.
            Domain:	Eukaryota
            Kingdom:	Animalia
            Phylum:	Chordata
            Class:	Mammalia
            Order:	Carnivora
            Suborder:	Feliformia
            Family:	Felidae
            Subfamily:	Felinae
            Genus:	Felis
            Species:	F. catus[1]""",
    "dog": """The dog is a domesticated descendant of the wolf. Also called the domestic dog, it was selectively bred from an extinct population of wolves during the Late Pleistocene by hunter-gatherers. The dog was the first species to be domesticated by humans, over 14,000 years ago and before the development of agriculture. 
            Domain:	Eukaryota
            Kingdom:	Animalia
            Phylum:	Chordata
            Class:	Mammalia
            Order:	Carnivora
            Family:	Canidae
            Genus:	Canis""",
}   
```

Adding example inputs is optional, but will also help with accuracy. You can always do this later - we'll show you how later in this notebook.

```python
examples = {
    "cat": [
        "Tend to be independent and aloof.",
        "Territorial and defensive .",
        "Self-grooming animals, using their tongues to keep their coats clean and healthy.",
        "Use body language and vocalizations, such as meowing and purring, to communicate."
    ],
    "dog": [
        "Social, pack-oriented, and tend to be more loyal to their human family.",
        "Need regular grooming from their owners, including brushing and bathing.",
        "Bark and growl to convey their messages.",
        "Responsive to human commands and can be trained to perform a wide range of tasks."
    ],
}
```

Now we initialize the project. This can take about a minute per class, so we'll put in a simple timer to keep us updated on status.

```python
resp = cls.initialize(classes, examples) 

import time

while True:
    print("Waiting for classifier to initialize")
    time.sleep(5)
    resp = cls.train_status()
    if resp["status"] == "completed":
        print("Model ID: " + resp["model_id"])
        first_model_id = resp["model_id"]
        break
    if resp["status"] == "failed":
        print(resp["status"])
        raise Exception("failed training")
```

Cool, we have our first model version! Let's try it out with a quick test.


```python
import json

print(json.dumps(cls.classify("woof"), indent=2))
```

Here's the expected output:

```json
{
  "classification": [
    [
      {
        "class_id": 1,
        "class_name": "dog",
        "prob": 0.5267619385770103
      },
      {
        "class_id": 0,
        "class_name": "cat",
        "prob": 0.47323806142298974
      }
    ]
  ]
}
```

Now we can see how useful the classifier output is. We get a list of all the categories we defined in our project, plus a confidence score for each.

We can go even further to easily quantify the accuracy of our classifier. Let's run an evaluation!

What an evaluation means for a classifier: when you provide a set of inputs and the expected output, we can test the accuracy of the model on those inputs, and give you back both overall metrics as well as per-input assessment.

```python
from lamini.one_evaler.one_evaler import LaminiOneEvaler

eval = LaminiOneEvaler(
    test_model_id=first_model_id,
    eval_data_id=f"first_eval{random.randint(1000,9999)}",
    eval_data=[{"input": "woof", "target": "dog"}, {"input": "meow", "target": "cat"}],
    test_eval_type="classifier",
)
```

Expected output:
```python
print(json.dumps(eval.run(), indent=2))
```

```json
{
  "eval_job_id": "1424247633",
  "eval_data_id": "first_eval6032",
  "metrics": {
    "tuned_accuracy": 1.0,
    "tuned_precision": 1.0,
    "tuned_recall": 1.0,
    "tuned_f1": 1.0
  },
  "status": "COMPLETED",
  "predictions": [
    {
      "input": "woof",
      "target": "dog",
      "test_output": "dog",
      "base_output": null
    },
    {
      "input": "meow",
      "target": "cat",
      "test_output": "cat",
      "base_output": null
    }
  ]
}
```

That first run was ok, but we can do better. Let's add some more examples and retrain to improve accuracy. You control when to add data and when to train.

```python
resp = cls.add(
    "additional_data",
    {
        "cat": [
            "Cats spend up to sixteen hours a day sleeping, making them some of nature's most dedicated nappers.",
            "Felines possess an extraordinary sense of balance thanks to their flexible backbone and righting reflex.",
            "A cat's sandpaper-like tongue is covered in tiny hooks called papillae that help them groom themselves effectively.",
            "Female cats tend to be right-pawed while male cats are more often left-pawed, according to scientific studies.",
            "Ancient Egyptians showed their devotion to cats by mummifying them alongside their human companions.",
        ],
        "dog": [
            "Dogs have evolved alongside humans for over 15,000 years, developing an uncanny ability to read our facial expressions and emotions.",
            "The average dog can understand around 165 different words or signals, though some exceptional dogs can learn many more.",
            "A dog's sense of smell is roughly 40 times greater than a human's, allowing them to detect diseases and track scents that are days old.",
            "Unlike humans who have three cones in their eyes, dogs only have two, making them partially colorblind but excellent at detecting movement.",
            "The Basenji breed is known as the 'barkless dog' because it produces an unusual yodel-like sound instead of a typical bark.",
        ],
    },
)

resp = cls.train()

while True:
    print("Waiting for classifier to train")
    time.sleep(5)
    resp = cls.train_status()
    if resp["status"] == "completed":
        print("Model ID: " + resp["model_id"])
        second_model_id = resp["model_id"]
        break
    if resp["status"] == "failed":
        print(resp["status"])
        raise Exception("failed training")
```

Great, now we have a second model version in our project! Let's run an eval and compare it to the first version.

```python
print("Running comparison eval between model versions " + first_model_id + " and " + second_model_id)

eval_2 = LaminiOneEvaler(
    test_model_id=first_model_id,
    eval_data_id=f"second_eval{random.randint(1000,9999)}",
    eval_data=[{"input": "woof", "target": "dog"}, {"input": "meow", "target": "cat"}],
    test_eval_type="classifier",
    base_model_id=second_model_id,
    sbs=True,
    fuzzy=True,
)

print(json.dumps(eval_2.run(), indent=2))
```

Expected output:
```json
Running comparison eval between model versions 8a9fe622-4555-4646-886a-dc94b16a56f2 and 9739bf49-82ab-4e69-8149-5b891111516e
{
  "eval_job_id": "2044167961",
  "eval_data_id": "second_eval9291",
  "metrics": {
    "base_accuracy": 1.0,
    "base_precision": 1.0,
    "base_recall": 1.0,
    "base_f1": 1.0,
    "base_fuzzy_accuracy": 1.0,
    "base_fuzzy_precision": 1.0,
    "base_fuzzy_recall": 1.0,
    "base_fuzzy_f1": 1.0,
    "tuned_accuracy": 1.0,
    "tuned_precision": 1.0,
    "tuned_recall": 1.0,
    "tuned_f1": 1.0,
    "tuned_fuzzy_accuracy": 1.0,
    "tuned_fuzzy_precision": 1.0,
    "tuned_fuzzy_recall": 1.0,
    "tuned_fuzzy_f1": 1.0,
    "tuned_win_loss_ratio": 0.0,
    "base_win_loss_ratio": 0.0
  },
  "status": "COMPLETED",
  "predictions": [
    {
      "input": "woof",
      "target": "dog",
      "test_output": "dog",
      "base_output": "dog"
    },
    {
      "input": "meow",
      "target": "cat",
      "test_output": "cat",
      "base_output": "cat"
    }
  ]
}
```

The eval output makes it easy to compare model versions overall, and to see exactly where the differences are, so you know exactly where to focus to improve your workflow.

Happy classifying!

