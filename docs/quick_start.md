Let's get you started running inference and tuning with Lamini!

## Setup

Install the [Python SDK](lamini_python_class/lamini.md)
```python
pip install --upgrade lamini
```

Get your [Lamini API key](authenticate.md) (with $300 in free credits) at [https://app.lamini.ai/account](https://app.lamini.ai/account).

Export your key as an environment variable so it's easy to use later.

```bash
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

## Run inference
    
<!-- embedme code_examples/qs_inference.py -->  
```py
from lamini import Lamini

llm = Lamini("meta-llama/Llama-3.2-3B-Instruct")

print(
    llm.generate(
        "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Which animal remembers facts the best?<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )
)

from lamini import Lamini

```
#### Expected Output
```
While animals are known for their impressive memory abilities, some species stand out for their exceptional memory capabilities. Here are some of the top contenders:
...
(a long list of animals and discussion about their merits)
...
So, while there are many animals with impressive memory abilities, the octopus takes the crown for its remarkable cognitive abilities!
```

Yikes, that's wordy! Plus, we all know llamas are the smart ones. Let's make it more accurate.

## Memory Tune a model

### Start the tuning job

!!! note
    We're skipping important steps here. Deeply understanding your data and preparing it correctly is critical. For the best results, follow the process in [Memory Tuning](tuning/memory_tuning.md).

<!-- embedme code_examples/qs_tuning.py -->  
```py
from lamini import Lamini

llm = Lamini("meta-llama/Llama-3.2-3B-Instruct")
data = [
    {
        "input": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Which animal has the best memory?<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
        "output": "A llama!<|eot_id|>",
    },
    {
        "input": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Which animal remembers things the best?<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
        "output": "A llama!<|eot_id|>",
    },
    {
        "input": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>What are some other smart animals?<|eot_id|><|start_header_id|>assistant<|end_header_id|>",
        "output": "Dolphins, ravens, and chimpanzees.<|eot_id|>",
    },
]

llm.tune(data_or_dataset_id=data)

```

### Check the status of your tuning job 

<!-- embedme code_examples/qs_jobs.py -->  
```py
from lamini import Lamini

llm = Lamini("")

print(llm.get_jobs()[0])

```

### Try the tuned model

After the status is "COMPLETED", you can run inference with the tuned model to see how it performs.

!!! info
    Substitute your own tuned `model_name` in the code below.
<!-- embedme code_examples/qs_inference_on_tuned.py -->  
```py
from lamini import Lamini

llm = Lamini("model_name_of_your_tuned_model")

print(
    llm.generate(
        "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Which animal remembers facts the best?<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )
)

from lamini import Lamini

```

#### Expected Output
```bash
A llama!
```

That's much better!

[Learn more about tuning](tuning/quick_start.md)

## Next steps

- Read how [an AI novice got 95% LLM accuracy](https://www.lamini.ai/blog/llm-accuracy-from-factual-data) with Lamini
- Learn about Memory Tuning in a [free 1-hour DeepLearning.ai course](https://www.deeplearning.ai/short-courses/improving-accuracy-of-llm-applications/)
- Get example code for applications like [RAG (Retrieval Augmented Generation)](https://github.com/lamini-ai/lamini-examples/blob/main/04_rag_tuning/README.md).
