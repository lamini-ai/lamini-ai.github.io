# GCP GKE Setup

## Prerequisites

Here are Pre-requistics:

- A GPU machine with a minimum of 40 GB of GPU memory. For GCP, we recommend using the a2-highgpu machine types, such as a2-highgpu-8g. For reference, [GCP GPU machine types](https://cloud.google.com/compute/docs/gpus).

- A high-performance network drive, such as Network File System (NFS), is recommended for storing models, datasets, and fine-tuned parameters to enable sharing across different pods. On GCP, we recommend using [FileStore NFS](https://cloud.google.com/filestore?hl=en).

## Setup

- Install gcloud CLI

Install the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install).

```bash
# Install the Google Cloud SDK
./google-cloud-sdk/install.sh
```

Modify profile to update your $PATH and enable shell command completion?
Do you want to continue (Y/n)? Y

Enter a path to an rc file to update, or leave blank to use
/Users/{userName}/.bash_profile: /Users/{userName}/.bash_profile

Start a new shell for the changes to take effect.

Run gcloud init to initialize the SDK

```bash
# Initialize the Google Cloud SDK
gcloud init
```

- Install GKE plugins

Install the kubectl if not installed. Example:

```bash
gcloud components install gke-gcloud-auth-plugin
```

Follow the instructions here to install the [GKE plugins](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)

```bash
# Install the GKE authentication plugin for kubectl
gcloud components install gke-gcloud-auth-plugin
```

```bash
# Install the GKE authentication plugin (if not already installed)
gcloud components install gke-gcloud-auth-plugin
```

## Setup GKE Cluster

- Create a K8s cluster, example:

```bash
# Create a GKE cluster with NVIDIA L4 GPUs and specified configurations
gcloud container clusters create l4-gpu-cluster \
   --zone=us-west4-c \
   --machine-type=g2-standard-96 \
   --accelerator=type=nvidia-l4,count=8 \
   --enable-gvnic \
   --enable-image-streaming \
   --enable-shielded-nodes \
   --shielded-secure-boot \
   --shielded-integrity-monitoring \
   --enable-autoscaling \
   --num-nodes=1 \
   --min-nodes=0 \
   --max-nodes=3 \
   --cluster-version=1.32.3-gke.1440000 \
   --node-locations=us-west4-c
```

- Verify the installation

```bash
# Verify the GKE cluster nodes are running
kubectl get nodes
```

## Setup the NFS

- Enable the Google Cloud FileStore

```bash
# Enable the Google Cloud FileStore API
gcloud services enable file.googleapis.com
```

- Create the FileStore, example:

```bash
# Create a FileStore instance with 1TB capacity
gcloud filestore instances create nfs-share \
   --zone=us-west4-c \
   --tier=BASIC_HDD \
   --file-share=name="share1",capacity=1TB \
   --network=name="default"
```

- Install NFS provisioner

```bash
# Add and update the NFS provisioner Helm repository
helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
helm repo update
```

- Create the Storage Class, example:

```bash
# Install the NFS provisioner with specified configurations
helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
   --set nfs.server=10.217.139.170 \
   --set nfs.path=/share1 \
   --set storageClass.name=nfs-client
```

- Create the PVC

```yaml
# Example: filestore-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: lamini-volume
  annotations:
    volume.beta.kubernetes.io/storage-class: nfs-client
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: nfs-client
  resources:
    requests:
      storage: 200Gi
```

```bash
# Apply the FileStore PVC configuration
kubectl -n lamini apply -f filestore-pvc.yaml
```

- Verify the installation

```bash
# Verify the PVC was created successfully
kubectl -n lamini get pvc
```

## Install Lamini

Follow this [link](https://github.com/lamini-ai/lamini-platform/blob/main/deployments/kube-installer/INSTALL.md) to install the Lamini.

It is highly recommended to start the Lamini installation with the following bare minimal requirements before adding and making any custom requirements and changes.

- Update configs/helm-config.yaml for minimal resources

```bash
inference.offline = 1   
training.worker.num_pods = 1
training.worker.resources.gpu.request = 1
```
- Enable local database, persistent-lamini/values.yaml

Uncomment the followings:

```bash
folder-creation:
  storage:
    pvc_name: lamini-volume # must be identical to the pvc_name in database
```

```bash
database:
  enabled: true
  storage:
    pvc_name: lamini-volume  # must be identical to the pvc_name in folder-creation
```

- Generate the Helm charts for Lamini

```bash
# Generate Helm charts for Lamini deployment
./generate_helm_charts.sh
```

- Install the Persistent Lamini

```bash
# Install the persistent Lamini components
NAMESPACE=lamini
helm install persistent-lamini ./persistent-lamini --namespace ${NAMESPACE} --create-namespace --debug
```

- Install the Lamini

```bash
# Install the main Lamini components
helm install lamini ./lamini --namespace ${NAMESPACE} --create-namespace --debug
```

- Port forwarding the service

```bash
# Forward the API service port to localhost
kubectl -n lamini port-forward svc/api 8000:8000
```

- Verify the Lamini Frontend.

Open the [http://localhost:8000](http://localhost:8000)

The Lamini portal should open and display corrctly.

- Verify the tuning

Create a new tuning job with the Tiny Random Mistral model and Llama 3.1 model, under the Tune tab in the Lamini portal. The jobs should finish with the `completed` status.

- Verify the inference

Run a simple inference test. The inference should return a prompt response without any errors or timeout.

```python
import lamini
import random
lamini.api_url = "http://localhost:8000"
lamini.api_key = "test_token"
model_name = "hf-internal-testing/tiny-random-MistralForCausalLM"
llm = lamini.Lamini(model_name=model_name)
prompt = f"Generate a random number between 0 and {random.random()}"
print(llm.generate(prompt=prompt))
```

Replace `hf-internal-testing/tiny-random-MistralForCausalLM` with `meta-llama/Llama-3.1-8B-Instruct`, and try again.


