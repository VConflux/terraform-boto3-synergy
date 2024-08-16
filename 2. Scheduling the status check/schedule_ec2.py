import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="ap-southeast-1")

def check_instance_status():
    statuses = ec2_client.describe_instance_status(         # this describe_instance_status provides only running instance to see the all instance add 'IncludeAllInstances to True'
            IncludeAllInstances=True    
        )            
    for status in statuses['InstanceStatuses']:
        instant_status = status['InstanceStatus']['Status']
        system_status = status['SystemStatus']['Status']
        instant_state = status['InstanceState']['Name']
        print(f"This {status['InstanceId']} instance is {instant_status} and system status is {system_status}, finally instance state is {instant_state}")

print('___________________________________________________________________________\n')
print('---------------------------------------------------------------------------\n')
# or every 5 second
schedule.every(5).seconds.do(check_instance_status)

# or every 5 minute
# schedule.every(5).minute.do(check_instance_status)

# or Every saturday at 12:00
# schedule.every().saturday.at("12:00")

while True: 
    schedule.run_pending()