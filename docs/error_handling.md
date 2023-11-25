# Error Handling

Eliminate errors with our comprehensive error handling documentation

## Internal Server 500 error

Internal server errors are errors on our server. These are our problems, so report these! They are usually caused by a misconfigured server, or an issue with the server's resources.

Here are some ways in which you can resolve Internal Server 500 error:

1. Update the lamini python package to the most recent version: Make sure that you are using supported python version. Supported python version are 3.7 to 3.11.

    1. Download the most recent python client from [Lamini python package](https://pypi.org/project/lamini).

    2. You can update your Python version by downloading the latest version from the [Python website](https://www.python.org/downloads/) and running the installer.

    3. Alternatively, you can update Python using a package manager such as Homebrew (for macOS) or apt-get (for Linux)

2. Review the script: This error could arise due to mismatch in defined Type format. Make sure that the input and output types are defined in following format:

```sh
    [user_defined_type_name] : [python_data_type] = Context("")
```

Be sure to include the Context. This helps the LLM understand your types in natural language.
Example:

```python
from llama import Type, Context

class AdAspects(Type):
  tone: str = Context("tone of the marketing copy")
  product_features: list = Context("product features to promote")
  audience: str = Context("target audience for the message")
  subject: str = Context("subject or topic of the message")
  goal: str = Context("goal of this marketing campaign and message")
```

## Timeout error

These errors can occur if a request takes too long to process or if the server is unable to fulfill a request due to internal issues or resource constraints. Resource constraints can occur if the server has too little available memory, disk space, or other resources to process a request. Usually request to lamini api expires after 240 secs.
You can try following solutions:

1. Using PowerML batching interface, you can learn more about it [here](batching.md)

2. If above solution doesn't resolve timeout error then try reruning the program

## Authentication error

Authentication errors occur when a user attempts to access a secured resource but fails to provide the correct credentials. This can occur if the user has entered their credentials incorrectly, if the credentials are out of date, or if the credentials are not authorized to access the resource. Authentication errors can also occur if the authentication system itself has malfunctioned or has been compromised.
You can resolve it by setting correct authentication token. More detailed documentation can be found [here](Start/auth.md)
