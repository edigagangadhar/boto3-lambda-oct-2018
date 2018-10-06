import boto3

ec2 = boto3.client('ec2')

vol_filter = [
    {
        'Name':'status',
        'Values':['in-use']
    }
]
resp = ec2.describe_volumes(Filters=vol_filter)
for volume in resp['Volumes']:
    vol_id = volume['VolumeId']
    print('Volume ID ',vol_id)
    ec2.create_snapshot(
        Description='Created by boto3',
        VolumeId=vol_id
    )

    # Boto3 Waiter