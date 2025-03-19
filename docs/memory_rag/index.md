# Memory RAG

Memory RAG is a simple approach that boosts LLM accuracy from ~50% to 90-95% compared to GPT-4. It creates contextual embeddings that capture meaning and relationships, allowing smaller models to achieve high accuracy without complex RAG setups or fine-tuning overhead.

## Quick Start with Python or REST API

First, make sure your API key is set (get yours at [app.lamini.ai](https://app.lamini.ai)):

=== "Terminal"
    ```sh
    export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
    ```

=== "Python SDK"
    ```py
    import lamini
    import os

    lamini.api_key = os.environ["LAMINI_API_KEY"]
    ```

To use Memory RAG, build an index by uploading documents and selecting a base open-source LLM. This is the model you'll use to query over your documents.

=== "Python SDK"
    Initialize the Memory RAG client:

    ```py

    from lamini import MemoryRAG

    client = MemoryRAG("meta-llama/Llama-3.1-8B-Instruct")
    ```

    Find a PDF file to embed:
    ```py
    lamini_wikipedia_page_pdf = ("https://huggingface.co/datasets/lamini/"
                                "lamini-wikipedia-page/blob/main/"
                                "Lamini-wikipedia-page.pdf")
    ```

    Download the PDF file:
    ```python
    import requests
    import os

    # Download the PDF file
    response = requests.get(lamini_wikipedia_page_pdf)

    # Save locally
    pdf_path = "lamini_wikipedia.pdf"
    with open(pdf_path, "wb") as f:
        f.write(response.content)

    ```

    Embed and build the Memory RAG Index:
    ```py
    response = client.memory_index(documents=[pdf_path])
    ```

    Expected `response`:
    ```json
    {'job_id': 1, 'status': 'CREATED'}
    ```

=== "REST API"

    ```sh

    curl --location 'https://huggingface.co/datasets/lamini/lamini-wikipedia-page/resolve/main/Lamini-wikipedia-page.pdf' --output lamini_wikipedia.pdf

    curl --location 'https://api.lamini.ai/alpha/memory-rag/train' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --form 'files=@"lamini_wikipedia.pdf"' \
        --form 'model_name="meta-llama/Llama-3.1-8B-Instruct"'
    ```

    Expected response:
    ```json
    {"job_id":1,"status":"CREATED"}
    ```

Next, Memory embedding and indexing will complete. Poll for status:

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
            "job_id": 1
        }'
    ```

Finally, run the Memory RAG model:

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
            "job_id": 1,
            "rag_query_size": 3,
            "model_name": "meta-llama/Llama-3.1-8B-Instruct"
        }'
    ```

    If it's not yet ready, you'll get this response:
    ```json
    {"detail":"Trained memory rag model 15505 status is not COMPLETED, current status: CREATED."}
    ```

## Iteration

You are now ready to run evaluation of this model. To do so, build out an evaluation set that consists of Question/Answer pairs for the expected answers you have for the
provided question. The more representative your questions and answer pairs are to your production use case, the better the model is evaluated. Rate the models performance
in reference to this evaluation set. If the model performs poorly, try iterating on the Memory Rag job with additional data. If the model performs well enough, then you
can consider it ready for production!
