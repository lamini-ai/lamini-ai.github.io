from lamini import Lamini

llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
dataset_id = llm.upload_file("test.jsonl", input_key="user", output_key="answer")

llm.tune(data_or_dataset_id=dataset_id)
