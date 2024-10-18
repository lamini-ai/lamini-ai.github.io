# AWS EKS Installation

## Create EKS Cluster

1. Type EKS in the AWS search bar of the AWS landing page. Select the EKS.

![screenshot-20241016-125951](https://github.com/user-attachments/assets/ec974bdc-f3e8-4f7c-968b-089718722ebd)

2. Click Add Cluster and then Create, to create a cluster.

![screenshot-20241016-124632](https://github.com/user-attachments/assets/19d062c2-fef3-4505-99db-8f4bdd50f5e3)

3. Enter a cluster name.

![screenshot-20241016-124818](https://github.com/user-attachments/assets/87ad2dbf-74ff-4ffe-84f9-b70e4d938ab0)

4. Create an IAM role for EKS.

![screenshot-20241016-124818](https://github.com/user-attachments/assets/80e484e9-6b99-4498-965d-186ddd63b72a)

5. Select the EKS service and check the EKS - Cluster

![screenshot-20241016-125059](https://github.com/user-attachments/assets/d4f6b638-4fc7-47f0-994c-ed6d62d0c935)

6. Enter the role name.

![screenshot-20241016-125246](https://github.com/user-attachments/assets/d51fe3cb-191c-46bd-9821-d0bb2df793cd)

7. Select networking and specify the default security groups.

![screenshot-20241016-125510](https://github.com/user-attachments/assets/e3ffc9bf-8775-4fe4-a315-cb3bc8cc5507)

8. Create the EKS cluster.

![screenshot-20241016-125623](https://github.com/user-attachments/assets/e750d751-a8ed-4367-8581-cc97f39b790b)

9. It will show the creating status.

![screenshot-20241016-125721](https://github.com/user-attachments/assets/d0ad2c7b-d3ac-4855-b794-e261d474410c)

## Set Up NFS

1. Create AWS S3 File Gateway. Type Storage Gateway in the search bar of AWS Console.

![screenshot-20241016-132005](https://github.com/user-attachments/assets/ddc87ddf-2ed4-4477-bd3b-9d098f2e9305)

2. Click on Create gateway.

![screenshot-20241016-132157](https://github.com/user-attachments/assets/0524d580-6bda-4ae2-8de3-afd25edd3fde)

3. Enter gateway name and timezone.

![screenshot-20241016-132349](https://github.com/user-attachments/assets/e8066704-62ff-445e-8676-909a4e7c7504)

4. Select EC2 as platform option and create the instance key pair.

![screenshot-20241016-132636](https://github.com/user-attachments/assets/1a1df9ca-63d1-4a31-a7c4-4e9766f261db)

5. Enter the key pair name and create the key pair.

![screenshot-20241016-132724](https://github.com/user-attachments/assets/eb7e04ba-dc58-4e97-b091-5f22af47d42e)

6. Launch the instance.

![screenshot-20241016-132934](https://github.com/user-attachments/assets/d807e543-92f0-4e64-879b-3b6e26eec188)

7. Access to AWS set to IP address connection and publicly accessible endpoint.

![screenshot-20241016-133202](https://github.com/user-attachments/assets/b99d88e3-ccb9-4963-a4d7-2b4e0ab0d548)

8. Activate gateway.

![screenshot-20241016-133259](https://github.com/user-attachments/assets/c04176fb-fa26-426a-87d5-4f6fe3de26a5)

9. After activating the gateway and configure.

![screenshot-20241016-133541](https://github.com/user-attachments/assets/e80fc075-31bc-48b8-83c9-f00b9488df7c)

10. Create file share.

![screenshot-20241016-133627](https://github.com/user-attachments/assets/14081deb-ca27-4f63-bb77-7083d6bd7b95)

11. Select the gateway that just created, set NFS protocol, and then create the S3 bucket.

![screenshot-20241016-133734](https://github.com/user-attachments/assets/0847d42c-3d95-4b62-8965-1e1563a4f305)

![screenshot-20241016-133755](https://github.com/user-attachments/assets/f1dd14f5-5909-409c-a3d2-4bc9c42fa526)

12. Select S3 that was just created.

![screenshot-20241016-133823](https://github.com/user-attachments/assets/964d89ff-e7fc-4f02-8631-1ffb928c35f6)

13. Create the file share.

![screenshot-20241016-133849](https://github.com/user-attachments/assets/8b196ec7-e9f1-4baa-9584-fcc46d63cb8f)

![screenshot-20241016-133926](https://github.com/user-attachments/assets/6fef6ec3-f368-444f-ab1b-6693abcf4dff)

14. Notice the NFS IP and path that will be used in the Lamini installer deployment.

![screenshot-20241016-134042](https://github.com/user-attachments/assets/b6f3fb02-f855-47e6-88ef-4cbdfc4a251a)

## Create Node Group

1. Select the EKS cluster that was just created.

![screenshot-20241016-140806](https://github.com/user-attachments/assets/1353b041-0808-40f0-80bb-cb578f892235)

2. Select the Compute.

![screenshot-20241016-140901](https://github.com/user-attachments/assets/17e66bd9-7fe9-48da-816a-774eaea90fb6)

3. Select Add Node Group.

![screenshot-20241016-140935](https://github.com/user-attachments/assets/d2f4de58-01b1-40e9-bc88-3c67c2edca29)

4. Create an instance role with policy.

![screenshot-20241016-142207](https://github.com/user-attachments/assets/56e3f77a-5fa1-41c8-bef5-2fbcb6f9031d)

5. Select EC2.

![screenshot-20241016-141329](https://github.com/user-attachments/assets/e34659a7-dbca-41d5-9cc6-5dd9cc7127e8)

6. Ensure to select the following policies:
AmazonEC2ContainerRegistryReadOnly
AmazonEKSWorkerNodePolicy
AmazonEKS_CNI_Policy

![screenshot-20241016-141652](https://github.com/user-attachments/assets/4df48597-3db1-4510-8033-ac25450ad6d1)

![screenshot-20241016-141712](https://github.com/user-attachments/assets/21f270c4-0e8b-41e5-909c-fb4aae8de94d)

7. Enter the role name and create the role.

![screenshot-20241016-141954](https://github.com/user-attachments/assets/a3a4d04c-383d-4ff3-8e1c-4a2c71161ae9)

![screenshot-20241016-141826](https://github.com/user-attachments/assets/9484f741-14de-475f-a672-578dc9594d17)

8. Enter the node group name and the role that was created.

![screenshot-20241016-142247](https://github.com/user-attachments/assets/fd3adda8-c104-4f7e-a936-9a908966e5a5)

9. Set Amazon Linux 2 CPU Enabled AMI type, select the desired instance type with GPU, and set disk size to 100 G.

![screenshot-20241016-142340](https://github.com/user-attachments/assets/e4acb36c-61c6-41b2-9c8d-cc052ea4fa61)

10. Specify the desired node size.

![screenshot-20241016-142444](https://github.com/user-attachments/assets/e9016a5f-b5f9-4e35-9bf2-98ad2ec93468)

11. Create the node group.

![screenshot-20241016-142520](https://github.com/user-attachments/assets/4ec322e9-0f16-460a-a8c4-ac7908f6246d)

12. Once the node group has been created, note down the node names that will be used in the lamini installer configuration.

![screenshot-20241016-144133](https://github.com/user-attachments/assets/184c4751-3a92-4638-a57b-facc2fee6980)

### Install AWS CLI

1. Follow the AWS instruction to install the AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

2. Check the AWS CLI installation.

```bash
aws --version
```

### Access EKS Cluster

1. Create and get the AWS Access Key ID and AWS Secret Access Key.

![screenshot-20241016-145511](https://github.com/user-attachments/assets/725860fb-63ea-4704-b4e3-27fcc3e8435d)

![screenshot-20241016-145833](https://github.com/user-attachments/assets/fafd8625-6466-448f-987f-22c61e5d168c)

![screenshot-20241016-145852](https://github.com/user-attachments/assets/e93ab366-69f3-4bd3-b239-c5353e128cab)

![screenshot-20241016-150135](https://github.com/user-attachments/assets/3fd14b3b-bdab-4696-88e5-76281119e51e)

2. Configure AWS credential.

```bash
aws configure
```

![screenshot-20241016-150214](https://github.com/user-attachments/assets/e76d18f3-8156-4af2-a9bd-122b4eff8bd5)

```bash
aws eks update-kubeconfig --name <eks-cluster-name>
```

![screenshot-20241016-150748](https://github.com/user-attachments/assets/09dc7a4f-2f42-4869-8424-8539ce0a25e6)

### Install Lamini Installer

Follow the Installing Lamini Platform on Kubernetes section in [Kube installer README.md](https://github.com/lamini-ai/lamini-platform/blob/main/deployments/kube-installer/README.md) to complete the Lamini installation on EKS.
