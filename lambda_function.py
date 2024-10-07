import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! this is for POC in Cloud session...Edit CCM my test.... (Modified v0.2')
    }
