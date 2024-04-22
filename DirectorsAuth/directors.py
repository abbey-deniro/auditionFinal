import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key, Attr
import re
from base64 import b64encode, b64decode

dynamodb = boto3.resource("dynamodb")
auth_users_table = dynamodb.Table('DirectorsDB')
token_list = ["authtoken01","authtoken02","authtoken03","authtoken04"]
db_mode = True

def lambda_handler(event, context):
    # two options for the header, see test json
    # auth_header = event['authorizationToken']
    auth_header = event['headers']["Authorization"]
    #print(auth_header)
    
    allow = "Deny"

    
    if db_mode == False:
        if auth_header in token_list:
            allow = "Allow"
    else:
        #create_user_in_db("chris", "pwd123")
        #create_user_in_db("john", "pwd456")
        
        # username = "chris"
        # password = "pwd123"
        
        matcher1 = re.match("^Basic (.+)$", auth_header)
        print(matcher1[1])
        credentials = b64decode(matcher1[1])
        print(credentials)
        
        # credentials is a byte string, so you have to use br in your regex
        matcher2 = re.match(br"^([^:]+):(.+)$", credentials)
        
        # coerce the bytes into an actual string you can use
        username = matcher2[1].decode('utf-8')
        password = matcher2[2].decode('utf-8')
        
        print(username)
        print(password)
            
        
        if found_in_db(username, password):
            print("user found in db")
            allow = "Allow"
        else:
            print("user not found in db")

    
    response = {
        "principalId": "abcdef", # The principal user identification associated with the token sent by the client.
        "policyDocument": {
        "Version": "2012-10-17",
            "Statement": [
                {
                "Action": "execute-api:Invoke",
                # "Effect": "Allow|Deny",
                "Effect": allow,
                # "Resource": "arn:aws:execute-api:{regionId}:{accountId}:{apiId}/{stage}/{httpVerb}/[{resource}/[{child-resources}]]"
                "Resource": event['methodArn']
                }
            ]
        },
            "context": {
            "exampleKey": "exampleValue"
        }
    }
    
    return response
    
    
    
def found_in_list(myToken):
    for auth_item in mydataSet:
        if(myToken == auth_item):
            return True
    return False
  
  
  
def create_user_in_db(username, password):
    user = {
        'id':str(uuid.uuid4()),
        'username': username,
        'password': password
    }
    
    auth_users_table.put_item(Item=user)
    
    
    
def found_in_db(username, password):
    user = auth_users_table.scan(FilterExpression=Attr('username').eq(username) & Attr('password').eq(password))
    # print(user)
    
    if len(user["Items"]) == 1 :
        return True
    else:
        return False