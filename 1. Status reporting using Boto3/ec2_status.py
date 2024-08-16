import boto3

ec2_client = boto3.client('ec2', region_name="ap-southeast-1")

# with 'describe_instance_status' you can grab status, state of instances
statuses = ec2_client.describe_instance_status()    # this describe_instance_status provides only running instance
for status in statuses['InstanceStatuses']:
    instant_status = status['InstanceStatus']['Status']
    system_status = status['SystemStatus']['Status']
    instant_state = status['InstanceState']['Name']
    print(f"This {status['InstanceId']} instance is {instant_status} and system status is {system_status}, finally instance state is {instant_state}")
    

print()
# With 'describe_instances' is more describable output then 'describe_instance_status', so using this you can also grab instance status.  

reservations = ec2_client.describe_instances()      # this describe_instances provides all instance, running, terminated, pending etc
for reservation in reservations['Reservations']:    # here reservations is a value, for lising reservations we need reservations['Reservations']
    instances = reservation['Instances']
    for instance in instances:              
        #print(instance)             # This will give us instance dictionary instead of list.
        print(f"Instance id is: {instance['InstanceId']} & the Instance is: {instance['State']['Name']}")        # this is a dictionary= instance['State'], on that dictionary name is a key
        
