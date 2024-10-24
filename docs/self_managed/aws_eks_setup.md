# AWS EKS Installation

!!! note
    The Lamini installer is only available when self-managing Lamini Platform. [Contact us](https://www.lamini.ai/contact) to learn more.

## Summary

This installation covers the steps involved in setting up an AWS EKS cluster, configuring NFS storage, creating a node group, installing the AWS CLI, accessing the EKS cluster, and finally installing the Lamini platform on the EKS cluster.

### Create EKS Cluster

- Search for EKS on AWS console
- Create a new cluster
  - Configure cluster details (name, IAM role, networking)
- Create the cluster

### Set Up NFS

- Create AWS S3 File Gateway
  - Configure gateway settings (name, timezone, instance key pair)
  - Launch gateway instance
- Activate and configure gateway
- Create file share and note the NFS IP and path

### Create Node Group

- Select the created EKS cluster
- Add a node group
  - Create an instance role with necessary policies
  - Configure node group details (name, role, instance type, disk size)
- Create the node group and note the node names

### Install AWS CLI

- Follow AWS instructions to install the AWS CLI
- Verify installation

### Access EKS Cluster

- Create AWS Access Key ID and Secret Access Key
- Configure AWS credentials
- Update kubeconfig for the EKS cluster

### Install Lamini Installer

- Follow the "Installing Lamini Platform on Kubernetes" guide
- Complete Lamini installation on EKS

## Create EKS Cluster

- Type EKS in the AWS search bar of the AWS landing page. Select the EKS.

![screenshot-20241016-125951](../assets/eks.png)

- Click Add Cluster and then Create, to create a cluster.

![screenshot-20241016-124632](../assets/eks_create_cluster.png)

- Enter a cluster name.

![screenshot-20241016-124818](../assets/eks_cluster_name.png)

- Create an IAM role for EKS.

![screenshot-20241016-124818](../assets/eks_iam.png)

- Select the EKS service and check the EKS - Cluster

![screenshot-20241016-125059](../assets/eks_service.png)

- Enter the role name.

![screenshot-20241016-125246](../assets/eks_role_name.png)

- Select networking and specify the default security groups.

![screenshot-20241016-125510](../assets/eks_networking.png)

- Create the EKS cluster.

![screenshot-20241016-125623](../assets/eks_create_cluster_1.png)

- It will show the creating status.

![screenshot-20241016-125721](../assets/eks_status.png)

## Set Up NFS

- Create AWS S3 File Gateway. Type Storage Gateway in the search bar of AWS Console.

![screenshot-20241016-132005](../assets/eks_gateway.png)

- Click on Create gateway.

![screenshot-20241016-132157](../assets/eks_create_gateway.png)

- Enter gateway name and timezone.

![screenshot-20241016-132349](../assets/eks_create_gateway.png)

- Select EC2 as platform option and create the instance key pair.

![screenshot-20241016-132636](../assets/eks_ecs.png)

- Enter the key pair name and create the key pair. Download the pem file to be used for accessing the instance for deployment later.

![screenshot-20241016-132724](../assets/eks_keypair.png)

- Launch the instance.

![screenshot-20241016-132934](../assets/eks_launch_instance.png)

- Connect to AWS - select the IP address connection option and publicly accessible endpoint option.

![screenshot-20241016-133202](../assets/eks_ip.png)

- Activate gateway.

![screenshot-20241016-133259](../assets/eks_activate_gateway.png)

- Configure after activating the gateway.

![screenshot-20241016-133541](../assets/eks_configure.png)

- Create file share.

![screenshot-20241016-133627](../assets/eks_fileshare.png)

- Select the gateway that just created, set NFS protocol, and then create the S3 bucket.

![screenshot-20241016-133734](../assets/eks_nfs_protocol.png)

![screenshot-20241016-133755](../assets/eks_s3.png)

- Select the S3 that was just created.

![screenshot-20241016-133823](../assets/eks_select_s3.png)

- Create the file share.

![screenshot-20241016-133849](../assets/eks_create_fileshare.png)

- Note down the NFS IP and path that will be used in the NFS setup for Lamini installation.

![screenshot-20241016-134042](../assets/eks_ip_path.png)

## Create Node Group

- Select the EKS cluster that was just created.

![screenshot-20241016-140806](../assets/eks_select_cluster.png)

- Select the Compute.

![screenshot-20241016-140901](../assets/eks_compute.png)

- Select Add Node Group.

![screenshot-20241016-140935](../assets/eks_add_nodegroup.png)

- Create an instance role with policy.

![screenshot-20241016-142207](../assets/eks_role.png)

- Select EC2.

![screenshot-20241016-141329](../assets/eks_ec2.png)

- Ensure to select the following policies:
AmazonEC2ContainerRegistryReadOnly
AmazonEKSWorkerNodePolicy
AmazonEKS_CNI_Policy

![screenshot-20241016-141652](../assets/eks_policy.png)

![screenshot-20241016-141712](../assets/eks_policy_1.png)

- Enter a role name and create the role.

![screenshot-20241016-141954](../assets/eks_role_name_1.png)

![screenshot-20241016-141826](../assets/eks_create_role.png)

- Enter the node group name and the role that was created.

![screenshot-20241016-142247](../assets/eks_nodegroup.png)

- Set Amazon Linux 2 GPU Enabled AMI type, select the desired instance type with GPU, typically the G and P types. Set disk size to at least 100 G.

![screenshot-20241016-142340](../assets/eks_ec2_type.png)

- Specify the desired node size.

![screenshot-20241016-142444](../assets/eks_nodegroup_size.png)

- Create the node group.

![screenshot-20241016-142520](../assets/eks_create_nodegroup.png)

- Once the node group has been created, note down the node names that will be used in the lamini installer configuration.

![screenshot-20241016-144133](../assets/eks_nodename.png)

## Install AWS CLI

- Follow the AWS instruction to install the AWS CLI
<https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>

- Check the AWS CLI installation.

```bash
aws --version
```

## Access EKS Cluster

- Create and get the AWS Access Key ID and AWS Secret Access Key.

![screenshot-20241016-145511](../assets/eks_access_key.png)

![screenshot-20241016-145833](../assets/eks_access_key_1.png)

![screenshot-20241016-145852](../assets/eks_access_key_2.png)

![screenshot-20241016-150135](../assets/eks_access_key_3.png)

- Configure AWS credential.

```bash
aws configure
```

![screenshot-20241016-150214](../assets/eks_configure.png)

```bash
aws eks update-kubeconfig --name <eks-cluster-name>
```

![screenshot-20241016-150748](../assets/eks_update_config.png)

## Install Lamini Installer

- Follow the Installing Lamini Platform on Kubernetes section in [Kube installer README.md](https://github.com/lamini-ai/lamini-platform/blob/main/deployments/kube-installer/README.md) to complete the Lamini installation on EKS.
