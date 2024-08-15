# Installing Lamini Platform on Kubernetes

Lamini Platform on Kubernetes enables multi-node, multi-GPU inference and training. Looking for Docker installation instead? [See here](../enterprise_install.md).

## Prerequisites

### Lamini Enterprise access

[Contact us](https://www.lamini.ai/contact) for access to the Kubernetes installer to host Lamini Platform on your own GPUs or in your cloud VPC.
 
### NFS Provisioner
   Lamini requires a RWX NFS provisioner. For example, you can set up a simple provisioner using `nfs-subdir-external-provisioner`:

   ```bash
   helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
   helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner \
       --set nfs.server=<NFS_IP> \
       --set nfs.path=<NFS_SUBFOLDER_PATH>
   ```

### GPU Operator
   - For AMD:
     ```bash
     git clone https://github.com/ROCm/k8s-device-plugin.git
     kubectl create -f k8s-device-plugin/k8s-ds-amdgpu-dp.yaml
     ```
   - For NVIDIA:
     ```bash
     helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
       && helm repo update
     helm install --wait --generate-name \
       -n gpu-operator --create-namespace \
       nvidia/gpu-operator
     ```

### Docker

   We recommend using [Docker](https://docs.docker.com/engine/install/) to generate the Helm charts as described below.

   Make sure to switch to a user with sufficient RBAC privieges to deploy the Helm charts in the Kubernetes cluster. Typically that's root (`sudo su`).

## Installation Steps

### 1. Update `helm_config.yaml`

1. Set the `name` of the PVC provisioner being used for the Lamini cluster. If the PVC has been created beforehand, ensure the `name` is correct, that it is in the `lamini` namespace, and set `create` to `False`:
   ```yaml title="helm_config.yaml"
   pvcLamini: {
      name: lamini-volume, 
      size: 200Gi,
      create: True
   }
   ```
   We recommend at least >200Gi (and the more, the better!) for `lamini-volume`. Base models, trained weights, and datasets will all be stored on this volume.

1. Update the PVC provisioner classname by changing the `nfs_provisioner` field.
```yaml title="helm_config.yaml"
nfs_provisioner: nfs-client
```

1. Confirm the top-level platform `type` (one of: `amd`, `nvidia`, or `cpu`) matches your hardware.
```yaml title="helm_config.yaml"
type: "amd"
```

1. Update the distribution of inference pods. 
   ```yaml title="helm_config.yaml"
   inference: {
      type: ClusterIP, 
      batch: 1,
      streaming: 1,
      embedding: 1,
      catchall: 1
   }
   ```
   The example above would create 4 pods using 4 GPUs in total. Each pod has 1 GPU. The example shows 1 inference pod allocated to `batch` inference, 1 pod dedicated only to `streaming` inference, 1 dedicated only to `embedding` inference (also used in classification), and 1 for the `catchall` pod, which is intended to handle requests for models that have not been preloaded on the `batch` pod. See [Model Management](../model_management) for more details.

1. Update the number of training pods and number of GPUs per pod:
   ```yaml title="helm_config.yaml"
   training: { 
      type: ClusterIP, 
      num_pods: 1, 
      num_gpus_per_pod: 8 
   }
   ```
   We recommend minimizing the number of pods per node. For example, instead of 2 pods with 4 GPUs, it's better to create 1 pod with all 8 GPUs.

1. Update the node affinity for the Lamini deployment. These are the nodes where Lamini pods will be deployed:
   ```yaml title="helm_config.yaml"
   nodes: [
      "node0"
   ]
   ```

1. (Optional) If you want to use a custom ingress pathway, update the `ingress` field:
   ```yaml title="helm_config.yaml"
   ingress: 'ingress/pathway'
   ```

### 2. Generate and Deploy Helm Charts

The Lamini Platform Kubernetes deployment consists of 2 Helm charts:

- `lamini`: Most Lamini services. Will be upgraded when updating to a new version of Lamini Platform.
- `persistent-lamini`: Components that are meant to be persistent and unchanging across Lamini Platform upgrades. These include the Lamini database, PVC, and the Kubernetes secret to download new Lamini images.

#### First time install

   Run  `./install.sh` - This takes helm_config.yaml and dynamically creates the Helm charts to deploy `lamini` & `persistent-lamini`.

#### Upgrade

   Run `./upgrade.sh` - This recreates the Helm charts and redeploys `lamini` without touching `persistent-lamini`.

That's it! You're up and running with Lamini Platform on Kubernetes.