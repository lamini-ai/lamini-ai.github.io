Customize inference in many ways:

- Change the prompt.
- Change the model.
- Change the output type, e.g. `str`, `int`, or `float`.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run simple applications like [RAG](/../applications/rag).


## Run Lamini with Llama 3
=== "Python SDK"

    The Python SDK offers higher-level class, `Lamini`, to work with models.
    ```python hl_lines="3"
    from lamini import Lamini

    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
    print(llm.generate("How are you?", output_type={"Response":"str"}))
    ```

=== "REST API"

    You can run inference with one CURL command.

    Full reference docs on the REST API are [here](/../rest_api/completions.md).

    ```sh hl_lines="5"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": "How are you?",
        "output_type": {
            "Response": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'Response': "I'm doing well, thanks for asking! How about you"
    }
    ```
</details>

Since Llama 3 assumes the Llama 3 prompt template, you will need to include it for further prompt tuning. This prompt template looks like this:
```python
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>

{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```
The `{system}` variable is a system prompt that tells your LLM how it should behave and what persona to take on. By default, it is that of a helpful assistant. The `{instruction}` variable is the instruction prompt that tells your LLM what to do. This is typically what you view as the prompt, e.g. the question you want to ask the LLM.

Prompt-engineer the system prompt in `Lamini`.
=== "Python SDK"

    ```python
    from lamini import Lamini

    prompt = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
    prompt += "You are a pirate. Say arg matey!"
    prompt += "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
    prompt += "How are you?"
    prompt += "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    llm = Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
    print(llm.generate(prompt, output_type={"Response":"str"}))
    ```

=== "REST API"

    ```sh hl_lines="6"
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
            "prompt": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n You are a pirate. Say arg matey! <|eot_id|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
            "output_type": {
                "Response": "str"
            }
        }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'Response': "Ahoy, matey! I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. The sun be shinin' bright, the wind be blowin' strong, and me trusty cutlass be by me side. What more could a pirate ask for, eh? Arrr"
    }
    ```
</details>

Definitely check out the expected output here. Because now it's a pirate :)

## Run Lamini with Mistral
=== "Python SDK"

    ```python hl_lines="3"
    from lamini import Lamini

    llm = Lamini(model_name='mistralai/Mistral-7B-Instruct-v0.2')
    print(llm.generate("How are you?", output_type={"Response":"str"}))
    ```

=== "REST API"

    ```sh hl_lines="5"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "mistralai/Mistral-7B-Instruct-v0.2",
        "prompt": "How are you?",
        "output_type": {
            "Response": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'Response': "I'm just a computer program, I don't have feelings or emotions. I'm here to help answer any questions you might have to the best of my ability"
    }
    ```
</details>

## Output type

`Lamini` expects a string or list of strings as input and a return dictionary for the output type. The simplest one you've seen here is returning a string.

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

=== "Python SDK"

    ```python hl_lines="6"
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    llm.generate(
        "How old are you in years?",
        output_type={"age": "int"}
    )
    ```

=== "REST API"

    ```sh hl_lines="7-9"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": "How old are you?",
        "output_type": {
            "age": "int"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        "age": 25
    }
    ```
</details>

And you can add multiple output types in one call. The output is a JSON schema that is also strictly enforced.

=== "Python SDK"

    ```python hl_lines="3"
    llm.generate(
        "How old are you?",
        output_type={"age": "int", "units": "str"}
    )
    ```

=== "REST API"

    ```sh hl_lines="7-10"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": "How old are you?",
        "output_type": {
            "age": "int",
            "units": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        "age": 25,
        "units": "years"
    }
    ```
</details>

Note that while it's tempting to squeeze everything into a single LLM call, performance can degrade after too many values in the output type. Sometimes, it's better to make multiple calls. This is a tradeoff between latency and throughput. Speaking of throughput...

You just ran inference many times. What's next?

## Bigger inference

Batching requests is the way to get more throughput. It's easy: simply pass in a list of inputs to any of the classes and it will be handled.

=== "Python SDK"

    ```python hl_lines="5-9"
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    llm.generate(
        [
           "How old are you?",
           "What is the meaning of life?",
           "What is the hottest day of the year?",
        ],
        output_type={"response": "str", "explanation": "str"}
    )
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

Great! You submitted a batch inference request. You're well on your way to building a production application that uses high-throughput pipelines of LLMs.

## Applications

See examples of applications in the [Applications](/../applications/rag) section.

- RAG
- Classifier
- Agent
- Chat
- Autocomplete (e.g. Copilot)

Before starting to train, we recommend prototyping your applications with inference and understanding the limits of inference first since these techniques are a lot easier and faster to iterate on than training.

Of course, training will give you the superpowers that took the world from a research project called GPT-3 to an app ChatGPT.
