_# AWS EKS Installation

## Create EKS Cluster

1. Type EKS in the AWS search bar of the AWS landing page. Select the EKS.

![screenshot-20241016-125951](../assets/eks.png)

2. Click Add Cluster and then Create, to create a cluster.

![screenshot-20241016-124632](../assets/eks_create_cluster.png)

3. Enter a cluster name.

![screenshot-20241016-124818](../assets/eks_cluster_name.png)

4. Create an IAM role for EKS.

![screenshot-20241016-124818](../assets/eks_iam.png)

5. Select the EKS service and check the EKS - Cluster

![screenshot-20241016-125059](../assets/eks_service.png)

6. Enter the role name.

![screenshot-20241016-125246](../assets/eks_role_name.png)

7. Select networking and specify the default security groups.

![screenshot-20241016-125510](../assets/eks_networking.png)

8. Create the EKS cluster.

![screenshot-20241016-125623](../assets/eks_create_cluster_1.png)

9. It will show the creating status.

![screenshot-20241016-125721](../assets/eks_status.png)

## Set Up NFS

1. Create AWS S3 File Gateway. Type Storage Gateway in the search bar of AWS Console.

![screenshot-20241016-132005](../assets/eks_gateway.png)

2. Click on Create gateway.

![screenshot-20241016-132157](../assets/eks_create_gateway.png)

3. Enter gateway name and timezone.

![screenshot-20241016-132349](../assets/eks_create_gateway.png)

4. Select EC2 as platform option and create the instance key pair.

![screenshot-20241016-132636](../assets/eks_ecs.png)

5. Enter the key pair name and create the key pair. Download the pem file to be used for accessing the instance for deployment later.

![screenshot-20241016-132724](../assets/eks_keypair.png)

6. Launch the instance.

![screenshot-20241016-132934](../assets/eks_launch_instance.png)

7. Connect to AWS - select the IP address connection option and publicly accessible endpoint option.

![screenshot-20241016-133202](../assets/eks_ip.png)

8. Activate gateway.

![screenshot-20241016-133259](../assets/eks_activate_gateway.png)

9. Configure after activating the gateway.

![screenshot-20241016-133541](../assets/eks_configure.png)

10. Create file share.

![screenshot-20241016-133627](../assets/eks_fileshare.png)

11. Select the gateway that just created, set NFS protocol, and then create the S3 bucket.

![screenshot-20241016-133734](../assets/eks_nfs_protocol.png)

![screenshot-20241016-133755](../assets/eks_s3.png)

12. Select the S3 that was just created.

![screenshot-20241016-133823](../assets/eks_select_s3.png)

13. Create the file share.

![screenshot-20241016-133849](../assets/eks_create_fileshare.png)

14. Note down the NFS IP and path that will be used in the NFS setup for Lamini installation.

![screenshot-20241016-134042](../assets/eks_ip_path.png)

## Create Node Group

1. Select the EKS cluster that was just created.

![screenshot-20241016-140806](../assets/eks_select_cluster.png)

2. Select the Compute.

![screenshot-20241016-140901](../assets/eks_compute.png)

3. Select Add Node Group.

![screenshot-20241016-140935](../assets/eks_add_nodegroup.png)

4. Create an instance role with policy.

![screenshot-20241016-142207](../assets/eks_role.png)

5. Select EC2.

![screenshot-20241016-141329](../assets/eks_ec2.png)

6. Ensure to select the following policies:
AmazonEC2ContainerRegistryReadOnly
AmazonEKSWorkerNodePolicy
AmazonEKS_CNI_Policy

![screenshot-20241016-141652](../assets/eks_policy.png)

![screenshot-20241016-141712](../assets/eks_policy_1.png)

7. Enter a role name and create the role.

![screenshot-20241016-141954](../assets/eks_role_name_1.png)

![screenshot-20241016-141826](../assets/eks_create_role.png)

8. Enter the node group name and the role that was created.

![screenshot-20241016-142247](../assets/eks_nodegroup.png)

9. Set Amazon Linux 2 CPU Enabled AMI type, select the desired instance type with GPU, typically the G and P type. Set disk size to at least 100 G.

![screenshot-20241016-142340](../assets/eks_ec2_type.png)

10. Specify the desired node size.

![screenshot-20241016-142444](../assets/eks_nodegroup_size.png)

11. Create the node group.

![screenshot-20241016-142520](../assets/eks_create_nodegroup.png)

12. Once the node group has been created, note down the node names that will be used in the lamini installer configuration.

![screenshot-20241016-144133](/assets/eks_nodename.png)

### Install AWS CLI

1. Follow the AWS instruction to install the AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

2. Check the AWS CLI installation.

```bash
aws --version
```

### Access EKS Cluster

1. Create and get the AWS Access Key ID and AWS Secret Access Key.

![screenshot-20241016-145511](../assets/eks_access_key.png)

![screenshot-20241016-145833](../assets/eks_access_key_1.png)

![screenshot-20241016-145852](../assets/eks_access_key_2.png)

![screenshot-20241016-150135](../assets/eks_access_key_3.png)


2. Configure AWS credential.

```bash
aws configure
```

![screenshot-20241016-150214](../assets/eks_configure.png)

```bash
aws eks update-kubeconfig --name <eks-cluster-name>
```

![screenshot-20241016-150748](../assets/eks_update_config.png)

### Install Lamini Installer

Follow the Installing Lamini Platform on Kubernetes section in [Kube installer README.md](https://github.com/lamini-ai/lamini-platform/blob/main/deployments/kube-installer/README.md) to complete the Lamini installation on EKS.
