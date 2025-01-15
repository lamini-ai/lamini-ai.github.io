# Memory RAG

Memory RAG is a simple approach that boosts LLM accuracy from ~50% to 90-95% compared to GPT-4. It creates contextual embeddings that capture meaning and relationships, allowing smaller models to achieve high accuracy without complex RAG setups or fine-tuning overhead.

## Quickstart

First, make sure your API key is set (get yours at [app.lamini.ai](https://app.lamini.ai)):


```sh
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

To use Memory RAG, build an index by uploading documents and selecting a base open-source LLM. This is the model you'll use to query over your documents.


=== "Python SDK"
    Initialize the MemoryRAG client:

    ```py
    
    from lamini import MemoryRAG

    client = MemoryRAG("meta-llama/Meta-Llama-3.1-8B-Instruct")
    ```

    Define the PDF file to embed:
    ```py
    lamini_wikipedia_page_pdf = "https://huggingface.co/datasets/sudocoder/lamini-wikipedia-page/blob/main/Lamini-wikipedia-page.pdf"
    ```
    
    Embed and build the Memory RAG Index:
    ```py
    response = client.memory_index(documents=[lamini_wikipedia_page_pdf])
    ```

=== "REST API"

    ```sh

    curl --location 'https://api.lamini.ai/alpha/memory-rag/train' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --form 'files="https://huggingface.co/datasets/sudocoder/lamini-wikipedia-page/blob/main/Lamini-wikipedia-page.pdf"' \
        --form 'model_name="meta-llama/Meta-Llama-3.1-8B-Instruct"'
    ```

Next, wait for training to complete by polling for status.

=== "Python SDK"

    ```py
    job_id = response['job_id']

    status = client.status(job_id)
    ```

=== "REST API"

    ```sh

    curl --location 'https://api.lamini.ai/alpha/memory-rag/status' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
            "job_id": 1,
        }'
    ```

Finally, query the model.

=== "Python SDK"
    Create a prompt:
    ```py
    user_prompt = "How is lamini related to llamas?"
    prompt_template = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n {prompt} <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
    prompt = prompt_template.format(prompt=user_prompt)
    ```

    Pass the prompt to the Memory RAG model:
    ```py
    response = client.query(prompt)
    ```

=== "REST API"

    ```sh

    curl --location 'https://api.lamini.ai/alpha/memory-rag/completions' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
            "prompt": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
            "job_id": 1
        }'
    ```