import argparse
import os

from openai import OpenAI
from transformers.utils.versions import require_version


require_version("openai>=1.5.0", "To fix: pip install openai>=1.5.0")


def parse_args():
    parser = argparse.ArgumentParser(description="python openai_sdk.py --model meta-llama/Llama-3.2-1B " +
                                     "--api-url http://localhost:8000")
    parser.add_argument("--api-url", type=str, help="Base URL for the API endpoint", required=True)
    parser.add_argument("--model", type=str, help="Model name to use for inference", required=True)
    return parser.parse_args()

def main():
    args = parse_args()

    client = OpenAI(
        api_key=f"{os.environ.get('API_KEY', '0')}",
        base_url=f"{args.api_url}/v1",
    )

    result = client.chat.completions.create(
        # model is just a name, actual model name is specified in `examples/inference/llama3_vllm.yaml`
        model=args.model,
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
