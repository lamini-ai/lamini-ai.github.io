Lamini also supports streaming inference! Here is an example implementation using our Python library.

```python
import os
import random
import time

import lamini

api = lamini.StreamingCompletion()
async def main():
    prompt = f"[INST]{random.random()} What is a pickle? [/INST]"
    result = await api.async_create(
        prompt,
        "meta-llama/Llama-3.2-1B-Instruct",
        max_new_tokens=256,
    )

    async for r in result:
        print(r)

def main():
    prompt = f"What is A?"
    result = api.create(
        prompt,
        "hf-internal-testing/tiny-random-gpt2",
        max_new_tokens=256,
    )

    for r in result:
        print(r)
main()
```
