from lamini import Lamini

llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
llm.generate(
    [
        "How old are you?",
        "What is the meaning of life?",
        "What is the hottest day of the year?",
    ],
    output_type={"response": "str", "explanation": "str"},
)
