This repository combines AWS automation using Python with Boto3 and infrastructure management using Terraform. While both Boto3 and Terraform can manage AWS resources, there are specific tasks where using both tools provides enhanced capabilities and flexibility.

## Repository Structure

The repository is organized into several key components under ```tf_modules``` folder for terraform files & ```Status reporting using Boto3``` folder for boto3 files.

- **`terraform`**: Contains Terraform configurations for managing AWS infrastructure.
  - **`key_pair`**: Terraform files for creating and managing EC2 key pairs.
  - **`ec2_instance & vpc`**: Terraform files for creating and managing EC2 instances & setting up VPCs and networking components.

- **`python_automation`**: Contains Python scripts utilizing Boto3 for various AWS automation tasks.

## Prerequisites

- **Terraform**: Ensure Terraform is installed on your system. Download it from [terraform.io](https://www.terraform.io/downloads).
- **Python**: Ensure Python is installed on your system.
- **Boto3**: Install Boto3 using pip:
```bash
  pip install boto3
```
  
- **AWS Credentials**: Configure AWS credentials using the AWS CLI or environment variables.

## Terraform Setup
- Please check ```tf_modules``` folder to provisioning ec2 instance using terraform.

## Python Automation

After applying the Terraform configurations, you can use the Python scripts in the `python_automation` folder to automate AWS tasks. The provided script retrieves and displays information about EC2 instances, including:

- **InstanceId**: The ID of the instance.
- **InstanceStatus**: The status of the instance.
- **SystemStatus**: The system status of the instance.
- **InstanceState**: The state of the instance.

### Running the Python Script

1. **Navigate to the Python Automation Directory:**

   ```bash
   cd python_automation
   ```

2. **Run the Python Script:**

   ```bash
   python ec2_status.py
   ```


## Cautions

- **Order of Operations**: Ensure you apply the Terraform configurations in the correct order: `key_pair`, and then ` ec2_instance & vpc`.
- **Resource Cleanup**: Before deleting any resources or if you no longer need the infrastructure, make sure to run `terraform destroy` in each directory to clean up the resources properly:
  ```bash
  cd key_pair
  terraform destroy --auto-approve


  cd ../'ec2_instance & vpc'
  terraform destroy --auto-approve
  ```

