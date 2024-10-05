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
