import requests, pprint, json, os

'''
Intention: Script counts files saved by borg and inserts them as a data point
to SevOne

Data Source: borgCount.txt
'''

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

def insertData():
    '''post data to API endpoint '''

    data = [
          {
            "deviceId": 210,
            "indicatorDataDtos": [
              {
                "indicatorId": 9854,
                "value": getDataPoint()
                }
            ],
            "objectId": 1174,
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
    except:
        print(r.text)

def getDataPoint():
    ''' Get's data point from borgCount.txt
    '''
    try:
        f = open('/tmp/borgReturnValue.txt', 'r')
    except:
        raise

    return(f.read(1))

print(getDataPoint())

#insertData()

# Output data to console if run manually
if __name__ == "__main__":
    print("\n")
    print("BorgCount: ")
    print("Current Epoch Time: {}".format(getEpochTime()))
    print("File Count: {}".format(getDataPoint()))
