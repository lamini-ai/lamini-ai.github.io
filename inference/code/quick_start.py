import lamini

# lamini.api_key = "<YOUR-LAMINI-API-KEY>"

llm = lamini.Lamini("meta-llama/Meta-Llama-3.1-8B-Instruct")
print(
    llm.generate(
        """<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nHow are you?<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"""
    )
)
