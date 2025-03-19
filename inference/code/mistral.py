from lamini import Lamini

llm = Lamini(model_name="mistralai/Mistral-7B-Instruct-v0.3")
print(llm.generate("<s>[INST] How are you? [/INST]", output_type={"Response": "str"}))
