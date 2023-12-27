Customize inference in many ways:

- Change the prompt.
- Change the model.
- Change the output type, e.g. `str`, `int`, or `float`.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run simple applications like [RAG](/../applications/rag).

=== "Python Library"

    The Python library offers higher-level classes to work with models. The most common ones are:

    * `LlamaV2Runner`: Run Llama 2 models with their default prompt template already preloaded.
    * `MistralRunner`: Run Mistral models with their default prompt template already preloaded.

    Let's take a look at how to use one of these.

    ```python hl_lines="3"
    from lamini import LlamaV2Runner

    llm_runner = LlamaV2Runner() # defaults to Llama 2-7B
    print(llm_runner.call("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        Hello! I'm just an AI, I don't have feelings or emotions like humans do, so I don't have a physical state of being like "how I am." However, I'm here to help you with any questions or tasks you may have, so feel free to ask me anything! Is there something specific you'd like to know or discuss?
        ```
    </details>

    Notice the output is different, because `LlamaV2Runner` assumes the Llama 2 prompt template. This prompt template looks like this:
    ```python
    <s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{user}[/INST]
    ```
    The `{system}` variable is a system prompt that tells your LLM how it should behave and what persona to take on. By default, it is that of a helpful assistant. The `{user}` variable is the instruction prompt that tells your LLM what to do. This is typically what you view as the prompt, e.g. the question you want to ask the LLM.

    Prompt-engineer the system prompt in `LlamaV2Runner`.
    ```python hl_lines="3"
    from lamini import LlamaV2Runner

    pirate_llm_runner = LlamaV2Runner(system_prompt="You are a pirate. Say arg matey!")
    print(pirate_llm_runner.call("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        ARGH matey! *adjusts eye patch* I be doin' grand, thank ye for askin'! The sea be callin' me name, and me heart be yearnin' fer the next great adventure. *winks* What be bringin' ye to these fair waters? Maybe we can share a pint o' grog and swap tales o' the high seas? *grin*
        ```
    </details>

    Definitely check out the expected output here. Because now it's a pirate :)

    Let's go lower-level. The [`Lamini` class](/../lamini_python_class/__init__) is the base class for all runners. `Lamini` wraps our [REST API endpoint](/../rest_api/completions).

    `Lamini` expects a dictionary as input and a return dictionary for the output type. The simplest one you'll see here is returning a string.

    Note that while runners use a `.call(prompt)` method, `Lamini` uses `.generate(prompt)`.

    ```python
    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
    output = llm.generate("How are you?")
    ```

=== "REST API"

    You can run inference with one CURL command.

    Full reference docs on the REST API are [here](/../rest_api/completions.md).

    ```sh
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]"
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        "output":" I'm good, thanks. How about you?"
    }
    ``` 
</details>

Here, you can see `system` and `instruction` used in the template and input dictionary.

=== "Python Library"

    !!! note

        In the `LlamaV2Runner` class, the prompt template is already preloaded with the Llama 2 prompt template. You can recreate it similarly here (simplified version) using `Lamini`:

    ```python  hl_lines="4 8 9"
    llm = Lamini(
        model_name="meta-llama/Llama-2-7b-chat-hf",
    )
    output = llm.generate(
        prompt="<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow are you? [/INST]",
    )
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        {
            'output': "  Hello! *smiling* I'm just an AI, I don't have feelings like humans do, but I'm here to help you in any way I can! Is there something specific you need assistance with or would you like to chat?"
        }
        ```
    </details>

=== "REST API"

    The prompt is passed in through `prompt` as part of the request.

    ```sh hl_lines="6"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow are you? [/INST]"
    }'
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        {
            "output":"  Hello! *adjusts glasses* I'm feeling quite well, thank you for asking! It's always a pleasure to assist you. How may I be of service today? Is there something specific you need help with?"
        }
        ```
    </details>

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

=== "Python Library"

    ```python hl_lines="3"
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
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you in years? [/INST]",
        "out_type": {
            "age": "int"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'age': 25
    }
    ```
</details>

And you can add multiple output types in one call. The output is a JSON schema that is also strictly enforced.

=== "Python Library"

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
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
        "out_type": {
            "age": "int",
            "units": "str"
        }
    }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    {
        'age': 27,
        'units': 'years'
    }
    ```
</details>

!!! note

    While it's tempting to squeeze everything into a single LLM call, performance can degrade after too many values in the output type due. Sometimes, it's better to make multiple calls. This is a tradeoff between latency and throughput. Speaking of throughput...

You just ran inference many times. What's next?

## Bigger inference

Batching requests is the way to get more throughput. It's easy: simply pass in a list of inputs to any of the classes and it will be handled.

You can send up to 10,000 requests per call - on the Pro and Organization tiers. Up to 1000 on the Free tier.

=== "Python Library"

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

    ```sh hl_lines="6-10"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": [
            "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow old are you? [/INST]",
            "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nWhat is the meaning of life? [/INST]",
            "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nWhat is the hottest day of the year? [/INST]"
        ],
        "out_type": {
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
            "response":"I'm just an AI, I don't have a physical body or age, so I don't have a specific age. I'm here to help you with any questions or tasks you may have, so feel free to ask me anything ",
            "explanation":"I'm just an AI, I don't have a physical body or age, so I don't have a specific age. I'm here to help you with any questions or tasks you may have, so feel free to ask me anything"
        },
        {
            "response":"The meaning of life is a question that has puzzled philosophers and theologians for centuries. There are many different perspectives on this question, and there is no one definitive answer. However, some common themes that people often identify as giving meaning to life include: ",
            "explanation":"Relationships: Many people believe that the connections and relationships we have with others, whether they be romantic, familial, or friendship, give life meaning. This can include the love and support we receive from others, as well as the positive impact we have on their lives.
        },
        {
            "response":"The hottest day of the year in most places is typically around July or August in the Northern Hemisphere, when the sun is at its highest point in the sky and the Earth is tilted towards the sun. However, the exact date of the hottest day can vary depending on the location and the specific weather patterns in a given year. Some places, such as the deserts of the southwestern United States, can experience their hottest temperatures in June, while others, such as the tropics, may not reach their hottest temperatures until September or ",
            "explanation":"The hottest day of the year is typically around July or August in the Northern Hemisphere, when the sun is at its highest point in the sky and the Earth is tilted towards the sun. However, the exact date of the hottest day can vary depending on the location and the specific weather patterns in a given year. Some places, such as the deserts of the southwestern United States, can experience their hottest temperatures in June, while others, such as the tropics, may not reach their hottest temperatures until September or October. In"
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
