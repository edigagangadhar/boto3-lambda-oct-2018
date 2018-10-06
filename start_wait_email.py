import boto3

ec2 = boto3.client('ec2')

ec2.start_instances(InstanceIds=['i-0cef60720c068359d'])

# Wait for ec2 to be running state

waiter = ec2.get_waiter('instance_running')
print('waiting for running state')
waiter.wait(InstanceIds=['i-0cef60720c068359d'])
print('Instance is running')