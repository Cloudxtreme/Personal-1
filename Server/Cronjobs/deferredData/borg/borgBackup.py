import requests, pprint, json, os

'''
Intention: Script counts files saved by borg and inserts them as a data point
to SevOne

Data Source: borgCount.txt
'''

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

deviceInfo = {
    'deviceId': 210,
    'pluginObjectType': 1580,
    'objectId': 1388,
    'indicator': 12040
}

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

def insertData(value):
    '''post data to API endpoint '''

    if value == 0:
        value = 100

    data = [
          {
            "deviceId": deviceInfo['deviceId'],
            "indicatorDataDtos": [
              {
                "indicatorId": deviceInfo['indicator'],
                "value": str(value)
                }
            ],
            "objectId": deviceInfo['objectId'],
            "timestamp": getEpochTime()
          }
        ]

    post_indicatorData = url + "/device-indicators/data"

    header = {
        "Accept":"application/json",
        "X-AUTH-TOKEN":"{}".format(get_api_token())
        }

    try:
        r = requests.post(post_indicatorData, headers=header, json=data)
        return(r.status_code)
    except:
        print(r.status_code)

def getDataPoint():
    ''' Get's data point from borgCount.txt
    '''
    try:
        f = open('/tmp/borgReturnValue.txt', 'r')
    except:
        raise

    return(f.read(1))

print(insertData(getDataPoint()))


# dataPoint = getDataPoint()

# insertData(dataPoint)
print(insertData(getDataPoint()))
