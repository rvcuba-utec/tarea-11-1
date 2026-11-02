import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['nombre_bucket']

    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    return {
        'statusCode': 200,
        'nombre_bucket': nombre_bucket,
        'message': f'Bucket {nombre_bucket} creado exitosamente'
    }
