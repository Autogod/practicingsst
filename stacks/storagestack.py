import boto3
from botocore.exceptions import ClientError
import logging

def create_note_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', end_point='api')

    table = dynamodb.create_table(
        TableName = 'Notes',
        KeySchema = [
            {
                'AttributeName' : 'userId',
                'KeyType' : 'Partition key'
            },
            {
                'AttributeName' : 'noteId',
                'KeyType' : 'Sort Key'
            }
        ],
        AttributeDefinitions =[
            {
                'AttirbuteName' : 'userId',
                'AttributeType' : 'S'
            },
            {
                'AttributeName' : 'noteId',
                'KeyType' : 'S'
            }
        ]
    )
def create_note_bucket(note_bucket, region = 'ap-northeast-1'):
    try:
        s3_client = boto3.client('s3')
        s3_client.create_bucket = boto3.client('s3', region_name = region)
        location = {'LocationConstraint' : region}
        s3_client.create_bucket(Bucket=note_bucket, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True