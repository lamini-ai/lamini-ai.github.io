import lamini
lamini.api_key = "<YOUR-LAMINI-API-TOKEN>"

llm = lamini.Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
print(llm.generate("How are you?", output_type={"Response":"str"}))
