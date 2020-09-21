import requests
import json
from flask import Flask
from flask import request
from pprint import pprint
import get
import pathlib

roomId='Y2lzY29zcGFyazovL3VzL1JPT00vNThmM2QwMmUtNzc4ZS0zOWUyLWIzOTctZmZjODA0ZDBmZGRl'
auth_bot_token='NDM5ZDkzZmUtMzA1NS00OGIyLThlMWUtMjliNzVjZTU0YWJkMGExOWEyZTctMjdj_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
webhook_url='https://dnacbot.ngrok.io'
webhook_name='Webhook'

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + auth_bot_token
}

webhook_ini = {
  "name": webhook_name,
  "targetUrl": webhook_url,
  "resource": "messages",
  "event": "created",
  "filter": "roomId="+roomId
}

    
def rest_get(url):
    response = requests.get(url, headers = headers)
    return response

def rest_post(url, data):

    request = requests.post(url, json.dumps(data), headers=headers)
    return request


webhook_created = rest_get('https://api.ciscospark.com/v1/webhooks')
if range(len(webhook_created.json()['items'])) != range(0,0):
    for i in range(len(webhook_created.json()['items'])):
        if webhook_url == webhook_created.json()['items'][i]['targetUrl']:
            print(" \n Webhook will not be created, there is a Webhook already created with the same URL \n")
            break
else:
    print(f"Creating Webhook, with URL:{webhook_url}")
    webhook_creation = rest_post('https://api.ciscospark.com/v1/webhooks', webhook_ini)


def help_me():
    return "I can help. Below are the commands that I understand:\n" \
           "`Help` - I will display what I can do. \n" \
           "`Status` - I will display your DNAC Status \n"
    

app = Flask(__name__)
@app.route('/', methods=['POST'])
def dnacbot():
    if request.method == 'POST':
        webhook = request.get_json()
        if "@webex.bot" not in webhook['data']['personEmail']:
            message_id = webhook['data']['id']
            message = rest_get(f'https://api.ciscospark.com/v1/messages/{message_id}') 
            message = message.json()['text']
            message = message.lower()
            if message == 'help':
                reply_message = help_me()
            elif message == "status":
                reply_message = get.network_health()
            else:
                print("match")
                reply_message = "I have not understand what you are trying to do \n"
            file_data = pathlib.Path.cwd()/'test.doc'
            post_msg =  {"roomId" : roomId,"text" : reply_message,}                
            rest_post('https://api.ciscospark.com/v1/messages', post_msg)           
    return "ok"
app.run(host='localhost', port=3000)              

