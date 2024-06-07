# Enterprise Install 🦙

Looking to get an installer and host Lamini on-premise or on a GPU VM in your VPC? Reach out to us at [info@lamini.ai](mailto:info@lamini.ai)!

## System requirements 🌾
Before getting started, make sure your machine is set up to run Lamini smoothly. Check that your machine has ***at least***:

- 64 GB CPU memory
- 32 GB GPU memory
- 1 TB disk
- Ubuntu 22*

*other linux distros should work as long as they run Docker/OCI

Reach out to us at [info@lamini.ai](mailto:info@lamini.ai) for advice on
configuring and purchasing machines capable of running your
desired application, LLM model (e.g. Llama v3), data volume, and number of users.

However, you can also run the entire Lamini platform on your laptop.  It's a helpful
dev/testing environment, and CPUs can run LLMs with hundreds of millions of parameters
just fine.

## Dependencies ☕️

Lamini is entirely self contained and can run on any machine that can run Docker or OCI containers.  In addition to the operation system, provisioning involves installing Docker, and installing the GPU driver.

### Docker
Install Docker by following [the instructions here](https://docs.docker.com/engine/install/ubuntu/) 🔗.

### GPU Driver
1. Install the GPU driver for the operating system following the manufacturer's instructions.
    1. Note that the driver version must be compatible with PyTorch: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/).
1. Run system management interface (SMI) tests inside of a GPU enabled docker container to verify the installation.

## Installation 🎁

### Docker

1. Using the link provided by Lamini (reach out if you have any issues!), get the installer: `$ wget -O lamini-installer.sh '`*`link-to-installer`*`'` .
1. Add execute permissions: `$ chmod +x lamini-installer.sh` .
1. Run the installer: `$ ./lamini-installer.sh` .

### Kubernetes/etc setup

Docs coming soon!  Reach out to us at [info@lamini.ai](mailto:info@lamini.ai)!

## Running Lamini 🚀
Congrats and welcome to the herd!!

Go to the lamini installer directory: `$ cd build-lamini-installer/lamini-installer`

Get your Hugging Face Access Token from: https://huggingface.co/settings/tokens

Enter the token in the config file, `configs/llama_config_edits.yaml`, under the huggingface token field:
```
huggingface: # This is the Hugging Face API token, it will default to offline mode if no token is provided
    token: ""
```
Start Lamini with `$ ./lamini-up`.

Once running, you can checkout the UI at [http://localhost:5001](http://localhost:5001)!

### Using your local instance
To use your running Lamini instance with the Lamini library, set the API url to your local instance:
```python hl_lines="3-4"
import lamini

lamini.api_url = "http://localhost:5001"
lamini.api_key = "test_token"

llm = lamini.Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")
print(llm.generate("How are you?", output_type={"Response":"str"}))
```


## Configuring Lamini

### llama_config.yaml

Most configuration options for the Lamini platform are available in a single
yaml configuration file, which is installed at:
`$ ./build-lamini-installer/lamini-installer/configs/llama_config.yaml`

Some common config values:

1. `verbose` : Set to true to enable verbose logging
2. `powerml` : A list of API endpoints.  If you want to run different services on different machines, e.g. in a kubernetes cluster, configure each service's endpoints here.
3. `disable_auth` : Turn off built in authentication, e.g. if you want to use your own.

### docker-compose.yaml

The list of all Lamini services is available in the docker-compose.yaml file
`$ ./build-lamini-installer/lamini-installer/docker-compose.yaml`

Some common config values:

1. `USE_HTTPS` : enable or disable HTTPS (e.g. for external facing services or internal development)
2. `volumes.slurm-volume`: where do you want fine-tuned models to be stored (they are saved in pytorch format)

<br><br>
