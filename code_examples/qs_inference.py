from lamini import Lamini

llm = Lamini("meta-llama/Llama-3.2-3B-Instruct")

print(
    llm.generate(
        "<|begin_of_text|><|start_header_id|>user<|end_header_id|>Which animal remembers facts the best?<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    )
)

from lamini import Lamini
