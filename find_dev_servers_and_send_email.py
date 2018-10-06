import boto3
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
# Find all Dev servers

dev_filter = [
    {
        'Name': 'tag:Environment',
        'Values': ['Dev']
    }
]
# Fetch InstanceId, LaunchTime, AvailabilityZone
resp = ec2.describe_instances(Filters=dev_filter)
msg_list = []
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        id = instance['InstanceId']
        time = instance['LaunchTime']
        zone = instance['Placement']['AvailabilityZone']
        msg = 'Id = {}, Time = {}, AZ = {} \n'.format(id,time,zone)
        msg_list.append(msg)

# Send Email
sns.publish(
    TopicArn = 'arn:aws:sns:ap-south-1:353848682332:ec2-alerts',
    Message = str(msg_list),
    Subject = 'Java Home Boto3 Demo'
)