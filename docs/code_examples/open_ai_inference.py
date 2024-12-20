import json
import os
from typing import Sequence

from openai import OpenAI
from transformers.utils.versions import require_version


require_version("openai>=1.5.0", "To fix: pip install openai>=1.5.0")

def main():
    client = OpenAI(
        api_key="{}".format(os.environ.get("API_KEY", "0")),
        base_url="http://localhost:{}/v1".format(os.environ.get("API_PORT", 8000)),
    )

    result = client.chat.completions.create(
        # model is just a name, actual model name is specified in `examples/inference/llama3_vllm.yaml`
        model="test",
        # messages[0] is system prompt, messages[2] is user prompt
        messages=[
            {"role": "system", "content": "You are an expert assistant that answers questions succinctly."},
            {"role": "user", "content": "What is the capital of the Iceland? "},
        ],
    )    

    print("FULL RESULT")
    print(result)
    print("RESULT")    
    result = result.choices[0].message.content
    print(result)    


if __name__ == "__main__":
    main()
