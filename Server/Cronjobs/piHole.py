import requests, pprint, logging, json

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

piHoleUrl = 'http://10.0.0.49/admin/api.php'

def get_api_token():

    api_token_url = url + "/authentication/signin"

    header = {"Content-Type" : "application/json","Accept":"application/json"}

    r = requests.post(api_token_url,data=json.dumps(credentials), headers=header)
    api_token_json = json.loads(r.content)
    api_token = api_token_json["token"]
    return api_token


def getpiHoleApiData():
    r = requests.get(piHoleUrl)
    data = r.json()

    dataDict = {'ads_blocked_today': data['ads_blocked_today'],
    'ads_percentage_today': data['ads_percentage_today'],
    'dns_queries_today': data['dns_queries_today'],
    'domains_being_blocked': data['domains_being_blocked'],
    'queries_cached': data['queries_cached'],
    'queries_forwarded': data['queries_forwarded'],
    'unique_clients': data['unique_clients'],
    'unique_domains': data['unique_domains']}

    return dataDict

def getEpochTime():
    """ SevOne requires epoch in millisecond """
    import time
    timestamp = int(time.time())
    timestamp = str(timestamp) + '000'
    return timestamp

def insertData(apiToken, dataDict):

    '''

    +-------+-----------------------+
    | id    | name                  |
    +-------+-----------------------+        |
    | 12915 | ads_blocked_today     |
    | 12916 | queries_forwarded     |
    | 12917 | dns_queries_today     |
    | 12918 | queries_cached        |
    | 12919 | unique_domains        |
    | 12920 | unique_clients        |
    | 12921 | domains_being_blocked |
    | 12922 | ads_percentage_today  |
    +-------+-----------------------+

    +--------------+--------------------------+
    | indicator_id | plugin_indicator_type_id |
    +--------------+--------------------------+
    |         8923 |                    12915 |
    |         8924 |                    12916 |
    |         8925 |                    12917 |
    |         8926 |                    12918 |
    |         8927 |                    12919 |
    |         8928 |                    12920 |
    |         8929 |                    12921 |
    |         8930 |                    12922 |
    +--------------+--------------------------+
    '''

    data = [
          {
            "deviceId": 204,
            "indicatorDataDtos": [
              {
                "indicatorId": 8923,
                "value": dataDict['ads_blocked_today']
              },
              {
                "indicatorId": 8924,
                "value": dataDict['queries_forwarded']
              },
              {
                "indicatorId": 8925,
                "value": dataDict['dns_queries_today']
              },
              {
                "indicatorId": 8926,
                "value": dataDict['queries_cached']
              },
              {
                "indicatorId": 8927,
                "value": dataDict['unique_domains']
              },
              {
                "indicatorId": 8928,
                "value": dataDict['unique_clients']
              },
              {
                "indicatorId": 8929,
                "value": dataDict['domains_being_blocked']
              },
            {
              "indicatorId": 8930,
              "value": dataDict['ads_percentage_today']
            }
            ],
            "objectId": 1112,
            "timestamp": getEpochTime()
          }
        ]

    post_indicatorData = url + "/device-indicators/data"

    header = {
        "Accept":"application/json",
        "X-AUTH-TOKEN":"{}".format(apiToken)
        }

    try:
        r = requests.post(post_indicatorData, headers=header,json=data)
    except:
        print r.text



indicatorIds = {"domains_being_blocked": 8912, "dns_queries_today": 8913}


insertData(apiToken=get_api_token(), dataDict=getpiHoleApiData())


if __name__ == '__main__':
    for k,v in etpiHoleApiData().items():
        print(k,v)
