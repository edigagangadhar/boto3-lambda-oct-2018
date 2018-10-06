# Launching EC2 Using Boto3
import boto3
client = boto3.client('ec2', region_name='ap-south-1')
client.run_instances(
    ImageId='ami-00b6a8a2bd28daf19',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
