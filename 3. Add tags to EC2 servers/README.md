# AWS EC2 Instance Tagging Automation with Boto3

This script automates the process of tagging AWS EC2 instances in multiple regions using Boto3. The script targets instances in the Singapore (`ap-southeast-1`) and Seoul (`ap-northeast-2`) regions, applying environment-specific tags to the instances found in each region.

## Scenario

The script performs the following tasks:

- **Singapore Region**:
  - Retrieves all EC2 instances.
  - Tags them with the `environment: prod`.

- **Seoul Region**:
  - Retrieves all EC2 instances.
  - Tags them with the `environment: dev`.

## Outcome

- **For Singapore (`ap-southeast-1`)**:
  - All EC2 instances found are tagged with `environment: prod`.
  - If no instances are found, a message is displayed indicating this.

- **For Seoul (`ap-northeast-2`)**:
  - All EC2 instances found are tagged with `environment: dev`.
  - If no instances are found, a message is displayed indicating this.

## Prerequisites

- Python 3.x
- Boto3 - ```pip install boto3```


### Running the Python Script
   ```bash
   python add_tags.py
   ```


## Cautions

- **Order of Operations**: Ensure you apply the Terraform configurations in the correct order: `key_pair`, and then ` ec2_instance_&_vpc`.
- **Resource Cleanup**: Before deleting any resources or if you no longer need the infrastructure, make sure to run `terraform destroy` in each directory to clean up the resources properly
- **Navigate to the terraform Directory:**
  ```bash
  cd /0. tf_modules/key_pair
  terraform destroy --auto-approve


  cd /0. tf_modules/ec2_instance_&_vpc
  terraform destroy --auto-approve
  ```
