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
from pydantic import BaseModel

class LlamaType(BaseModel):
    name: str
    description: str

response = client.beta.chat.completions.parse(
    model="meta-llama/Llama-3.2-3B-Instruct",
    messages=[{"role": "user", "content": "What is the best llama?"}],
    response_format=LlamaType,
)
print(response)
```

<details>
  <summary>Example Response</summary>

```text
ParsedChatCompletion[LlamaType](id='chatcmpl-fa84117790324edbbe38782f05c05cc1', choices=[ParsedChoice[LlamaType](finish_reason='stop', index=0, logprobs=None, message=ParsedChatCompletionMessage[LlamaType](content='{\n"name": "Suri",\n"description": "Greater size with multiple fleece registration levels,"\n\n}', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, parsed=LlamaType(name='Suri', description='Greater size with multiple fleece registration levels,')))], created=1741380276, model='hosted_vllm/meta-llama/Llama-3.2-3B-Instruct', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=27, prompt_tokens=41, total_tokens=68, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
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

By default, the inference requests are cached for 60 seconds. You can override this by passing an `extra_body` parameter with the request.

```python
response2 = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
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
