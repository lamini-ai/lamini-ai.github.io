# AWS EKS Installation

## Create EKS Cluster

1. Type EKS in the AWS search bar of the AWS landing page. Select the EKS.

![screenshot-20241016-125951](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377213426-ec974bdc-f3e8-4f7c-968b-089718722ebd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T192919Z&X-Amz-Expires=300&X-Amz-Signature=18db1123a7de0ac006f70fe6d93b9c7677bb7506d92b00384e8770f85b6f55c3&X-Amz-SignedHeaders=host)

2. Click Add Cluster and then Create, to create a cluster.

![screenshot-20241016-124632](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377213778-19d062c2-fef3-4505-99db-8f4bdd50f5e3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T193407Z&X-Amz-Expires=300&X-Amz-Signature=246e82c0dd5ab7d40721d7fcbb5c2351c559af83db6a64f3bcc5a8516c6fdf60&X-Amz-SignedHeaders=host)

3. Enter a cluster name.

![screenshot-20241016-124818](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377213847-87ad2dbf-74ff-4ffe-84f9-b70e4d938ab0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195700Z&X-Amz-Expires=300&X-Amz-Signature=7ac1a28c1134ce6e8b4c6fc706191f5e1505e0aaf31ecc1128814bd1927903f2&X-Amz-SignedHeaders=host)

4. Create an IAM role for EKS.

![screenshot-20241016-124818](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377213960-80e484e9-6b99-4498-965d-186ddd63b72a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195730Z&X-Amz-Expires=300&X-Amz-Signature=6f39f819d054ffe4c58ae7fe7c6120feb58a6d393458ae7e39b547242e109102&X-Amz-SignedHeaders=host)

5. Select the EKS service and check the EKS - Cluster

![screenshot-20241016-125059](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377214367-d4f6b638-4fc7-47f0-994c-ed6d62d0c935.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195748Z&X-Amz-Expires=300&X-Amz-Signature=025d30e7df79891058c79be208d928f08963560fc144884eb89e7480dd7d6062&X-Amz-SignedHeaders=host)

6. Enter the role name.

![screenshot-20241016-125246](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377214681-d51fe3cb-191c-46bd-9821-d0bb2df793cd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195821Z&X-Amz-Expires=300&X-Amz-Signature=23ac5ea7f49530bc9882e313217dbcd8d6bfe8fdf1c0e9e47ecd8bc32eac929f&X-Amz-SignedHeaders=host)

7. Select networking and specify the default security groups.

![screenshot-20241016-125510](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377215057-e3ffc9bf-8775-4fe4-a315-cb3bc8cc5507.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195921Z&X-Amz-Expires=300&X-Amz-Signature=e12ed090f937f392d9104cbd1796d904f4da553130ae52fb1eb61a7cfff66f71&X-Amz-SignedHeaders=host)

8. Create the EKS cluster.

![screenshot-20241016-125623](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377215267-e750d751-a8ed-4367-8581-cc97f39b790b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195934Z&X-Amz-Expires=300&X-Amz-Signature=5b2b0997b95f8e389c89e149c33b8b86893d6ee9a75c3c7737c47b1543755184&X-Amz-SignedHeaders=host)

9. It will show the creating status.

![screenshot-20241016-125721](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377215363-d0ad2c7b-d3ac-4855-b794-e261d474410c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195952Z&X-Amz-Expires=300&X-Amz-Signature=46e3fb24e5810a304fce89d75706b295a9957262262f6ebeb60a7a7e5496d524&X-Amz-SignedHeaders=host)

## Set Up NFS

1. Create AWS S3 File Gateway. Type Storage Gateway in the search bar of AWS Console.

![screenshot-20241016-132005](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377225543-ddc87ddf-2ed4-4477-bd3b-9d098f2e9305.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200917Z&X-Amz-Expires=300&X-Amz-Signature=cc1a9ba7fa1449e2fbe43a9946ec33be95cb809fd8ec56f7b9cf3189cdb733ae&X-Amz-SignedHeaders=host)

2. Click on Create gateway.

![screenshot-20241016-132157](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377225925-0524d580-6bda-4ae2-8de3-afd25edd3fde.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T201329Z&X-Amz-Expires=300&X-Amz-Signature=4ce1828b17e54a7ef8db632f2ab337fb4dabefc255f3109b806399913c741b99&X-Amz-SignedHeaders=host)

3. Enter gateway name and timezone.

![screenshot-20241016-132349](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377226031-e8066704-62ff-445e-8676-909a4e7c7504.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T201349Z&X-Amz-Expires=300&X-Amz-Signature=78b583272fce34b18bcd342336ae6ea6088cd09a88911ce266426ecc69963538&X-Amz-SignedHeaders=host)

4. Select EC2 as platform option and create the instance key pair.

![screenshot-20241016-132636](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377226254-1a1df9ca-63d1-4a31-a7c4-4e9766f261db.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T201404Z&X-Amz-Expires=300&X-Amz-Signature=e9ec87f9401eaa25f720e7b96b6875e9df738797770ea19859a1567f3ae2d613&X-Amz-SignedHeaders=host)

5. Enter the key pair name and create the key pair. Download the pem file to be used for accessing the instance for deployment later.

![screenshot-20241016-132724](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377226496-eb7e04ba-dc58-4e97-b091-5f22af47d42e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T201417Z&X-Amz-Expires=300&X-Amz-Signature=b89515dcf07d55e756bd7f380a9ee1db5511c45ffbb6c46ffa9750bf2efed2ab&X-Amz-SignedHeaders=host)

6. Launch the instance.

![screenshot-20241016-132934](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377226668-d807e543-92f0-4e64-879b-3b6e26eec188.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T201444Z&X-Amz-Expires=300&X-Amz-Signature=5f053fc5b03827839e4980003b3d87b37579a9d7e32cb414c83499a51bde4cd2&X-Amz-SignedHeaders=host)

7. Connect to AWS - select the IP address connection option and publicly accessible endpoint option.

![screenshot-20241016-133202](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377227290-b99d88e3-ccb9-4963-a4d7-2b4e0ab0d548.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T201520Z&X-Amz-Expires=300&X-Amz-Signature=57b32703800536d73af00ff292234856a7a09e4049627e620761ad883694ea23&X-Amz-SignedHeaders=host)

8. Activate gateway.

![screenshot-20241016-133259](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377227407-c04176fb-fa26-426a-87d5-4f6fe3de26a5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200504Z&X-Amz-Expires=300&X-Amz-Signature=502fad140c342c1e9989367b82d9a9108c38dc2cd2338943119f20f59c268f7a&X-Amz-SignedHeaders=host)

9. Configure after activating the gateway.

![screenshot-20241016-133541](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377227894-e80fc075-31bc-48b8-83c9-f00b9488df7c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200524Z&X-Amz-Expires=300&X-Amz-Signature=56ff1afb125e7d51887fa70d1912cfe82107c19dd657083602fe04abf9ea1eaf&X-Amz-SignedHeaders=host)

10. Create file share.

![screenshot-20241016-133627](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377228009-14081deb-ca27-4f63-bb77-7083d6bd7b95.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200621Z&X-Amz-Expires=300&X-Amz-Signature=2af3e879c83e259162905cdfe3e8cd5a83e0818dcf1174fbebaffaa37b12eff3&X-Amz-SignedHeaders=host)

11. Select the gateway that just created, set NFS protocol, and then create the S3 bucket.

![screenshot-20241016-133734](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377228341-0847d42c-3d95-4b62-8965-1e1563a4f305.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200639Z&X-Amz-Expires=300&X-Amz-Signature=560c1f48fe6da727afaf81abebb587204a53bee4b2a9f87246477d5c3157d918&X-Amz-SignedHeaders=host)

![screenshot-20241016-133755](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377228434-f1dd14f5-5909-409c-a3d2-4bc9c42fa526.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200652Z&X-Amz-Expires=300&X-Amz-Signature=bfb6ad39f002261b3a38a2dde5769188ec6b97c74acefe9d563d357a31968092&X-Amz-SignedHeaders=host)

12. Select the S3 that was just created.

![screenshot-20241016-133823](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377228661-964d89ff-e7fc-4f02-8631-1ffb928c35f6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200712Z&X-Amz-Expires=300&X-Amz-Signature=50ec0172290da4f954877686e194329f15f452646ffe4c2920a2c992b033a1c8&X-Amz-SignedHeaders=host)

13. Create the file share.

![screenshot-20241016-133849](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377228852-8b196ec7-e9f1-4baa-9584-fcc46d63cb8f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200728Z&X-Amz-Expires=300&X-Amz-Signature=ad2b7386a57b7ae67dcd374dc33df3ceb41d8f81760c3c046a5de53c561f922a&X-Amz-SignedHeaders=host)

![screenshot-20241016-133926](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377228960-6fef6ec3-f368-444f-ab1b-6693abcf4dff.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200742Z&X-Amz-Expires=300&X-Amz-Signature=2a0d699f8f6abb978ed42247ad21c5cdbfc33af9a7888028086a1e3613a6d2db&X-Amz-SignedHeaders=host)

14. Note down the NFS IP and path that will be used in the NFS setup for Lamini installation.

![screenshot-20241016-134042](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377229914-b6f3fb02-f855-47e6-88ef-4cbdfc4a251a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T200800Z&X-Amz-Expires=300&X-Amz-Signature=292a2158315d112e0c2f628f56cc0acb6d226575805473ff04963e56b720e53e&X-Amz-SignedHeaders=host)

## Create Node Group

1. Select the EKS cluster that was just created.

![screenshot-20241016-140806](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239274-1353b041-0808-40f0-80bb-cb578f892235.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195011Z&X-Amz-Expires=300&X-Amz-Signature=37c6ada903ea82d1c563167c06811032551e8710b0fb9a4c070a517b83dba450&X-Amz-SignedHeaders=host)

2. Select the Compute.

![screenshot-20241016-140901](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239368-17e66bd9-7fe9-48da-816a-774eaea90fb6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195023Z&X-Amz-Expires=300&X-Amz-Signature=1fb30835c4bec4999116cc4f400c4ad5a03c281b63c63600bec28093855e520b&X-Amz-SignedHeaders=host)

3. Select Add Node Group.

![screenshot-20241016-140935](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239450-d2f4de58-01b1-40e9-bc88-3c67c2edca29.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195029Z&X-Amz-Expires=300&X-Amz-Signature=29a7000a781cfc2950aebbd3fe33bd56853313a1cdf94a9b436e3292469793ee&X-Amz-SignedHeaders=host)

4. Create an instance role with policy.

![screenshot-20241016-142207](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239527-56e3f77a-5fa1-41c8-bef5-2fbcb6f9031d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195036Z&X-Amz-Expires=300&X-Amz-Signature=b2dc0f8ad6c68435d16bb5a523c72ebe979cefbfcfa913245777971a82f50047&X-Amz-SignedHeaders=host)

5. Select EC2.

![screenshot-20241016-141329](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239675-e34659a7-dbca-41d5-9cc6-5dd9cc7127e8.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195044Z&X-Amz-Expires=300&X-Amz-Signature=844b219daa99001c451422b91c9c4b5cd96bcca2895aa86a1b429b16f2f44318&X-Amz-SignedHeaders=host)

6. Ensure to select the following policies:
AmazonEC2ContainerRegistryReadOnly
AmazonEKSWorkerNodePolicy
AmazonEKS_CNI_Policy

![screenshot-20241016-141652](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239707-4df48597-3db1-4510-8033-ac25450ad6d1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195053Z&X-Amz-Expires=300&X-Amz-Signature=b5fde848f8dc22039fb15e46ce523431ec173424463ea864c7e802723bf3ba45&X-Amz-SignedHeaders=host)

![screenshot-20241016-141712](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377239766-21f270c4-0e8b-41e5-909c-fb4aae8de94d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195059Z&X-Amz-Expires=300&X-Amz-Signature=ad1b2fc849accfa3b8a46e0cb9d924e4612384aec27853fda77f78a66010c738&X-Amz-SignedHeaders=host)

7. Enter a role name and create the role.

![screenshot-20241016-141954](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377240168-a3a4d04c-383d-4ff3-8e1c-4a2c71161ae9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195105Z&X-Amz-Expires=300&X-Amz-Signature=bd9081c04bc4a662720b6ab2c4a5bbd94fbabc117b6ea8d919e3af9bdd8192d3&X-Amz-SignedHeaders=host)

![screenshot-20241016-141826](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377240120-9484f741-14de-475f-a672-578dc9594d17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195119Z&X-Amz-Expires=300&X-Amz-Signature=7aedadaa22aaa7f9cb47540263307e66fb558eca161791535874a64b3b44403f&X-Amz-SignedHeaders=host)

8. Enter the node group name and the role that was created.

![screenshot-20241016-142247](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377240241-fd3adda8-c104-4f7e-a936-9a908966e5a5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195127Z&X-Amz-Expires=300&X-Amz-Signature=46ebb570b153bf82f7a4012e6a3386c68e624700fa37cb6aa8dfb382d76bcd27&X-Amz-SignedHeaders=host)

9. Set Amazon Linux 2 CPU Enabled AMI type, select the desired instance type with GPU, typically the G and P type. Set disk size to at least 100 G.

![screenshot-20241016-142340](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377240739-e4acb36c-61c6-41b2-9c8d-cc052ea4fa61.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195134Z&X-Amz-Expires=300&X-Amz-Signature=81d810e52d7bb265c47d82eae7985b5cb47819247a74673e180107365edbd321&X-Amz-SignedHeaders=host)

10. Specify the desired node size.

![screenshot-20241016-142444](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377240799-e9016a5f-b5f9-4e35-9bf2-98ad2ec93468.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195140Z&X-Amz-Expires=300&X-Amz-Signature=e3b6770eb6a6b208382f3bb65053a1349eee0247ae1fadd18b6ecdf04708f684&X-Amz-SignedHeaders=host)

11. Create the node group.

![screenshot-20241016-142520](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377240895-4ec322e9-0f16-460a-a8c4-ac7908f6246d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195148Z&X-Amz-Expires=300&X-Amz-Signature=4555eb4667dd8282cff8aa092070a4737841af593f7a922fe69bf33dce185347&X-Amz-SignedHeaders=host)

12. Once the node group has been created, note down the node names that will be used in the lamini installer configuration.

![screenshot-20241016-144133](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377241398-184c4751-3a92-4638-a57b-facc2fee6980.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195205Z&X-Amz-Expires=300&X-Amz-Signature=fcd4a1f4709d648a0a5f8fd723e0dc2144269b240331fcc2f7102d0728ca0432&X-Amz-SignedHeaders=host)

### Install AWS CLI

1. Follow the AWS instruction to install the AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

2. Check the AWS CLI installation.

```bash
aws --version
```

### Access EKS Cluster

1. Create and get the AWS Access Key ID and AWS Secret Access Key.

![screenshot-20241016-145511](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377246459-725860fb-63ea-4704-b4e3-27fcc3e8435d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195228Z&X-Amz-Expires=300&X-Amz-Signature=f73476ef0ce7657e19c037227e08acc1452d7c9032e7f1468593270ff0dd839c&X-Amz-SignedHeaders=host)

![screenshot-20241016-145833](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377246483-fafd8625-6466-448f-987f-22c61e5d168c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195236Z&X-Amz-Expires=300&X-Amz-Signature=9d9d1c952bb03b2ab868cda89d7e4781f002127f5372aaebaa4056574654dc30&X-Amz-SignedHeaders=host)

![screenshot-20241016-145852](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377246561-e93ab366-69f3-4bd3-b239-c5353e128cab.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195242Z&X-Amz-Expires=300&X-Amz-Signature=55cf2cc46c3a51126ad51add1af2d64098c5006737944fa9520ec0d475bb17ab&X-Amz-SignedHeaders=host)

![screenshot-20241016-150135](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377246651-3fd14b3b-bdab-4696-88e5-76281119e51e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195247Z&X-Amz-Expires=300&X-Amz-Signature=c3f77802d50df95a74f1b2dd6df72738c832f5d09b88e4da97b475b4983baf97&X-Amz-SignedHeaders=host)


2. Configure AWS credential.

```bash
aws configure
```

![screenshot-20241016-150214](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377246693-e76d18f3-8156-4af2-a9bd-122b4eff8bd5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195254Z&X-Amz-Expires=300&X-Amz-Signature=1eaed2b5a02b31b0bfc2f27453b8a9b5fa4ec604884854a4b0d3427057a35036&X-Amz-SignedHeaders=host)

```bash
aws eks update-kubeconfig --name <eks-cluster-name>
```

![screenshot-20241016-150748](https://github-production-user-asset-6210df.s3.amazonaws.com/165714345/377246800-09dc7a4f-2f42-4869-8424-8539ce0a25e6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20241018%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241018T195302Z&X-Amz-Expires=300&X-Amz-Signature=5cea9c02e3b521f9250f2732fee687bee89c8d5038d8953ccc2893d27b015ff4&X-Amz-SignedHeaders=host)

### Install Lamini Installer

Follow the Installing Lamini Platform on Kubernetes section in [Kube installer README.md](https://github.com/lamini-ai/lamini-platform/blob/main/deployments/kube-installer/README.md) to complete the Lamini installation on EKS.
