This Python script uses the Boto3 library to interact with AWS EC2 instances. It performs two main tasks:

1. **Retrieve and Print Instance Status**: Fetches the status and state of EC2 instances using the `describe_instance_status` method.
2. **Retrieve and Print Instance Details**: Fetches detailed information about instances using the `describe_instances` method.

## Prerequisites

- **Python**: Ensure Python is installed on your system.
- **Boto3**: This script requires the Boto3 library. You can install it using pip:
  ```bash
  pip install boto3
  ```
- **AWS Credentials**: Ensure that AWS credentials are configured on your system. You can set up credentials using the AWS CLI or environment variables.

## Script Details

### Imports

```python
import boto3
```

### Initialization

The script initializes the Boto3 EC2 client for the `ap-southeast-1` region.

```python
ec2_client = boto3.client('ec2', region_name="ap-southeast-1")
```

### Describe Instance Status

The script retrieves the status of all EC2 instances and prints their instance ID, instance status, system status, and instance state.

```python
statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    instant_status = status['InstanceStatus']['Status']
    system_status = status['SystemStatus']['Status']
    instant_state = status['InstanceState']['Name']
    print(f"This {status['InstanceId']} instance is {instant_status} and system status is {system_status}, finally instance state is {instant_state}")
```

### Describe Instances

The script also retrieves detailed information about each EC2 instance, including the instance ID and its current state.

```python
reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"Instance id is: {instance['InstanceId']} & the Instance is: {instance['State']['Name']}")
```

## Usage

1. **Run the Script**: Execute the Python script in your terminal or command prompt.

   ```bash
   python ec2_status.py
   ```

2. **View Output**: The script will print the status and state of all EC2 instances in the specified region.

## Notes

- Make sure your AWS credentials have the necessary permissions to access EC2 instance details.
- The region is set to `ap-southeast-1`, but you can change this to your preferred AWS region.
- Ensure that the Boto3 library is installed and properly configured.

