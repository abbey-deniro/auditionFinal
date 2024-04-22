import json
import boto3
from os import getenv
from uuid import uuid4
from boto3.dynamodb.conditions import Key, And, Attr

region_name = getenv('APP_REGION')

performanceDB = boto3.resource('dynamodb',
region_name=region_name).Table('PerformanceDB')

performersDB = boto3.resource('dynamodb',
region_name=region_name).Table('PerformersDB')

def lambda_handler(event, context):
    req_body = event["body"]
    Auditioners = req_body["AuditionersId"]
    id = req_body["Id"]
    Name = req_body["name"]
    Title = req_body["title"]
    CastingDirector = req_body["castingDirector"]

    isPresent = checkTableElement(CastingDirector, Name)
    if isPresent:
        updateTable(id, Name, Auditioners, Title)


def updateTable(id, Name, Auditioners, Title):
    performanceDB.put_item(
        Key={"Id": id},
        UpdateExpression="SET Characters = list_append(Characters, :i)",
        ExpressionAttributeValues={
            ':i': [Name]
        },
        ReturnValues="UPDATED_NEW"
    )

    performersDB.update_item(
        Key={"Id": Auditioners},
        UpdateExpression="SET currentPerformances = list_append(currentPerformances, :i)",
        ExpressionAttributeValues={
            ':i': [Title]
        },
        ReturnValues="UPDATED_NEW"
    )

def checkTableElement(CastingDirector, Name):
    response = performanceDB.scan(
        FilterExpression=Attr('CastingDirector').eq(
            CastingDirector) & Attr('Auditioners').eq(Name)
    )
    if response:
        return True
    else:
        return False