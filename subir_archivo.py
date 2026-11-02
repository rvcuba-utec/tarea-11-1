import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['nombre_bucket']
    nombre_directorio = event['body']['nombre_directorio']
    nombre_archivo = event['body']['nombre_archivo']
    contenido = event['body']['contenido']

    s3 = boto3.client('s3')
    key = nombre_directorio + '/' + nombre_archivo
    s3.put_object(
        Bucket=nombre_bucket,
        Key=key,
        Body=contenido.encode('utf-8')
    )

    return {
        'statusCode': 200,
        'nombre_bucket': nombre_bucket,
        'key': key,
        'message': f'Archivo {nombre_archivo} subido a {nombre_bucket}/{key}'
    }
