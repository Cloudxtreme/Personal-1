import requests
import json

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

def get_api_token():

    api_token_url = url + "/authentication/signin"

    header = {"Content-Type" : "application/json","Accept":"application/json"}

    r = requests.post(api_token_url,data=json.dumps(credentials), headers=header)
    api_token_json = r.json()
    api_token = api_token_json["token"]
    return api_token

def getEpochTime():
    """ SevOne requires epoch in millisecond """
    import time
    timestamp = int(time.time())
    timestamp = str(timestamp) + '000'
    return timestamp
