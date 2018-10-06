import boto3
client = boto3.client('ec2')
resp = client.describe_instances()

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        if state == 'stopped':
            print('Instance Id = {} And Its State is {}'.format(instance_id,state))

