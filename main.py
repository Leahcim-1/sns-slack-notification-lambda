import urllib3 
import json
http = urllib3.PoolManager() 

def lambda_handler(event, context): 
    url = "https://slack.com/api/chat.postMessage"    
    body = {
        'token': '<* Slack App Token *>',
        'channel': '<* Your Channel Here! *>',
        'text': "<* Random dumb message *>"
    }
    encoded_msg = json.dumps(body).encode('utf-8')
    resp = http.request('POST', url, body=encoded_msg)
    print({
        "message": event['Records'][0]['Sns']['Message'], 
        "status_code": resp.status, 
        "response": resp.data
    })