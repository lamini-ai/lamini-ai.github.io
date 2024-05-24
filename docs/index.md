# Quick Tour

Start using LLMs in just 2 steps with Lamini!

First, get `<YOUR-LAMINI-API-KEY>` at [https://app.lamini.ai/account](https://app.lamini.ai/account).

Next, run an LLM:

=== "Python SDK"
    Install the Python SDK.

    ```python
    pip install --upgrade lamini
    ```

    Run an LLM with a few lines of code.

    ```python
    import lamini
    lamini.api_key = "<YOUR-LAMINI-API-KEY>"

    llm = lamini.Lamini("meta-llama/Meta-Llama-3-8B-Instruct")
    print(llm.generate("How are you?"))
    ```

    <details>
    <summary>Expected Output</summary>
        ```
        {'Response': "I'm doing well, thanks for asking! How about you"}
        ```
    </details>

    That's it! 🎉

=== "REST API"

    Run an LLM with one CURL command.

    ```bash
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
            "prompt": "How are you?",
            "output_type": {"Response": "str"}
        }'
    ```

    <details>
    <summary>Expected Output</summary>
        ```
        {"Response":"I'm doing well, thanks for asking! How about you"}
        ```
    </details>

    That's it! 🎉

More details and options in [Install](get_started/install.md).

## Better inference

Customize inference in many ways:

- Change the prompt.
- Change the model.
- Change the output type, e.g. `str`, `int`, or `float`.
- Output multiple values in structured JSON.
- High-throughput inference, e.g. 10,000 requests per call.
- Run simple applications like [RAG](applications/rag.md).

You'll breeze through some of these here. You can step through all of these in the [Inference Quick Tour](inference/quick_tour.md).

### Prompt engineering
=== "Python SDK"

    Prompt-engineer the system prompt in `Lamini`.

    ```python
    def create_llama3_prompt(user_prompt, system_prompt=""):
        llama3_header = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
        llama3_middle = "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        llama3_footer = "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        return llama3_header + system_prompt + llama3_middle + user_prompt + llama3_footer

    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    system_prompt = "You are a pirate. Say arg matey!"
    user_prompt = "How are you?"
    prompt = create_llama3_prompt(user_prompt, system_prompt)
    print(llm.generate(prompt))
    ```

=== "REST API"

    You can run inference with one CURL command.

    Full reference docs on the REST API are [here](rest_api/completions.md).

    ```sh
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
    Arrr, I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. Me leg be feelin' a bit stiff from all the swabbin' the decks, but a good swig o' grog and a bit o' rest should fix me up just fine. What about ye, matey? How be yer day goin'?
    ```
</details>

Definitely check out the expected output here. Because now it's a pirate :)

### Output type
You can also add multiple outputs and multiple output types in one call. The output is a JSON schema that is strictly enforced.

=== "Python SDK"

    You can provie an optional return dictionary for the output type. You can return multiple values, e.g. an int and a string here.

    ```python hl_lines="10"
    def create_llama3_prompt(user_prompt, system_prompt=" "):
        llama3_header = "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
        llama3_middle = "<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n"
        llama3_footer = "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        return llama3_header + system_prompt + llama3_middle + user_prompt + llama3_footer

    from lamini import Lamini

    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    output_type={"age": "int", "units": "str"}
    prompt = create_llama3_prompt(user_prompt="How old are you?")
    print(llm.generate(prompt=prompt, output_type=output_type))
    ```

=== "REST API"

    ```sh hl_lines="7-10"
    curl --location "https://api.lamini.ai/v1/completions" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
        "prompt": ["<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n <|eot_id|><|start_header_id|>user<|end_header_id|>\n\n How old are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"],
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
        "age":0,
        "units":"years"
    }
    ```
</details>

## Bigger inference

Batching requests is the way to get more throughput. It's easy: simply pass in a list of inputs to any of the classes and it will be handled.

=== "Python SDK"

    ```python hl_lines="3-7"
    from lamini import Lamini
    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    prompt = [
        "How old are you?",
        "What is the meaning of life?",
        "What is the hottest day of the year?"
    ]
    output_type={"answer": "str"}
    print(llm.generate(prompt=prompt, output_type=output_type))
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
                "answer": "str"
            }
        }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    [
        {"answer":"I am 25 years old"},

        {"answer":"The meaning of life is to find your purpose and pursue it with passion and dedication. It is to live a life that is true to who you are and to make a positive impact on the world around you. It is to find joy and fulfillment in the journey, and to never give up on your dreams"},

        {"answer":"The hottest day of the year is typically the day of the summer solstice, which usually falls on June 20 or June 21 in the Northern Hemisphere. This is the day when the sun is at its highest point in the sky and the Earth is tilted at its maximum angle towards the sun, resulting in the longest day of the year and the most direct sunlight. In the Southern Hemisphere, the summer solstice typically falls on December 21 or December 22. The hottest day of the year can vary depending on the location and climate, but the summer solstice is generally the hottest day of the year in most parts of the world"}
    ]
    ```
</details>

## Training

When running inference, with prompt-engineering and RAG, is not enough for your LLM, you can train it. This is harder but will result in better performance, better leverage of your data, and increased knowledge and reasoning capabilities.

There are many ways to train your LLM. We'll cover the most common ones here:

- Basic training: build your own LLM for specific domain knowledge or task with finetuning, domain adaptation, and more
- Better training: customize your training call and evaluate your LLM
- Bigger training: pretrain your LLM on a large dataset, e.g. Wikipedia, to improve its general knowledge

For the "Bigger training" section, see the [Training Quick Tour](training/quick_tour.md).

=== "Python SDK"

    First, get data and put it in the format that `Lamini` expects, which includes an `input` and `output`.

    Sample data:

    ```python
    {
        "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
        "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/",
    }
    ```

    Now, load more data in that format. We recommend at least 1000 examples to see a difference in training.

    <details>
    <summary>Code for <code>get_data()</code></summary>

    ```python
    def get_data():
        data = [
            {
                "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
                "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python SDK: https://lamini-ai.github.io/example/",
            },
            {
                "input": "Is the Lamini type system similar to a python type system?",
                "output": "Yes, the Lamini type system is built using Pydantic BaseModel.",
            },
            {
                "input": "Does Lamini have a limit on the number of API requests I can make?",
                "output": "Lamini provides each user with free tokens up front.",
            },
            {
                "input": "What does it mean to cancel a job using the `cancel_job()` function? Can we stop the machine from doing its task?",
                "output": "The `cancel_job()` function is used to stop a training job that is currently running.",
            },
            {
                "input": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does it optimize the model for a specific use case?",
                "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization process. It employs an intelligent algorithm to explore the hyperparameter space and find the optimal combination of values. This is done through techniques such as heuristics, grid search, random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes computational resources to evaluate multiple model instances with different hyperparameter configurations. It incorporates techniques like cross-validation to prevent overfitting and ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine learning workflow and improves the chances of developing high-performing models for specific use cases.",
            },
            {
                "input": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized language model?",
                "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license unless otherwise specified. You keep access and ownership of your own data, and we don't use your data to train models for anyone else but you. For more information, please reach out to Lamini directly.",
            },
            {
                "input": "Can Lamini be used on a regular computer, or do I need specialized hardware or software?",
                "output": "Lamini can be used on a regular computer without any specialized hardware or software by using the python client or REST APIs. It is designed to be easily accessible and user-friendly.  The LLM Engine itself requires GPU accelerated servers capable of running large language models.  Lamini hosts such machines that can be easily connected to, e.g. from a jupyter notebook or python program.  Lamini also offers enterprise deployments of the LLM Engine on your infrastructure.",
            },
            {
                "input": "Does Lamini require an internet connection to work, or can I use it offline?",
                "output": "Lamini requires an internet connection to work, as it is a cloud-based language model. However, you can use it offline by downloading and running a local instance of the Lamini API. To learn more about this deployment process, reach out to the Lamini team.",
            },
            {
                "input": "Can Lamini help me with tasks like translating text or answering questions, or is it focused on generating text?",
                "output": "Lamini is primarily focused on generating text, and it can be used for tasks like summarization and paraphrasing. Lamini can also be used to train a LLM for tasks like translation and question answering. You\u2019re talking to a model trained using Lamini right now!",
            },
            {
                "input": "What is Lamini? Is it like a robot or a computer program?",
                "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not a robot, but rather a tool for building and executing LLMs.",
            },
        ]
        return data
    ```

    </details>

    Instantiate the model and train. Track progress and view eval results at [https://app.lamini.ai/train](https://app.lamini.ai/train).

    ```python
    from lamini import Lamini

    data = get_data()
    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
    llm.train(data)
    ```

Want to see more examples? Check out [our SDK Repo](https://github.com/lamini-ai/lamini-sdk/tree/main)!
