# [Beta] OpenAI-compatible Inference API

Our new OpenAI-compatible inference API is now in beta!

## Quick Start

Remember to get your API key at [https://app.lamini.ai/account](https://app.lamini.ai/account).

Initialize the OpenAI client:

```python
import openai

client = openai.OpenAI(
    api_key="<YOUR-LAMINI-API-KEY>",
    base_url="https://api.lamini.ai/inf",
)
```

Use the [OpenAI API](https://github.com/openai/openai-python) as you normally would.

### Chat Completions

```python
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[{"role": "user", "content": "What is the best llama?"}],
)
print(response)
```

<details>
  <summary>Example Response</summary>

```text
ChatCompletion(id='chatcmpl-a5d61c89c0b64bfcbda823f1205f89ff', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='That\'s a subjective question, as the "best" llama is often a matter of personal preference. Llamas come in a wide range of breeds, each with their unique characteristics, temperaments, and purposes. Here are some popular llama breeds, known for their distinct traits:\n\n1. **Suri Llama**: Known for their long, soft fleece, Suri llamas are prized for their luxurious coat and calm nature.\n2. **Huacaya Llama**: Huacaya llamas have a fluffy, dense coat and are often used as pack animals or for their meat.\n3. **Camelid Combination (Cama)**: Cams are hybrids of llamas and camels, often bred for their unique appearance and temperaments.\n4. **American Llama**: A popular breed in the United States, American llamas are known for their intelligence, friendly nature, and versatility.\n5. **Peruvian Llama**: Peruvian llamas are one of the oldest breeds, known for their sturdy build and high-quality fleece.\n\nWhen choosing the "best" llama, consider factors such as:\n\n* Purpose (pack animal, fiber production, pet, or show)\n* Temperament (calm, friendly, curious, or energetic)\n* Fleece quality (softness, density, and color)\n* Size (standards vary, but most llamas range from 32 to 40 inches tall)\n* Health and breeding\n\nIt\'s essential to research and work with reputable breeders to find a llama that meets your needs and preferences. Remember, every llama has its unique personality, so take the time to get to know one before making a decision.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1741379785, model='hosted_vllm/meta-llama/Llama-3.2-3B-Instruct', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=337, prompt_tokens=41, total_tokens=378, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
```

</details>

### JSON Output

```python
SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
    },
    "required": ["answer"],
}

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[
        {"role": "user", "content": "What is the best llama?"},
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "json_response",
            "schema": SCHEMA,
        },
    },
)

print(response)
```

<details>
  <summary>Example Response</summary>

```text
ChatCompletion(id='meta-llama/Llama-3.2-3B-Instruct-20364893-cbd0-45af-84ff-b4f51a7864fd', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='{"answer" : "It is difficult to pinpoint the \'best\' llama as they can vary in temperament, purpose, and physical characteristics. However, some popular and well-known breeds of llamas include:* Suri llamas: Known for their stunning, silky fleece and slender build, suri llamas are popular for their beauty and are often used for fiber production.* Huacaya llamas: With their fluffy, soft coats and medium build, huacaya llamas are prized for their fiber and are often used for wool production.* Suri Angora llamas: A cross between a suri and an Angora rabbit, Suri Angora llamas inherit the rabbit\'s Angora fiber, which is highly prized for its softness and warmth.* Pacaya-Llama: A rare and unique breed, Pacaya-Llamas are known for their striking appearance, intelligence, and friendly temperament.Each llama is an individual with its unique characteristics, and what one person considers the \'best\' may not be the same for another. Ultimately, the \'best\' llama is one that is well-suited to its purpose and lifestyle. It\'s recommended to research and find a llama that meets your specific needs and preferences."}', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[], reasoning_content=None), stop_reason=None)], created=1745873448, model='meta-llama/Llama-3.2-3B-Instruct', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=250, prompt_tokens=42, total_tokens=292, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
```

</details>

### With Additional Parameters

```python
response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[{"role": "user", "content": "What is the best llama?"}],
    temperature=0.5,
    max_tokens=100,
)
print(response)
```

<details>
  <summary>Example Response</summary>

```text
ChatCompletion(id='chatcmpl-e4b07deb82264bb28fb786b67769538b', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='There is no single "best" llama, as they are all unique individuals with their own characteristics, temperaments, and purposes. However, I can provide some information on popular llama breeds and their characteristics.\n\nHere are a few popular llama breeds:\n\n1. **Suri Llama**: Known for their long, silky coats, Suri llamas are often used as pack animals and are prized for their intelligence, gentle nature, and versatility.\n2. **Huacaya Llama**: Huacaya', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1741380397, model='hosted_vllm/meta-llama/Llama-3.2-3B-Instruct', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=100, prompt_tokens=41, total_tokens=141, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
```

</details>

### Caching

Inference requests to hosted models are not cached.

For third-party models, inference requests are cached for 60 seconds and can be overridden by passing an `extra_body` parameter with the request.

```python
response = client.chat.completions.create(
    model="gpt-4o-mini", # third-party model
    messages=[{"role": "user", "content": "What is the best llama?"}],
    temperature=0.5,
    max_tokens=100,
    extra_body = {
        "cache": {
          "ttl": 600 # seconds, caches response for 10 minutes
      }
    }
)
print(response)
```

## Get available models

Get the list of available models for OpenAI-compatible inference.

```bash
curl -X GET "https://api.lamini.ai/inf/models" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR-LAMINI-API-KEY>"
```
