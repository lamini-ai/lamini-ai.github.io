import lamini
# lamini.api_key = "<YOUR-LAMINI-API-KEY>"

llm = lamini.Lamini("meta-llama/Meta-Llama-3.1-8B-Instruct")
print(llm.generate("How are you?", output_type={"Response":"str"}))
