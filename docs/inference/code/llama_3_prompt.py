from lamini import Lamini

prompt = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
prompt += "You are a pirate. Say arg matey!"
prompt += "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
prompt += "How are you?"
prompt += "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
llm = Lamini("meta-llama/Meta-Llama-3.1-8B-Instruct")
print(llm.generate(prompt, output_type={"Response": "str"}))
