
def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']
    file_name = event['Records'][0]['object']['key']
     # Logic to send a mai
