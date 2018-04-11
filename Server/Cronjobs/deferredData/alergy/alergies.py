import requests, pprint, logging, json

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

#logger = logging.getLogger('piHole')
#logger.setLevel(logging.INFO)

#handler = logging.FileHandler('/home/aelchert/Dropbox/Logs/piHoleLog.txt')
#handler.setLevel(logging.INFO)

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)

# add the handlers to the logger
#logger.addHandler(handler)

def get_api_token():

    api_token_url = url + "/authentication/signin"

    header = {"Content-Type" : "application/json","Accept":"application/json"}

    r = requests.post(api_token_url,data=json.dumps(credentials), headers=header)
    api_token_json = json.loads(r.content)
    api_token = api_token_json["token"]
    return api_token


def getpiHoleApiData():


def getEpochTime():
    """ SevOne requires epoch in millisecond """
    import time
    timestamp = int(time.time())
    timestamp = str(timestamp) + '000'
    return timestamp

def insertData(apiToken, dataDict):
    
    deviceinfo = { 'deviceId': 209, 'objectId': 1382, 'objectTypeId': 1586 }
    '''
   
mysql (data)> select * from objectsubtypes where name='Allergies';
+------+-----------+-------------+--------+-----------+-------------+
| id   | plugin_id | object_type | common | name      | description |
+------+-----------+-------------+--------+-----------+-------------+
| 1426 |        10 |        1586 |      0 | Allergies |             |
+------+-----------+-------------+--------+-----------+-------------+

mysql (data)> select id, plugin_object_type_id, name from plugin_indicator_type where plugin_id=10;
| 12925 |                  1586 | Nose                  |
| 12926 |                  1586 | Throat                |
| 12927 |                  1586 | UpperLung             |
| 12928 |                  1586 | LowerLung             |
| 12929 |                  1586 | Flonase               |
| 12930 |                  1586 | Inhailer              |
| 12931 |                  1586 | Tiredness             |
| 12932 |                  1586 | DrinksNightBefore     |
| 12933 |                  1586 | SmokeNightBefore      |
+-------+-----------------------+-----------------------+


ObjectID: 1382
    '''

    data = [
          {
            "deviceId": 209
            ,
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
        logger.info('insertData: %s', data)
        r = requests.post(post_indicatorData, headers=header,json=data)
    except:
        logger.info('insertData Error: %s', r.text)
        print r.text

insertData(apiToken=get_api_token(), dataDict=getpiHoleApiData())

if __name__ == '__main__':
    for k,v in getpiHoleApiData().items():
        print(k,v)
