# Installing Lamini Platform on Docker

Lamini Platform on Docker is available for limited Proof-of-Concept projects, but the only supported production deployment option is [Kubernetes](kubernetes_install.md). Docker deployment only supports single-node inference and training.

## Prerequisites

### Lamini Enterprise access

[Contact us](https://www.lamini.ai/contact) for access to the Docker installer to host Lamini Platform on your own GPUs or in your cloud VPC.

### System requirements
Before getting started, make sure your machine is set up to run Lamini smoothly. Check that your machine has ***at least***:

- 64 GB CPU memory
- 32 GB GPU memory
- 1 TB disk
- Ubuntu 22*

*other linux distros should work as long as they run Docker/OCI

You can run Lamini on your laptop for dev and testing. CPUs can run LLMs with hundreds of millions of parameters (like [`hf-internal-testing/tiny-random-gpt2`](https://huggingface.co/hf-internal-testing/tiny-random-gpt2)) just fine.

### Dependencies

Lamini is entirely self contained and can run on any machine that can run Docker or OCI containers.  In addition to the operating system, provisioning involves installing Docker, and installing the GPU driver.

#### Docker
Install Docker by following [the instructions here](https://docs.docker.com/engine/install/ubuntu/) 🔗.

#### GPU Driver
1. Install the GPU driver for the operating system following the manufacturer's instructions.
    1. Note that the driver version must be compatible with PyTorch: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/).
1. Run system management interface (SMI) tests inside of a GPU enabled docker container to verify the installation.

## Installation

### Docker

1. Using the link provided by Lamini, download the installer: `$ wget -O lamini-installer.sh '`*`link-to-installer`*`'`.
1. Add execute permissions: `$ chmod +x lamini-installer.sh`.
1. Run the installer: `$ ./lamini-installer.sh`.

### Running Lamini
1. Go to the lamini installer directory: `$ cd build-lamini-installer/lamini-installer`
1. Get your Hugging Face Access Token from: https://huggingface.co/settings/tokens
1. Enter the token in the config file, `configs/llama_config_edits.yaml`, under the huggingface token field:
```
huggingface: # This is the Hugging Face API token, it will default to offline mode if no token is provided
    token: ""
```
1. Start Lamini with `$ ./lamini-up`.

Once running, you can view the UI at [http://localhost:5001](http://localhost:5001)!

### Using your local instance
To use your running Lamini instance with the Lamini library, set the API url to your local instance:
```python hl_lines="3-4"
import lamini

lamini.api_url = "http://localhost:5001"
lamini.api_key = "test_token"

llm = lamini.Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")
print(llm.generate("How are you?", output_type={"Response":"str"}))
```


## Configuring Lamini

### llama_config.yaml

Most configuration options for Lamini are available in a single
yaml configuration file, which is installed at:
`$ ./build-lamini-installer/lamini-installer/configs/llama_config.yaml`

Some common config values:

1. `verbose` : Set to true to enable verbose logging
2. `powerml` : A list of API endpoints.  If you want to run different services on different machines, e.g. in a kubernetes cluster, configure each service's endpoints here.

### docker-compose.yaml

The list of all Lamini services is available in the docker-compose.yaml file
`$ ./build-lamini-installer/lamini-installer/docker-compose.yaml`

Some common config values:

1. `volumes.slurm-volume`: where do you want fine-tuned models to be stored (they are saved in pytorch format)
