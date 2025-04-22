Lamini also supports streaming inference! Here is an example implementation using our Python library.

```python
import os
import random
import time

import lamini

api = lamini.StreamingCompletion()


"""
If you want to use the async version, you can do the following:

async def main():
    prompt = f"What is AI?"
    result = await api.async_create(
        prompt,
        "meta-llama/Llama-3.2-3B-Instruct",
        max_new_tokens=256,
    )

    async for r in result:
        print(r)

"""

def main():
    prompt = f"What is AI?"
    result = api.create(
        prompt,
        "meta-llama/Llama-3.2-3B-Instruct",
        max_new_tokens=256,
    )

    for r in result:
        print(r)
main()
```
