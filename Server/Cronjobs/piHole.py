import requests, pprint, logging

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

piHoleUrl = 'http://10.0.0.49'

logger = logging.getLogger('piHoleData')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('/home/aelchert/Dropbox/Logs/piHoleData.txt')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)


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

def insertData(apiToken, deviceId, indicatorId, value, objectId, timestamp):
    data = [
          {
            "deviceId": deviceId,
            "indicatorDataDtos": [
              {
                "indicatorId": indicatorId,
                "value": value
              }
            ],
            "objectId": objectId,
            "timestamp": timestamp
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
        logger.info('Error at: %s', r.text)

'''
*************************** 1. row ***************************
                      id: 8912
               device_id: 203
               object_id: 1109
               plugin_id: 10
plugin_indicator_type_id: 12913
              is_enabled: 1
           is_baselining: 1
              is_deleted: 0
             column_name: p1i8912
           maximum_value: 0
                  format: GAUGE
has_precalculated_deltas: 0
  last_invalidation_time: 0
    synthetic_expression: NULL
        evaluation_order: 1
*************************** 2. row ***************************
                      id: 8913
               device_id: 203
               object_id: 1109
               plugin_id: 10
plugin_indicator_type_id: 12914
              is_enabled: 1
           is_baselining: 1
              is_deleted: 0
             column_name: p1i8913
           maximum_value: 0
                  format: GAUGE
has_precalculated_deltas: 0
  last_invalidation_time: 0
    synthetic_expression: NULL
        evaluation_order: 1
'''

indicatorIds = {"domains_being_blocked": 12913, "dns_queries_today": 12914}

piHoleData = getpiHoleApiData()

token = get_api_token()

# Insert temperature
insertData(
    apiToken=token,
    deviceId = 203,
    indicatorId =  indicatorIds['domains_being_blocked'],
    value = piHoleData['domains_being_blocked'],
    objectId = 1109,
    timestamp = getEpochTime())

logger.info('Data Entered for %s', piHoleData['domains_being_blocked'])

insertData(
    apiToken=token,
    deviceId = 203,
    indicatorId =  indicatorIds['dns_queries_today'],
    value = piHoleData['dns_queries_today'],
    objectId = 1109,
    timestamp = getEpochTime())

logger.info('Data Entered for %s', piHoleData['dns_queries_today'])
