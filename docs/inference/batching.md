Batching inference requests (submitting multiple prompts simultaneously) provides [dramatically higher throughput](https://www.lamini.ai/blog/lamini-inference) compared to submitting each request individually.

### Use cases

- [Memory Tuning](/tuning/memory_tuning) using both evaluation and data-generation agents
- Evaluation agents that enable rapid feedback loops during model development by automatically measuring model performance
- Data-generation agents for expanding tuning and evaluation data sets without tedious manual effort
- Async inference for enriching or updating data in the background

### A better way to batch

Lamini Platform implements approaches similar to iteration-level scheduling and selective batching (as described in [the Orca paper](https://www.usenix.org/system/files/osdi22-yu.pdf)) to deliver significantly higher throughput compared to naive inference batching implementations. 

Naive batching has two major drawbacks:

1. The entire batch blocks on the request that takes the longest to process.
1. A second batch cannot be processed until the first batch is completely processed.

Iteration-level scheduling and selective batching avoid these drawbacks by allocating work across GPUs at the model iteration level, rather than the entire request level.

### Example

Inference batching with Lamini is simple: just pass in a list of inputs—no configuration required.

=== "Python SDK"

    ```py
    # code/batching.py
    ```

=== "REST API"

    ```sh hl_lines="6-10"

    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": [
            "How old are you?",
            "What is the meaning of life?",
            "What is the hottest day of the year?"
        ],
        "output_type": {
            "response": "str",
            "explanation": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    [
        {
            'response': 'I am 25 years old',
            'explanation': "I am a 25-year-old AI assistant, so I don't have a physical body and don't age like humans do"
        },
        {
            'response': "The meaning of life is a question that has puzzled philosophers, scientists, and thinkers for centuries. There is no one definitive answer, as it is a deeply personal and subjective question that can vary greatly from person to person. However, here are some possible answers that have been proposed:\n\n1. The search for happiness: Many people believe that the meaning of life is to find happiness and fulfillment. This can be achieved through personal relationships, career, hobbies, or other activities that bring joy and satisfaction.\n2. The pursuit of knowledge: Others believe that the meaning of life is to learn and understand the world around us. This can be achieved through education, research, and exploration.\n3. The pursuit of purpose: Some people believe that the meaning of life is to find a sense of purpose and direction. This can be achieved through setting goals, pursuing passions, and making a positive impact on the world.\n4. The search for connection: Many people believe that the meaning of life is to connect with others and build meaningful relationships. This can be achieved through communication, empathy, and understanding.\n5. The search for transcendence: Some people believe that the meaning of life is to transcend the physical world and connect with something greater than ourselves. This can be achieved through spirituality, meditation, or other practices that help us connect with a higher power or the universe.\n\nUltimately, the meaning of life is a deeply personal and subjective question that can only be answered by each individual. It is a question that requires self-reflection, introspection, and a willingness to explore and discover one's own values, beliefs, and passions",
            'explanation': "The meaning of life is a question that has puzzled philosophers, scientists, and thinkers for centuries. There is no one definitive answer, as it is a deeply personal and subjective question that can vary greatly from person to person. However, here are some possible answers that have been proposed:\n\n1. The search for happiness: Many people believe that the meaning of life is to find happiness and fulfillment. This can be achieved through personal relationships, career, hobbies, or other activities that bring joy and satisfaction.\n2. The pursuit of knowledge: Others believe that the meaning of life is to learn and understand the world around us. This can be achieved through education, research, and exploration.\n3. The pursuit of purpose: Some people believe that the meaning of life is to find a sense of purpose and direction. This can be achieved through setting goals, pursuing passions, and making a positive impact on the world.\n4. The search for connection: Many people believe that the meaning of life is to connect with others and build meaningful relationships. This can be achieved through communication, empathy, and understanding.\n5. The search for transcendence: Some people believe that the meaning of life is to transcend the physical world and connect with something greater than ourselves. This can be achieved through spirituality, meditation, or other practices that help us connect with a higher power or the universe.\n\nUltimately, the meaning of life is a deeply personal and subjective question that can only be answered by each individual. It is a question that requires self-reflection, introspection, and a willingness to explore and discover one's own values, beliefs, and passions"
        },
        {
            'response': "The hottest day of the year is typically the day of the summer solstice, which is the longest day of the year and usually falls on June 20 or June 21 in the Northern Hemisphere. This day is often referred to as the 'warmest day of the year' or the 'hottest day of the year' because it is the day when the sun is at its highest point in the sky and the Earth is tilted at its maximum angle towards the sun, resulting in the most direct sunlight and the highest temperatures. However, it's worth noting that the hottest day of the year can vary depending on the location and climate. In some regions, the hottest day of the year may occur in July or August, while in others it may occur in September or October",
            'explanation': "The summer solstice is the longest day of the year and typically marks the beginning of summer in the Northern Hemisphere. It is the day when the sun is at its highest point in the sky and the Earth is tilted at its maximum angle towards the sun, resulting in the most direct sunlight and the highest temperatures. This day is often referred to as the 'warmest day of the year' or the 'hottest day of the year' because it is the day when the sun is at its strongest and the Earth is at its warmest. However, it's worth noting that the hottest day of the year can vary depending on the location and climate. In some regions, the hottest day of the year may occur in July or August, while in others it may occur in September or October."
        }
    ]
    ```
</details>
