# EC2 Instance Status Checker with Boto3

## Overview

This project contains a Python script that automates the checking of AWS EC2 instance statuses using Boto3. The script is designed to periodically retrieve and display the status of all EC2 instances, including their instance status, system status, and state.

## Features

- **Boto3 Integration**: Leverages the AWS SDK for Python (Boto3) to interact with AWS EC2 services.
- **Automated Scheduling**: Uses the `schedule` library to periodically check the status of EC2 instances.
- **Customizable Intervals**: The script can be configured to run at different intervals, such as every 5 seconds, every 5 minutes, or at a specific time on a particular day.
- **Create Infra with terraform:** The repository is organized into several key components under ```0. 0. tf_modules``` folder for terraform files

## Usage

- The script retrieves and prints the status of all EC2 instances in the specified region (`ap-southeast-1` by default).
- The interval for checking instance statuses can be adjusted by modifying the scheduling lines in the script.

## Example Output

The script provides output in the following format:

```
This i-0abcd1234efgh5678 instance is running and system status is ok, finally instance state is running
```

## Prerequisites

- Python 3.x
- Boto3 - ```pip install boto3```
- Schedule - ```pip install schedule```


### Running the Python Script
   ```bash
   python schedule_ec2.py
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

