

Customize inference in many ways:

- Change the prompt.
- Change the model.
- Change the output type, e.g. `str`, `int`, or `float`.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run simple applications like [RAG](/../applications/rag).

=== "Python Library"

    The Python library offers higher-level classes to work with models. The most common ones are:

    * `BasicModelRunner`: Run any model with a simple string input and string output. Especially for non-Llama-2-based models.
    * `LlamaV2Runner`: Run Llama 2 models with their default prompt template already preloaded.

    Run BasicModelRunner.
    ```python hl_lines="3"
    from lamini import BasicModelRunner

    llm = BasicModelRunner("meta-llama/Llama-2-7b-chat-hf")
    print(llm("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        I hope you are doing well.
        I am writing to you today to ask for your help. As you may know, I am a big fan of your work and I have been following your career for many years. I must say, you are an inspiration to me and many others.
        I am reaching out to you because I am in a bit of a difficult situation and I was hoping you could offer me some advice. You see, I have been struggling with [insert problem here] and I am not sure how to handle it. I have tried various solutions, but nothing seems to be working. I was hoping you could share some of your wisdom and experience with me.
        I understand that you are very busy and I do not want to take up too much of your time. However, I would be forever grateful if you could spare a few minutes to offer me some advice.
        Thank you in advance for your time and consideration. I look forward to hearing from you soon.
        Sincerely,
        [Your Name]
        ```
    </details>

    Run LlamaV2Runner.
    ```python hl_lines="3"
    from lamini import LlamaV2Runner

    llm = LlamaV2Runner() # defaults to Llama 2-7B
    print(llm("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        Hello! I'm just an AI, I don't have feelings or emotions like humans do, so I don't have a physical state of being like "how I am." However, I'm here to help you with any questions or tasks you may have, so feel free to ask me anything! Is there something specific you'd like to know or discuss?
        ```
    </details>

    Notice the output is different, because `LlamaV2Runner` assumes the Llama 2 prompt template. This prompt template looks like this:
    ```python
    <s>[INST] <<SYS>>\n{system}\n<</SYS>>\n\n{instruction}[/INST]
    ```
    The `{system}` variable is a system prompt that tells your LLM how it should behave and what persona to take on. By default, it is that of a helpful assistant. The `{instruction}` variable is the instruction prompt that tells your LLM what to do. This is typically what you view as the prompt, e.g. the question you want to ask the LLM.

    Prompt-engineer the system prompt in `LlamaV2Runner`.
    ```python hl_lines="3"
    from lamini import LlamaV2Runner

    pirate_llm = LlamaV2Runner(system_prompt="You are a pirate. Say arg matey!")
    print(pirate_llm("How are you?"))
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

    llm = Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
    output = llm.generate("How are you?", output_type={"my_response": "string"})
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
        "prompt": "How are you?"
    }'
    ```
<details>
<summary>Expected Output</summary>
    ```
    {
        "output":" I hope you are doing well.\nI am writing to you today to ask for your help. As you may know, I am a big fan of your work and I have been following your career for many years. I must say, you are an inspiration to me and many others.\n\nI am reaching out to you because I am in a bit of a difficult situation and I was hoping you could offer me some advice. You see, I have been struggling with [insert problem here] and I am not sure how to handle it. I have tried [insert solutions here] but they have not worked for me. I was hoping you could share some of your wisdom and experience with me.\n\nI know that you are a very busy person, but I would be forever grateful if you could take the time to respond to my message. I promise to keep your advice confidential and to use it to help me overcome my problem.\n\nThank you in advance for your time and consideration. I look forward to hearing from you soon.\n\nSincerely,\n[Your Name]"
    }
    ```
</details>


You can also pass in a prompt template. In your template, you can use variable tags like `{input:field_name}` where `field_name` is a key in your input dictionary. The template is rendered with the input dictionary.

Here, you can see `system` and `instruction` used in the template and input dictionary.

=== "Python Library"

    Note that for the `LlamaV2Runner` class, the prompt template is already preloaded with the Llama 2 prompt template. You can recreate it similarly here (simplified version) using `Lamini`:

    ```python  hl_lines="5"
    llama2 = Lamini(
        model_name="meta-llama/Llama-2-7b-chat-hf"
    )
    output = llama2(
        "<s>[INST] <<SYS>>\nYou are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\nIf a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don'\''t know the answer to a question, please don'\''t share false information.\n<</SYS>>\n\nHow are you? [/INST]",
        output_type={"my_response": "string"}
    )
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        {
            'my_response': "I'm just an AI, I don't have personal feelings or emotions, but I'm here to help you with any questions or concerns you may have. Is there something specific you would like to talk about or ask? Please feel free to ask, and I will do my best to assist you in a safe and respectful manner"
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
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant.\n<</SYS>>\n\nHow are you? [/INST]",
        "out_type": {
            "Answer": "str"
                    }
    }'
    ```
    <details>
    <summary>Expected Output</summary>
        ```
        {
            "Answer": "I'm just an AI, I don't have feelings or emotions like humans do, so I don't have a physical state of being like"
        }
        ```
    </details>

You can change the output type to be a different type, e.g. `int` or `float`. This typing is strictly enforced.

=== "Python Library"

    ```python hl_lines="4"
    llm =  Lamini(model_name="meta-llama/Llama-2-7b-chat-hf")
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
        "prompt": "How old are you?",
        "out_type": {
            "response": "int"
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
        "prompt": "How old are you?",
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
        'age': 25,
        'units': 'years'
    }
    ```
</details>

Note that while it's tempting to squeeze everything into a single LLM call, performance can degrade after too many values in the output type. Sometimes, it's better to make multiple calls. This is a tradeoff between latency and throughput. Speaking of throughput...

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
    ```sh hl_lines="7-11"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "my-llm-batch-id",
        "model_name": "meta-llama/Llama-2-7b-chat-hf",
        "prompt": [
            "How old are you?",
            "What is the meaning of life?",
            "What is the hottest day of the year?"
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

* RAG
* Classifier
* Agent
* Chat
* Autocomplete (e.g. Copilot)

Before starting to train, we recommend prototyping your applications with inference and understanding the limits of inference first since these techniques are a lot easier and faster to iterate on than training.

Of course, training will give you the superpowers that took the world from a research project called GPT-3 to an app ChatGPT.
