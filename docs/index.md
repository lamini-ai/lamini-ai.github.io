# Quick Tour

Start using LLMs in just 2 steps with Lamini!

First, get `<YOUR-LAMINI-API-KEY>` at [https://app.lamini.ai/account](https://app.lamini.ai/account).

Next, run an LLM:

=== "Python Library"
Install the Python library.

    ```python
    pip install --upgrade lamini
    ```

    Run an LLM with a few lines of code.
    ```python
    import lamini

    lamini.api_key = "<YOUR-LAMINI-API-KEY>"

    llm = lamini.LlamaV2Runner()
    print(llm("How are you?"))
    ```
    <details>
    <summary>Expected Output</summary>

        "Hello! I'm just an AI, I don't have feelings or emotions like humans do, but I'm here to help you with any questions or concerns you may have. I'm programmed to provide respectful, safe, and accurate responses, and I will always do my best to help you. Please feel free to ask me anything, and I will do my best to assist you. Is there something specific you would like to know or discuss?"

    </details>

    That's it! 🎉

=== "Bash (REST API)"

    Run an LLM with one CURL command.

    ```bash
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Llama-2-7b-chat-hf",
            "prompt": "<s>[INST] <<SYS>>\nYou are a helpful assistant \n<</SYS>>\n\nWhat is a llama? [/INST]"
        }'
    ```
    <details>
    <summary>Expected Output</summary>

    {
        "output":"  Ah, a llama! *excitedly* A llama is a domesticated mammal that is native to South America. They are members of the camel family and are known for their distinctive long necks, ears, and coats. Llamas are known for their intelligence, gentle nature, and versatility, making them popular as pack animals, companions, and even therapy animals. They are also a popular choice for fiber production, as their wool is soft, warm, and durable. *nods* Is there anything else you would like to know about llamas?"
    }

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

=== "Python Library"

    Prompt-engineer the system prompt in `LlamaV2Runner`.
    ```python hl_lines="3"
    from lamini import LlamaV2Runner

    pirate_llm = LlamaV2Runner(system_prompt="You are a pirate. Say arg matey!")
    print(pirate_llm("How are you?"))
    ```

=== "REST API"

    You can run inference with one CURL command.

    Full reference docs on the REST API are [here](rest_api/completions.md).

    ```sh
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Llama-2-7b-chat-hf",
            "prompt": "<s>[INST] <<SYS>>\nYou are a pirate. Say arg matey!\n<</SYS>>\n\nHow are you? [/INST]"
        }'
    ```

<details>
<summary>Expected Output</summary>
    ```
    ARGH matey! *adjusts eye patch* I be doin' grand, thank ye for askin'! The sea be callin' me name, and me heart be yearnin' fer the next great adventure. *winks* What be bringin' ye to these fair waters? Maybe we can share a pint o' grog and swap tales o' the high seas? *grin*
    ```
</details>

Definitely check out the expected output here. Because now it's a pirate :)

You can also add multiple outputs and multiple output types in one call. The output is a JSON schema that is strictly enforced.

=== "Python Library"

    You can provie an optional return dictionary for the output type. You can return multiple values, e.g. an int and a string here.

    ```python hl_lines="6"
    from lamini import LlamaV2Runner

    llm = LlamaV2Runner()
    llm(
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
        "age":30,
        "units":"years"
    }
    ```
</details>

## Bigger inference

Batching requests is the way to get more throughput. It's easy: simply pass in a list of inputs to any of the classes and it will be handled.

=== "Python Library"

    ```python hl_lines="2-6"

    llm(
        [
            "How old are you?",
            "What is the meaning of life?",
            "What is the hottest day of the year?"
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
            "response":"I'm just an AI, I don't have personal experiences or emotions like humans do. However, I'm here to help you with any questions or tasks you may have. Is there something specific you'd like to know or discuss ",
            "explanation":"I'm just an AI, I don't have personal experiences or emotions like humans do. I'm here to help you with any questions or tasks you may have. Is there something specific you'd like to know or discuss"
        },
        {
            "response":"The meaning of life is to find your gift. The purpose of life is to give it away ",
            "explanation":"The meaning of life is a question that has puzzled philosophers and theologians for centuries. However, as the famous poet and author, Pablo Picasso once said, 'The meaning of life is to find your gift. The purpose of life is to give it away.' This quote highlights the idea that the purpose of life is not just to exist, but to make a positive impact on the world through the unique talents and abilities that each person possesses. By discovering and using our gifts to help others, we can find true fulfillment and purpose in life. This quote also emphasizes the importance of generosity and giving back to the community, as it is through these acts of kindness that we can truly make a difference in the world. Ultimately, the meaning of life is to find your gift, and to use it to make the world a better place"
        },
        {
            "response":"The hottest day of the year is usually around July 21st in the Northern Hemisphere, and January 20th in the Southern Hemisphere. However, the exact date can vary depending on the location and the specific weather patterns in a given year. Some places, such as the deserts of the southwestern United States, can experience their hottest temperatures in June or July, while other places, such as the tropics, may experience their hottest temperatures in April or May. It's important to check local weather forecasts and climate data to determine the hottest day of the year in a particular location ",
            "explanation":"The hottest day of the year is typically around the summer solstice in the Northern Hemisphere, and the winter solstice in the Southern Hemisphere. This is because the Earth's axis is tilted at an angle of about 23.5 degrees, which causes the sun's rays to hit the Northern Hemisphere more directly during the summer months and the Southern Hemisphere during the winter months. As a result, the temperatures in the Northern Hemisphere tend to be warmer than in the Southern Hemisphere during the summer months, and vice versa during the winter months. However, there can be variations in the timing and intensity of the hottest day of the year depending on local weather patterns and climate conditions."
        }
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

=== "Python Library"

    First, get data and put it in the format that `LlamaV2Runner` expects, which includes an `input` and `output`.

    Sample data:

    ```python
    {
        "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
        "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/",
    }
    ```

    Now, load more data in that format. We recommend at least 1000 examples to see a difference in training.

    ```python
    data = get_data()
    ```

    <details>
    <summary>Code for <code>get_data()</code></summary>

    ```python
    def get_data():
        data = [
            {
                "input": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
                "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/",
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

    Next, instantiate the model and train. Track progress and view eval results at [https://app.lamini.ai/train](https://app.lamini.ai/train).

    ```python
    from lamini import LlamaV2Runner

    llm = LlamaV2Runner()
    llm.data = data
    llm.train()
    ```

Want to go deeper? Check out [our SDK Repo](https://github.com/lamini-ai/lamini-sdk/tree/main)!
