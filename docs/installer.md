# Installer 🦙

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
desired application, LLM model (e.g. Llama v2), data volume, and number of users.

Our typical configuration is an LLM Superstation, which is a powerful server
with multiple GPUs that can fully host, finetune, and deploy the largest
models on the Lamini platform.  We have configs that fit into an office or
datacenter.  The Lamini software architecture is based on technologies used
in supercomputers and scales horizontally to the largest systems in the world, e.g.
more than 10,000 GPUs.

However, you can also run the entire Lamini platform on your laptop.  It's a helpful
dev/testing environment, and CPUs can run LLMs with hundreds of millions of parameters
just fine.

## Dependencies ☕️

Lamini is entirely self contained and can run on any machine that can run Docker or OCI containers.  In addition to the operation system, provisioning involves installing Docker, and installing the GPU driver.

### Docker
Install Docker by following [the instructions here](https://docs.docker.com/engine/install/ubuntu/) 🔗.

### Driver
1. Install the GPU driver for the operating system following the manufacturer's instructions.
1. Run system management interface (SMI) tests inside of a GPU enabled docker container to verify the installation.

## Lamini installer 🎁

### LLM Superstation

1. Using the link provided by Lamini (reach out if you have any issues!), get the installer: `$ wget -O lamini-installer.sh '`*`link-to-installer`*`'` .
1. Add execute permissions: `$ chmod +x lamini-installer.sh` .
1. Run the installer: `$ ./lamini-installer.sh` .

### Kubernetes/etc setup

Docs coming soon!  Reach out to us at [info@lamini.ai](mailto:info@lamini.ai)!

## Start up 🚀
Woo, congrats and welcome to the herd!!

Start Lamini with `$ ./build-lamini-installer/lamini-installer/lamini-up`.
We recommend running this inside a [screen](https://en.wikipedia.org/wiki/GNU_Screen)
or [tmux](https://en.wikipedia.org/wiki/Tmux) for ease of use to be able to
view detailed logs.

You can also run with `$ ./build-lamini-installer/lamini-installer/lamini-up -d`
to start the services as a background daemon process, and view the logs with
`docker logs`

Once running, you can checkout the UI at http://localhost:5001!

## Configuring Lamini

### llama_config.yaml

Most configuration options for the Lamini platform are available in a single
yaml configuration file, which is installed at:
`$ ./build-lamini-installer/lamini-installer/configs/llama_config.yaml`

Some common config values:

1. verbose : Set to true to enable verbose logging
2. powerml : A list of API endpoints.  If you want to run different services on different machines, e.g. in a kubernetes cluster, configure each service's endpoints here.
3. wandb.key : Add your weight and biases key here to get detailed dashboards for your fine tuning experiments.
4. disable_auth : Turn off built in authentication, e.g. if you want to use your own.
5. auth.google_whitelist : Set to your company domain to enable any gmail account with a matching domain to log in.

### docker-compose.yaml

The list of all Lamini services is available in the docker-compose.yaml file
`$ ./build-lamini-installer/lamini-installer/docker-compose.yaml`

Some common config values:

1. USE_HTTPS : enable or disable HTTPS (e.g. for external facing services or internal development)
2. volumes.slurm-volume: where do you want fine-tuned models to be stored (they are saved in pytorch format)

