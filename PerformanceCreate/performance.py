import json
import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

performanceDB = boto3.resource('dynamodb',
region_name=region_name).Table('PerformanceDB')

def lambda_handler(event, context):
    req_body = event["body"]
    id = str(uuid4())
    title = req_body["title"]
    director = req_body["director"]
    castingDirector = req_body["castingDirector"]
    Date = req_body["Date"]
    Characters = req_body["Characters"]
    Venue = req_body["Venue"]
    Auditioners = req_body["Auditioners"]

    performanceDB.put_item(Item={
        'Id': id,
        'title': title,
        'director': director,
        'castingDirector': castingDirector,
        'Date': Date,
        'Characters': Characters,
        'Venue': Venue,
        'Auditioners': Auditioners
    })

    return {
        'Id': id,
        'title': title,
        'director': director,
        'castingDirector': castingDirector,
        'Date': Date,
        'Characters': Characters,
        'Venue': Venue,
        'Auditioners': Auditioners
    }