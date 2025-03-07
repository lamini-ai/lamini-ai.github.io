# Inference Quick Start

Even faster inference is here! Try out our new [OpenAI-compatible inference API](../inference/infv2.md) 🚀.

Let's try running inference with a Llama model. First, make sure you have your API key (get yours at [https://app.lamini.ai/account](https://app.lamini.ai/account)).

## Run inference on a Llama model

=== "Python SDK"
    Initialize the Lamini client:
    ```py
    import lamini
    lamini.api_key = "<YOUR-LAMINI-API-KEY>"

    llm = lamini.Lamini("meta-llama/Llama-3.2-3B-Instruct")
    ```

    Create a prompt using the Llama template:
    ```py
    prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n"
    prompt += "Which animal remembers facts the best?\n"
    prompt += "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    ```

    Generate a response:
    ```py
    response = llm.generate(prompt)
    print(response)
    ```

=== "REST API"
    ```sh
    curl --location 'https://api.lamini.ai/v1/completions' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
            "model_name": "meta-llama/Llama-3.2-3B-Instruct",
            "prompt": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\nWhich animal remembers facts the best?\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        }'
    ```

<details>
  <summary>Example Response</summary>

    ```json
    While animals are known for their impressive memory abilities, the answer to this question can vary depending on the species and the type of facts they're trying to remember. Here are some examples:

    **Top contenders:**

    1. **Chimpanzees**: Our closest living relatives in the animal kingdom, chimpanzees have been shown to possess exceptional memory abilities. They can recall:
            *Complex social hierarchies and relationships
            * Tool use and usage
            *Food sources and locations
            * Even human faces and emotions
    2. **Dolphins**: These intelligent marine mammals have been observed:
            *Recognizing and remembering individual humans and other dolphins
            * Learning and recalling complex vocalizations and songs
            * Solving problems and adapting to new situations
    3. **Elephants**: With their large brains and complex social structures, elephants have impressive memory abilities, including:
            *Remembering migration routes and watering holes
            * Recognizing and responding to family members and social hierarchies
            * Displaying empathy and cooperation
    4. **Crows and Ravens**: These intelligent birds are known for their problem-solving abilities and memory:
            *Remembering and using tools to obtain food
            * Recognizing individual humans and other animals
            * Solving complex puzzles and learning from experience

    **Honorable mentions:**

    * **Parrots**: Some parrot species, like African Greys, are renowned for their exceptional vocal mimicry and memory abilities.
    * **Honeybees**: These social insects have impressive memory for:
            + Nectar sources and food locations
            + Social hierarchies and communication
            + Navigation and migration routes
    * **Octopuses**: These cephalopods have been observed:
            + Solving complex problems and learning from experience
            + Remembering and recognizing individual humans and other octopuses

    **The winner?**

    While it's difficult to declare a single winner, chimpanzees are often considered one of the top contenders for remembering facts the best. Their advanced cognitive abilities, social complexity, and adaptability make them a strong candidate for exceptional memory.

    However, it's essential to remember (pun intended) that each species has its unique strengths and weaknesses, and the concept of "remembering facts" can be subjective. The best way to understand an animal's memory abilities is to study their behavior, social structures, and cognitive processes in their natural habitats.
    ```
</details>

## Using System Prompts

You can also use system prompts to guide the model's behavior:

=== "Python SDK"
    ```py
    # Add a system prompt for more control
    prompt = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n"
    prompt += "You are a concise assistant who gives brief, direct answers.\n"
    prompt += "<|eot_id|><|start_header_id|>user<|end_header_id|>\n"
    prompt += "Which animal remembers facts the best?\n"
    prompt += "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

    response = llm.generate(prompt)
    print(response)
    ```

=== "REST API"
    ```sh
    curl --location 'https://api.lamini.ai/v1/completions' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
            "model_name": "meta-llama/Llama-3.2-3B-Instruct",
            "prompt": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a concise assistant who gives brief, direct answers.\n<|eot_id|><|start_header_id|>user<|end_header_id|>\nWhich animal remembers facts the best?\n<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
        }'
    ```

<details>
  <summary>Example Response</summary>

    ```json
    Elephants.
    ```

</details>

Remember that different models use different prompt templates. Check out our [prompt templates guide](../inference/prompt_templates.md) to learn more.
