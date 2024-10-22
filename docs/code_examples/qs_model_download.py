import random
import string
from lamini import Lamini
from lamini.api.utils.supported_models import ALL as ALL_MODELS

lamini_client = Lamini("meta-llama/Llama-3.2-1B-Instruct")


# You can download the model specified in the Lamini object.
resp = lamini_client.download_model()
print(resp)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = "".join(random.choice(characters) for _ in range(length))
    return random_string


# You can request to download models that are already available.
# The downloader can discover the cached model and update the database records.
for model in ALL_MODELS:
    print(f"Downloading {model=} ...")
    download_resp = lamini_client.download_model(
        model, wait=True, wait_time_seconds=300
    )
    print(f"{model=} {download_resp=}")

    prompt = f"Who are you {generate_random_string(10)}?"
    response = lamini_client.generate(
        # Use random string in prompt to avoid getting cached responses.
        prompt=prompt,
        model_name=model,
    )
    print(f"{model=} {prompt=} {response=}")


# List models and their status on Lamini Platform
models = lamini_client.list_models()
for model in models:
    print(model)
