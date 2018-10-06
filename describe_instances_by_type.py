import boto3
client = boto3.client('ec2')
ec2_filter = [
    {
        'Name': 'instance-type',
        'Values': [
            't2.micro'
        ]
    }
]

resp = client.describe_instances(Filters=ec2_filter)

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        type = instance['InstanceType']
        print('Instance Id = {} And Its State is {} and type is {} '.format(instance_id,state,type))

