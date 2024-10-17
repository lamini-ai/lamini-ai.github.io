from lamini import Lamini

llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
data = [
    {
        "input": "What is Lamini? Is it like a robot or a computer program?",
        "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not a robot, but rather a tool for building and executing LLMs.",
    }
]

results = llm.tune(data_or_dataset_id=data, finetune_args={"learning_rate": 1.0e-4})
