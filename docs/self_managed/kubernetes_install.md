# Installing Lamini Platform on Kubernetes

!!! note
    The Lamini installer is only available when self-managing Lamini Platform. [Contact us](https://www.lamini.ai/contact) to learn more.

Lamini Platform on Kubernetes enables multi-node, multi-GPU inference and training running on your own GPUs, in the environment of your choice.

## Prerequisites

### Tools

You need to have a working Kubernetes cluster, and [`python`](https://www.python.org/downloads/), [`helm`](https://helm.sh/docs/intro/install/), [`kubectl`](https://kubernetes.io/docs/tasks/tools/) installed.

### Lamini Self-Managed license

[Contact us](https://www.lamini.ai/contact) for access to the Kubernetes installer to host Lamini Platform on your own GPUs or in your cloud VPC.

### Hardware system requirements

- 64 GB CPU memory
- 1 TB disk
- GPU memory: 2xHBM per GPU

  - Example: AMD MI250 has 64GB of HBM, so Lamini requires 128GB of RAM per GPU.
  - Example: AMD MI300 has 192GB HBM, so Lamini requires 384GB of RAM per GPU.

### PVC

   Lamini requires a RWX PVC for storing all runtime data.
   
   You can use NFS and other storage solutions.
   For example, you can set up a simple provisioner using `nfs-subdir-external-provisioner`:

   ```bash
   helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/
   helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner \
       --set nfs.server=<NFS_IP> \
       --set nfs.path=<NFS_SUBFOLDER_PATH>
   ```

   Then proceed to create a PVC `lamini-volume` with `ReadWriteMany` access for installing Lamini Platform.

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

## Installation Steps

### Obtain the installer

Ask your Sales Engineer for the installer.
The installer is a `.tar.gz` compressed file with all helm charts and scripts for installing Lamini Platform.
You should work with your Sales Engineer for each installation or upgrade of Lamini Platform.

You should keep any changes to the installer in a private repository for tracking purposes.
Also ask your Sales Engineer to keep track of such changes.

After obtaining the installer, extract it to a directory of your choice:

```shell
# Make sure the installer name is used for directory name
# so that you can track the version of the installer.
INSTALLER_NAME="<name>"
mkdir -p ${INSTALLER_NAME}
tar -xzf ${INSTALLER_NAME}.tar.gz -C ${INSTALLER_NAME}
```

The rest of the instructions are in the INSTALL.md file in the installer.
You should operate under the directory of the installer.

```shell
# Change to the installer directory
cd ${INSTALLER_NAME}/lamini-kube-installer

# Read the INSTALL.md file, open with your favorite editor
vi INSTALL.md
```

### Update `helm_config.yaml`

1. **Optional**: If you already have `nfssubdir-external-provisioner` installed, set the `pvc_provisioner` to the `storageclass` name of defined by your installed `nfs-subdir-external-provisioner`.

   ```yaml title="helm_config.yaml"
   pvc_provisioner: nfs-client
   ```

1. If you opt to use Lamini Platform provided NFS pvc provisioner, set the `pvcLamini.name` to the name of the PVC you want to use, and set `create` to `True`, and set `size` to the recommended `200Gi`, or work with your Sales Engineer to determine the size:

   ```yaml title="helm_config.yaml"
   pvcLamini: {
      name: lamini-volume,
      size: 200Gi,
      create: True
   }
   ```

   if you have already created a PVC, set `name` to the name of the PVC, set `create` to `False`, you can
   omit `size`:

   ```yaml title="helm_config.yaml"
   pvcLamini: {
      name: lamini-volume,
      create: False
   }
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

   The example above would create 4 pods using 4 GPUs in total. Each pod has 1 GPU. The example shows 1 inference pod allocated to `batch` inference, 1 pod dedicated only to `streaming` inference, 1 dedicated only to `embedding` inference (also used in classification), and 1 for the `catchall` pod, which is intended to handle requests for models that have not been preloaded on the `batch` pod. See [Model Management](model_management.md) for more details.

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

### Generate Helm Charts and install Lamini Platform

Follow the **INSTALL.md** included in the installer for the detailed steps.
The general steps are:

1. Generate Helm charts with the provided shell script
1. Install Lamini Platform with `helm install` or upgrade with `helm upgrade`

## AWS instance tpyes recommendation

We recommend the following AWS instance types for running the Lamini Platform:
- G6 series: Sufficient for running models with fewer than 10B parameters.
- P4 series: Recommended as a general-purpose option.

For specific use cases or requirements, please reach out to us.
