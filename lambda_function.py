import boto3
import json
import urllib.parse

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    glue = boto3.client('glue')

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        print(f"Triggered by file: {key} in bucket: {bucket}")

        response = glue.start_job_run(JobName='careplus-glue-etl-job')
        print(f"Glue job started: {response['JobRunId']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda trigger executed successfully')
    }
