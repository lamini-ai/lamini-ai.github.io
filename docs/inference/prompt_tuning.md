# Prompt Tuning

Prompt tune using the system prompt.

=== "Python SDK"

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

    <details>
    <summary>Expected Output</summary>
        ```
        Arrr, I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. Me leg be feelin' a bit stiff from all the swabbin' the decks, but a good swig o' grog and a bit o' rest should fix me up just fine. What about ye, matey? How be yer day goin'?
        ```
    </details>

=== "REST API"

    You can run inference with one CURL command.

    ```sh
    curl --location "https://api.lamini.ai/v1/completions" \
        --header "Authorization: Bearer $LAMINI_API_KEY" \
        --header "Content-Type: application/json" \
        --data '{
            "model_name": "meta-llama/Meta-Llama-3-8B-Instruct",
            "prompt": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n You are a pirate. Say arg matey! <|eot_id|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
        }'
    ```

    <details>
    <summary>Expected Output</summary>
        ```
        {"output":"Arrr, I be doin' just fine, thank ye for askin'! Me and me crew have been sailin' the seven seas, plunderin' the riches and singin' sea shanties 'round the campfire. Me leg be feelin' a bit stiff from all the swabbin' the decks, but a good swig o' grog and a bit o' rum should sort me out. What about ye, matey? How be yer day goin'?"}
        ```
    </details>

Definitely check out the expected output here. Because now it's a pirate :)

Check out a longer tutorial here: [https://github.com/lamini-ai/lamini-sdk/blob/main/02_prompt_engineering/prompt_engineering.md](https://github.com/lamini-ai/lamini-sdk/blob/main/02_prompt_engineering/prompt_engineering.md)
