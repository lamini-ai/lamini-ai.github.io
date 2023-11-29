
Finetuning a model is training it to do a specific task with your data formatted with particular input-output pairs. To do this part right, you need a few things. One, we've set some mdoel defaults to get the model to improve and learn from the data, instead of going off the rails, but you can still control lower-level settings if you want to override them. Second, iterating on the data is critical for success. So knowing how to edit the data after each finetuning job is important. You will be iterating a lot to get to the right model and recipe. Third, you need to know how to evaluate your model to see if it's improving. We've made this easy for you to compare results across models and datasets with a viewer.


=== "Python Library"

    First, get data and put it in the format that `LlamaV2Runner` expects, which includes the `system` prompt, the `user` query, and the expected `output` response.

    Sample data:

    ```python
    {
        "user": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
        "system": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.",
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
                "user": "Are there any step-by-step tutorials or walkthroughs available in the documentation?",
                "system": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.",
                "output": "Yes, there are step-by-step tutorials and walkthroughs available in the documentation section. Here\u2019s an example for using Lamini to get insights into any python library: https://lamini-ai.github.io/example/",
            },
            {
                "user": "Is the Lamini type system similar to a python type system?",
                "output": "Yes, the Lamini type system is built using Pydantic BaseModel.",
            },
            {
                "user": "Does Lamini have a limit on the number of API requests I can make?",
                "output": "Lamini provides each user with free tokens up front.",
            },
            {
                "user": "What does it mean to cancel a job using the `cancel_job()` function? Can we stop the machine from doing its task?",
                "output": "The `cancel_job()` function is used to stop a training job that is currently running.",
            },
            {
                "user": "Can Lamini automatically handle hyperparameter tuning during the customization process? How does it optimize the model for a specific use case?",
                "output": "Lamini is capable of automatically handling hyperparameter tuning during the model customization process. It employs an intelligent algorithm to explore the hyperparameter space and find the optimal combination of values. This is done through techniques such as heuristics, grid search, random search, Bayesian optimization, or genetic algorithms. Lamini efficiently utilizes computational resources to evaluate multiple model instances with different hyperparameter configurations. It incorporates techniques like cross-validation to prevent overfitting and ensure generalization. By automating hyperparameter tuning, Lamini streamlines the machine learning workflow and improves the chances of developing high-performing models for specific use cases.",
            },
            {
                "user": "Can you explain the CC-BY license mentioned? What does it allow me to do with the customized language model?",
                "output": "Lamini allows for commercial use of their LLM technology under a permissive Apache 2.0 license unless otherwise specified. You keep access and ownership of your own data, and we don't use your data to train models for anyone else but you. For more information, please reach out to Lamini directly.",
            },
            {
                "user": "Can Lamini be used on a regular computer, or do I need specialized hardware or software?",
                "output": "Lamini can be used on a regular computer without any specialized hardware or software by using the python client or REST APIs. It is designed to be easily accessible and user-friendly.  The LLM Engine itself requires GPU accelerated servers capable of running large language models.  Lamini hosts such machines that can be easily connected to, e.g. from a jupyter notebook or python program.  Lamini also offers enterprise deployments of the LLM Engine on your infrastructure.",
            },
            {
                "user": "Does Lamini require an internet connection to work, or can I use it offline?",
                "output": "Lamini requires an internet connection to work, as it is a cloud-based language model. However, you can use it offline by downloading and running a local instance of the Lamini API. To learn more about this deployment process, reach out to the Lamini team.",
            },
            {
                "user": "Can Lamini help me with tasks like translating text or answering questions, or is it focused on generating text?",
                "output": "Lamini is primarily focused on generating text, and it can be used for tasks like summarization and paraphrasing. Lamini can also be used to train a LLM for tasks like translation and question answering. You\u2019re talking to a model trained using Lamini right now!",
            },
            {
                "user": "What is Lamini? Is it like a robot or a computer program?",
                "output": "Lamini is a program for the execution of LLMs called a large language model engine. It is not a robot, but rather a tool for building and executing LLMs.",
            },
        ]
        return data
    ```

    </details>

    Next, instantiate the model and load the data into it.

    ```python
    from lamini import LlamaV2Runner
    
    llm = LlamaV2Runner()
    llm.load_data(data)
    ```

    Train the model. Track progress at [https://app.lamini.ai/train](https://app.lamini.ai/train).

    ```python
    llm.train()
    ```

    Evaluate your model after training, which compares results to the base model.
    
    ```python
    llm.evaluate()
    ```

    Let's drop a level lower. We've set some good default hyperparameters for you in LlamaV2Runner, but you can also tune them yourself.

    ```python
    from lamini import Lamini

    data = [
        [{"input": "What's your favorite animal?"}, {"output": "dog"}],
        [{"input": "What's your favorite color?"}, {"output": "blue"}],
    ]
    llm = Lamini(id="example", model_name="meta-llama/Llama-2-7b-chat-hf", prompt_template="{input:input}")
    llm.load_data(data)
    ```

    The data can be any format and just passed into the model via the prompt template showing what's supposed to be the input. The "output" field is read as the desired target output.

    Then, the way to pass in hyperparamters is through the `train` method.
    ```python
    results = llm.train(finetune_args={'learning_rate': 1.0e-4})
    ```

    The `results` dictionary contains a `model_name` that you can then pass in for inference. By default, after training, the new finetuned model is loaded into the `llm` object.

    ```python
    llm("What's your favorite animal?")
    ```

    This will use the finetuned model for inference.


=== "REST API"

    First, add data to your model.

    ```bash
    curl --location "https://api.lamini.ai/v2/lamini/data_pairs" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "my-training-id",
        "data": [
                [{"name": "Larry", "height": 4}, {"speed": 1.0}],
                [{"name": "Cici", "height": 100}, {"speed": 1.2}]
            ]
    }'
    ```

    Using the same `id`, you can then submit a training job ("finetuning") on this model. This will finetune the model on the data you just added.

    ```bash
    curl --location "https://api.lamini.ai/v2/lamini/train" \
    --header "Authorization: Bearer $LAMINI_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
        "id": "my-training-id",
        "model_name": "meta-llama/Llama-2-7b-chat-hf"
    }'
    ```

    See the [REST API docs](../rest_api/train.md) for more details on training, checking the status of the training job, canceling the job, evaluating the model, loading data, and deleting data.

<br><br>