import json
import boto3
from boto3.dynamodb.conditions import Attr, Key
from os import getenv

region_name = getenv('APP_REGION')
directorsDB = boto3.resource('dynamodb',
region_name=region_name).Table('DirectorsDB')

def lambda_handler(event, context):
    id = event['Id'];

    key = {
        'Id': id
    }

    directorsDB.delete_item(
        ConditionExpression=Attr('Id').eq(id),
        Key=key
    )
    return {
        'Id': id
    }