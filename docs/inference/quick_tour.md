Customize inference in many ways:

- Change the prompt.
- Change the model.
- Change the output type, e.g. `str`, `int`, or `float`.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run simple applications like [RAG](/../applications/rag).

=== "Python SDK"

    The Python SDK offers higher-level class, `Lamini`, to work with models.

    Run Lamini with Llama 3.
    ```python hl_lines="3"
    from lamini import Lamini

    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct')
    print(llm.generate("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        I'm doing well, thank you for asking! I'm a large language model, so I don't have feelings or emotions like humans do, but I'm functioning properly and ready to assist you with any questions or tasks you may have. It's great to be able to help and provide information to users like you! How about you? How's your day going?
        ```
    </details>

    Run Lamini with Mistral.
    ```python hl_lines="3"
    from lamini import Lamini

    llm = Lamini(model_name='mistralai/Mistral-7B-Instruct-v0.2')
    print(llm.generate("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        I'm doing well, thank you for asking again! I'm here to help answer any questions or provide information you might have. How can I assist you today? Let me know if you have any specific topic or query in mind.
        ```
    </details>

    Notice the output is different, because Llama 3 assumes the Llama 3 prompt template. This prompt template looks like this:
    ```python
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>

    {{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>

    {{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
    ```
    The `{system}` variable is a system prompt that tells your LLM how it should behave and what persona to take on. By default, it is that of a helpful assistant. The `{instruction}` variable is the instruction prompt that tells your LLM what to do. This is typically what you view as the prompt, e.g. the question you want to ask the LLM.

    Prompt-engineer the system prompt in `Lamini`.
    ```python hl_lines="3"
    from lamini import Lamini

    prompt = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
    prompt += "You are a pirate. Say arg matey!"
    prompt += "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
    prompt += "How are you?"
    prompt += "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    print(llm.generate(prompt))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        ARGH matey! *adjusts eye patch* I be doin' grand, thank ye for askin'! The sea be callin' me name, and me heart be yearnin' fer the next great adventure. *winks* What be bringin' ye to these fair waters? Maybe we can share a pint o' grog and swap tales o' the high seas? *grin*
        ```
    </details>

    Definitely check out the expected output here. Because now it's a pirate :)

    Let's go lower-level. The [`Lamini` class](/../lamini_python_class/__init__) is the base class for all runners. `Lamini` wraps our [REST API endpoint](/../rest_api/completions).

    `Lamini` expects a string or list of strings as input and a return dictionary for the output type. The simplest one you'll see here is returning a string.

    ```python
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    print(llm.generate("How are you?", output_type={"answer": "str"}))
    ```

=== "REST API"

    You can run inference with one CURL command.

    Full reference docs on the REST API are [here](/../rest_api/completions.md).

    ```sh
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": "How are you?"
        "output_type": {
            "answer": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'answer': "I'm doing well, thanks for asking! How about you"
    }
    ```
</details>

You can also pass in a prompt template. In your template, you can use variable tags like `{input:field_name}` where `field_name` is a key in your input dictionary. The template is rendered with the input dictionary.

Here, you can see `system` and `instruction` used in the template and input dictionary.

=== "Python SDK"

    ```python  hl_lines="5"
    llama3_header = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
    llama3_middle = "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
    llama3_footer = "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"

    class PromptTemplate:

    @staticmethod
    def get_llama3_prompt(user_prompt, system_prompt=" "):
        return llama3_header + system_prompt + llama3_middle + user_prompt + llama3_footer
    ```

    ```python  hl_lines="5"
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    system_prompt = "You are a pirate. Say arg matey!"
    user_prompt = "How are you?"
    output_type={"answer": "str"}
    print(llm.generate(PromptTemplate.get_llama3_prompt(user_prompt, system_prompt, output_type)))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        {
            "answer": "Arrr, I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. Me leg be feelin' a bit stiff from all the swabbin' the decks, but a good swig o' grog and a bit o' rest should fix me up just fine. What about ye, matey? How be yer day goin'?"
        }
        ```
    </details>

=== "REST API"

    The input dictionary is passed in through `prompt` as part of the request.

    ```sh hl_lines="6"
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
            "prompt": ["<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n You are a pirate. Say arg matey! <|eot_id|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"]
        }'
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        {
            "answer": "Arrr, I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. Me leg be feelin' a bit stiff from all the swabbin' the decks, but a good swig o' grog and a bit o' rest should fix me up just fine. What about ye, matey? How be yer day goin'?"
        }
        ```
    </details>

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

=== "Python SDK"

    ```python hl_lines="4"
    llm =  Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
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
            "answer": "int"
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

    ```python hl_lines="2-6"
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

    ```sh hl_lines="7-11"

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
            'response': 'I am 27 years old ',
            'explanation': 'I am 27 years old because I was born on January 1, 1994'
        },
        {
            'response': "The meaning of life is to find purpose, happiness, and fulfillment. It is to live a life that is true to oneself and to contribute to the greater good. It is to find joy in the simple things and to pursue one's passions with dedication and perseverance. It is to love and be loved, to laugh and cry, and to leave a lasting impact on the world ",
            'explanation': "The meaning of life is a complex and deeply personal question that has puzzled philosophers and theologians for centuries. There is no one definitive answer, as it depends on an individual's beliefs, values, and experiences. However, some common themes that many people find give meaning to their lives include:"
        },
        {
            'response': 'The hottest day of the year in Los Angeles is typically around July 22nd, with an average high temperature of 88°F (31°C). ',
            'explanation': 'The hottest day of the year in Los Angeles is usually caused by a high-pressure system that brings hot air from the deserts to the coast. This can lead to temperatures reaching as high as 100°F (38°C) on some days, but the average high temperature is around 88°F (31°C).'
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
