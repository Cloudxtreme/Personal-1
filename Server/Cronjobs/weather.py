import json
import urllib2
import requests

""" This script is means to insertData into a already created device, object and indicator"""

wuAPIKey = "744ab92b8cf1baa5"

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)
deviceInfoTemp = {
    "deviceName" : "lancasterWeather",
    "deviceId": 196,
    "pluginIndicatorTypeId": 12908,
    "indicatorId":8357,
    "pluginId": 10,
    "objectId": 1067,
    "pluginObjectTypeId": 1578,
    "subtypeId": 1422
}

def getWeatherInfo():
    """
    Description: Grabs json of lancaster from Weather Underground.
    Returns: Dict of "temperature" and "dewpoint"
    """
    f = urllib2.urlopen('http://api.wunderground.com/api/744ab92b8cf1baa5/geolookup/conditions/q/PA/Lancaster.json')
    jsonObject = f.read()
    parsed_json = json.loads(jsonObject)
    temp = int(parsed_json['current_observation']['temp_f'])
    weatherInfo = {"temperature": temp}
    f.close()
    return weatherInfo

def getEpochTime():
    """ SevOne requires epoch in millisecond """
    import time
    timestamp = int(time.time())
    timestamp = str(timestamp) + '000'
    return timestamp

def get_api_token():
    """This fetches an Authorize API token"""
    api_token_url = url + "/authentication/signin"

    header = {"Content-Type": "application/json",
              "Accept": "application/json"}

    r = requests.post(api_token_url,
                      data=json.dumps(credentials), headers=header, verify=False)
    api_token_json = json.loads(r.content)
    api_token = api_token_json["token"]
    return api_token



def insertData(deviceId, indicatorId, value, objectId, timestamp):
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

    try:
        post_indicatorData = url + "/device-indicators/data"
        header = {
            "Accept":"application/json",
            "X-AUTH-TOKEN":"{}".format(get_api_token())
            }
        r = requests.post(post_indicatorData, headers=header,json=data)
        jsonObject = r.json()
        print(jsonObject)
    except Exception as e:
        print(e)


# # Grab dict of weather data [temp, dewpoint]
weather = getWeatherInfo()

#debug
# print deviceInfoTemp['deviceId'],
# print deviceInfoTemp['indicatorId'],
# print str(weather['temperature']),
# print deviceInfoTemp['objectId'],
# print int(getEpochTime())

# Insert temperature
insertData(
    deviceId = deviceInfoTemp['deviceId'],
    indicatorId =  deviceInfoTemp['indicatorId'],
    value = str(weather['temperature']),
    objectId = deviceInfoTemp['objectId'],
    timestamp = getEpochTime())

writeLog = open('/home/aelchert/Dropbox/Logs/cronLog.txt', 'w')
writeLog.write("[weather.py] - Run")
writeLog.write("\n")
writeLog.close()

if __name__ == "__main__":
    print deviceInfoTemp['deviceId'],
    print deviceInfoTemp['indicatorId'],
    print str(weather['temperature']),
    print deviceInfoTemp['objectId'],
    print int(getEpochTime())
