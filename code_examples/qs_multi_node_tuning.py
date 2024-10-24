import lamini

data = [
    {
        "input": f"{[i for _ in range(100)]}",
        "output": f"{[i for _ in range(100)]}",
    }
    for i in range(100)
]

model_name = "hf-internal-testing/tiny-random-MistralForCausalLM"

API_URL = "https://api.lamini.ai"
API_KEY = "<YOUR API KEY ON https://app.lamini.ai>"
llm = lamini.Lamini(model_name=model_name, api_url=API_URL, api_key=API_KEY)

result = llm.train(
    data_or_dataset_id=data,
    finetune_args={"max_steps": 100, "index_method": "IndexFlatL2"},
    # Distributed training running on 2 nodes, each node has 1 GPU.
    # In practice, you'll instead go with 2 GPUs on 1 node, as the network
    # connection between the 2 GPUs are faster.
    # This is for demonstration.
    gpu_config={"nodes": 2, "gpus": 1},
)
