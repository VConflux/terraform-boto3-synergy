
# Terraform Configuration for EC2 Instances and VPC

## Overview

This task contains Terraform configurations for managing AWS EC2 instances and VPCs. The configurations are organized into different folders:

- **`key_pair`**: Contains Terraform files for managing EC2 key pairs.
- **` ec2_instance_&_vpc`**: Contains Terraform files for creating and managing EC2 instances & setting up VPCs and related networking components.

## Prerequisites

- **Terraform**: Ensure Terraform is installed on your system. You can download it from [terraform.io](https://www.terraform.io/downloads).
- **AWS Credentials**: Ensure that AWS credentials are configured on your system. You can set up credentials using the AWS CLI or environment variables.

## Usage Instructions

### 1. Set Up Key Pair

First, navigate to the `key_pair` directory and apply the Terraform configuration to create the necessary key pairs for your EC2 instances.

```bash
terraform init

terraform validate

terraform plan

terraform apply --auto-approve
```


### 2. Set Up EC2 Instances

Finally, navigate to the ` ec2_instance_&_vpc` directory and apply the Terraform configuration to create and manage EC2 instances using the previously created key pairs and VPC.

```bash
cd ec2_instance_&_vpc

terraform init

terraform validate

terraform plan

terraform apply --auto-approve
```

## Cautions

- **Order of Operations**: Ensure you apply the Terraform configurations in the correct order: `key_pair`, and then ` ec2_instance_&_vpc`.
- **Resource Cleanup**: Before deleting any resources or if you no longer need the infrastructure, make sure to run `terraform destroy` in each directory to clean up the resources properly:
  ```bash
  cd key_pair
  terraform destroy --auto-approve


  cd 'ec2_instance_&_vpc
  terraform destroy --auto-approve
  ```
  This will prevent orphaned resources and potential additional costs.

- **AWS Costs**: Be aware of the potential costs associated with running AWS resources. Ensure that resources are properly managed and destroyed when no longer needed to avoid unexpected charges.


## Notes

- Ensure that each directory's `terraform apply` command is executed in sequence: first `key_pair`, and `ec2_instance_&_vpc`.
- Make sure your AWS credentials have the necessary permissions to create and manage EC2 instances, VPCs, and key pairs.
- The configurations are designed to be modular and dependent on the order of execution.

