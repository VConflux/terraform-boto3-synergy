import boto3


############################ For Singapore  ############################ 

ec2_client_singapore = boto3.client('ec2', region_name="ap-southeast-1")
ec2_resource_singapore = boto3.resource('ec2', region_name="ap-southeast-1")

instance_ids_singapore = []

reservations_singapore = ec2_client_singapore.describe_instances()['Reservations']

for reservation_singapore in reservations_singapore:
    instances = reservation_singapore['Instances']
    for instance in instances:
        instance_ids_singapore.append(instance["InstanceId"])
        
if not instance_ids_singapore:
    print("No instances found in the specified region.")    
else:
    print(f"Found instances: {instance_ids_singapore}")     
        
    response = ec2_resource_singapore.create_tags(
        Resources=instance_ids_singapore,
        Tags=[
            {
                'Key': 'environment',
                'Value': 'prod'
            },
        ]
    )

    print("Tags added successfully. Response:")
    print(response)
    
    
print("########################################################\n")
############################ For Seol  ############################  

ec2_client_seol = boto3.client('ec2', region_name="ap-northeast-2")
ec2_resource_seol = boto3.resource('ec2', region_name="ap-northeast-2")


instance_ids_seol = []


reservations_seol = ec2_client_seol.describe_instances()['Reservations']

for reservation_seol in reservations_seol:
    instances = reservation_seol['Instances']
    for instance in instances:
        instance_ids_seol.append(instance["InstanceId"])
        
if not instance_ids_seol:
    print("No instances found in the specified region.")    
else:
    print(f"Found instances: {instance_ids_seol}")     
        
    response = ec2_resource_seol.create_tags(
        Resources=instance_ids_seol,
        Tags=[
            {
                'Key': 'environment',
                'Value': 'dev'
            },
        ]
    )

    print("Tags added successfully. Response:")
    print(response)