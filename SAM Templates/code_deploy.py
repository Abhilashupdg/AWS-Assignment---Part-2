import boto3
import json
import os

region_name = os.environ['REGION_NAME']
table_name = os.environ['TABLE_NAME']
client = boto3.client('dynamodb', region_name=region_name)

def lambda_handler(event, context):
    
    event_id = event['id']
    event_detail = event['detail']
    response = client.put_item(TableName = table_name, Item = {
        'event_id' : {'S' : str(event_id)},
        'event_detail' : {'S' : str(event_detail)}
    }
    ) 
    return {
        'statusCode' : 200,
        'body' : json.dumps(event)
    }



