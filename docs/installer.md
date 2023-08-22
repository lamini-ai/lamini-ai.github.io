# Installer 🦙

Looking to get an installer and host Lamini on-premises? Reach out to us at info@lamini.ai!

## System requirements 🌾
Before getting started, make sure your machine is set up to run Lamini smoothly. Check that your machine has ***at least***:
- 32 GB memory
- 32 GB GPU memory, e.g. Nvidia A40 or V100
- 1 TB disk
- Ubuntu 22*

*other distros have not been tested

## Dependencies ☕️

### Docker
Install Docker by following [the instructions here](https://docs.docker.com/engine/install/ubuntu/) 🔗.

### Driver
1. [Install the Nvidia driver using Package Manager](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#package-manager) 🔗.
1. Confirm the driver is properly loaded by running `$ nvidia-smi` .
1. Install fabric-manager: `$ sudo apt-get install cuda-drivers-fabricmanager-`*`[NVIDIA-SMI-VERSION]`*` .
1. Starting with `$ sudo apt-get update`, [follow the commands to get Docker and Nvidia to work together](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#setting-up-nvidia-container-toolkit) 🔗.

## Lamini Installer 🎁

1. Using the link provided by Lamini (reach out if you have any issues!), get the installer: `$ wget -O lamini-installer.sh '`*`link-to-installer`*`'` .
1. Add execute permissions: `$ chmod +x lamini-installer.sh` .
1. Run the installer: `$ ./lamini-installer.sh` .

## Start up 🚀
Woo, congrats and welcome to the herd!!

Start Lamini with `$ ./build-lamini-installer/lamini-installer/lamini-up`. We reccomend running this inside a `screen` for ease of use.
