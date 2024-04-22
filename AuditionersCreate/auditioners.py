import json
import boto3
from boto3.dynamodb.conditions import Key
from os import getenv
from uuid import uuid4

region_name = getenv('APP_REGION')

performersDB = boto3.resource('dynamodb',
region_name=region_name).Table('PerformersDB')

def lambda_handler(event, context):
    req_body = event["body"]
    id = str(uuid4())
    name = req_body["name"]
    email = req_body["email"]
    phone = req_body["phone"]
    pastPerformances = req_body["pastPerformances"]
    currentPerformances = req_body["currentPerformances"]
    username = req_body["username"]
    password = req_body["password"]

    performersDB.put_item(Item={
        'Id': id,
        'name': name,
        'email': email,
        'phone': phone,
        'pastPerformances': pastPerformances,
        'currentPerformances': currentPerformances,
        'username': username,
        'password': password
        })

    return {
        'Id': id,
        'name': name,
        'email': email,
        'phone': phone,
        'pastPerformances': pastPerformances,
        'currentPerformances': currentPerformances,
        'username': username,
        'password': password
    }