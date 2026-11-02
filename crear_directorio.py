import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['nombre_bucket']
    nombre_directorio = event['body']['nombre_directorio']

    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=nombre_directorio + '/')

    return {
        'statusCode': 200,
        'nombre_bucket': nombre_bucket,
        'nombre_directorio': nombre_directorio,
        'message': f'Directorio {nombre_directorio}/ creado en bucket {nombre_bucket}'
    }
