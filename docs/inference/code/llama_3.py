from lamini import Lamini

llm = Lamini(model_name='meta-llama/Meta-Llama-3.1-8B-Instruct')
print(llm.generate("How are you?", output_type={"Response":"str"}))
