import json
import boto3 
from boto3.dynamodb.conditions import Key
from os import getenv

region_name = getenv('APP_REGION')
directorsDB = boto3.resource('dynamodb', region_name=region_name).Table('DirectorsDB')

def lambda_handler(event, context):
    response2 = read2()
    return response2
def read2():
    response = directorsDB.scan()
    return response["Items"]