# Authenticate

Welcome to this easy 2-step auth. Estimated time: 2 minutes.

If you want to host Lamini in your VPC or on prem, check out [enterprise installer instructions](/enterprise_install) 🔗.

## 1. Get your Lamini API key 🔑

Your API key is at [https://app.lamini.ai/account](https://app.lamini.ai/account). If it's your first time, create a free account by logging in.

## 2. Authenticate

=== "Environment Variable"

    Add your key to your environment variables. In your terminal, run:

    ```bash
    export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
    ```

    Put this line in your `~/.bash_profile` or equivalent file, so you don't have to rerun it in a new session. Remember to `source ~/.bash_profile` after you make the change.

    ```bash
    echo "export LAMINI_API_KEY='$LAMINI_API_KEY'" >> ~/.bash_profile
    source ~/.bash_profile
    echo $LAMINI_API_KEY
    ```

=== "Config File"

    You can authenticate by writing the following to a file `~/.lamini/configure.yaml`

    ```sh
    production:
        key: <YOUR-LAMINI-API-KEY>
    ```

=== "Python Client"

    For convenience, you can also authenticate directly in a python environment after importing lamini. It's recommended to use the other two methods.

    ```python
    import lamini
    lamini.api_key = "<YOUR-LAMINI-API-KEY>"
    ```

## Advanced Python setup: VPC or on premise

If you are [running Lamini in your VPC or on prem](/enterprise_install/installer.md), you can change the URL from Lamini's hosted service to your own server URL:

=== "Python script"

    ```python
    config = {
        "production.key": "<YOUR-LAMINI-API-KEY>",
        "production.url" : "<YOUR-SERVER-URL-HERE>"
    }
    ```

    Test that it works:
    ```python
    llm = Lamini(model_name='meta-llama/Meta-Llama-3-8B-Instruct', config=config)
    response = llm.generate("Tell me a story about llamas.")

    print(response)
    ```

=== "In `~/.lamini/configure.yaml`"

    Add the extra `url` field:

    ```sh
    production:
        key: "<YOUR-LAMINI-API-KEY>"
        url: "<YOUR-SERVER-URL-HERE>"
    ```

## Google Colab

Here's a Colab notebook you can use to get started: [Getting Started with Lamini](https://colab.research.google.com/drive/115OJavk4DE51rUKwfCOyWxWa0LguiuEI#scrollTo=lD391Mcv4lGQ)
