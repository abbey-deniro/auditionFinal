import json
import boto3
from os import getenv
from uuid import uuid4
from boto3.dynamodb.conditions import Key

region_name = getenv('APP_REGION')

performanceDB = boto3.resource('dynamodb',
region_name=region_name).Table('PerformanceDB')

def lambda_handler(event, context):
    req_body = event["body"]
    id = req_body["Id"]
    Name = req_body["name"]

    performanceDB.update_item(
        Key={"Id": id},
        UpdateExpression="SET Auditioners = list_append(Auditioners, :i)",
        ExpressionAttributeValues={
            ':i': [Name]
        },
        ReturnValues="UPDATED_NEW"
    )

    return{
        'Id': id,
    }