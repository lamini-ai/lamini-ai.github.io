# Memory RAG

Memory RAG is a novel approach to Retrieval-Augmented Generation (RAG) that leverages test-time compute during the indexing phase to create more intelligent, validated data representations. Unlike traditional RAG implementations that struggle with balancing information coverage and context window size, Memory RAG transforms raw data into rich representations that capture both meaning and relationships more effectively. By investing computational power during the indexing phase, Memory RAG creates higher-quality data representations from raw data that lead to more precise information retrieval, reducing retrieval misses and model hallucinations, while requiring smaller context windows. This approach provides a simplified path to achieving higher accuracy in LLM applications without the complexity of advanced RAG techniques, while also offering a natural progression path to Memory Tuning for organizations ready to move towards fine-tuning solutions.

## Quickstart

The first step is to build an index by uploading documents and selecting a base LLM. This should be the model you plan on using to query over your documents.

=== "Python SDK"

    ```py
    
    from lamini import Lamini
    
    client = MemoryRAG("meta-llama/Meta-Llama-3.1-8B-Instruct")
    response = client.memory_index(documents=["path/to/document.pdf"])
    job_id = response['job_id']
    ```

=== "REST API"

    ```sh hl_lines="6"

    curl --location 'https://api.lamini.ai/alpha/memory-rag/train' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --form 'files=@"{path/to/document}.pdf"' \
        --form 'model_name="meta-llama/Meta-Llama-3.1-8B-Instruct"'
    ```

Next, wait for training to complete by polling for status.

=== "Python SDK"

    ```py

    from lamini import Lamini
    
    client = MemoryRAG("meta-llama/Meta-Llama-3.1-8B-Instruct")
    status = client.status(job_id)
    ```

=== "REST API"

    ```sh hl_lines="6"

    curl --location 'https://api.lamini.ai/alpha/memory-rag/status' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
            "job_id": 1,
        }'
    ```

Finally, query the model.

=== "Python SDK"

    ```py

    from lamini import Lamini
    
    client = MemoryRAG("meta-llama/Meta-Llama-3.1-8B-Instruct")
    response = client.query("<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n")
    ```

=== "REST API"

    ```sh hl_lines="6"

    curl --location 'https://api.lamini.ai/alpha/memory-rag/completions' \
        --header 'Authorization: Bearer $LAMINI_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
            "prompt": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n How are you? <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
            "job_id": 1
        }'
    ```