import boto3

resource = boto3.resource('ec2')
# Boto3 Collection
# List(ec2.Instance)
instances = resource.instances.all()
for instance in instances:
    print(instance.instance_id)
    print(instance.state['Name'])