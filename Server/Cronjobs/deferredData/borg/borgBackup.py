import requests, pprint, logging, json

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

def get_api_token():

    api_token_url = url + "/authentication/signin"

    header = {"Content-Type" : "application/json","Accept":"application/json"}

    r = requests.post(api_token_url,data=json.dumps(credentials), headers=header)
    api_token_json = json.loads(r.content)
    api_token = api_token_json["token"]
    return api_token

def getEpochTime():
    """ SevOne requires epoch in millisecond """
    import time
    timestamp = int(time.time())
    timestamp = str(timestamp) + '000'
    return timestamp

def insertData(apiToken=get_api_token(), value):

    data = [
          {
            "deviceId": 206,
            "indicatorDataDtos": [
              {
                "indicatorId": 12912,
                "value":
                }
            ],
            "objectId": 1580,
            "timestamp": getEpochTime()
          }
        ]

    post_indicatorData = url + "/device-indicators/data"

    header = {
        "Accept":"application/json",
        "X-AUTH-TOKEN":"{}".format(apiToken)
        }

        insertData(apiToken=apiToken, dataDict=getpiHoleApiData())
