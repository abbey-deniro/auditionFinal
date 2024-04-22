import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    performancetable = dynamodb.Table('PerformanceDB')
    response = performancetable.scan()
    items = response["Items"]
    return items