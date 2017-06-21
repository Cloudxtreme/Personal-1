import json
import urllib2
import requests
import logging

""" This script is means to insertData into a already created device, object and indicator"""

wuAPIKey = "744ab92b8cf1baa5"
nmsApiKey = "eyJhbGciOiJIUzUxMiJ9eyJpc3MiOiJhRWxjaGVydCJ9HkQoTnHgFDKaWKZ38J3IQYaI3z53grlr1Z7VSDOLbttN_rA2fWz662InGgvH-yJT-fW0eDpYVvogzk452XWCLQ"

ip = "10.0.0.60"
credentials = {"name": "aElchert", "password": ";TuMhmYu3AiNw#2"}
url = 'http://{}/api/v1'.format(ip)

logger = logging.getLogger('weather')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('/home/aelchert/Dropbox/Logs/dewLog.txt')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

deviceInfoTemp = {
    "deviceId": 196,
    "pluginIndicatorTypeId": 12908,
    "indicatorId":8357,
    "pluginId": 10,
    "objectId": 1067,
    "pluginObjectTypeId": 1578,
    "subtypeId": 1422
}

deviceInfoDew = {
    "deviceId": 196,
    "pluginIndicatorTypeId": 12908,
    "indicatorId":8495,
    "pluginId": 10,
    "objectId": 1080,
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
    dew = int(parsed_json['current_observation']['dewpoint_f'])
    weatherInfo = {"temperature": temp, "dewpoint": dew}
    f.close()
    return weatherInfo

def getEpochTime():
    """ SevOne requires epoch in millisecond """
    import time
    timestamp = int(time.time())
    timestamp = str(timestamp) + '000'
    return timestamp

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

    post_indicatorData = url + "/device-indicators/data"
    header = {
        "Accept":"application/json",
        "X-AUTH-TOKEN":"{}".format(nmsApiKey)
        }
    r = requests.post(post_indicatorData, headers=header,json=data)
    print r.text

# # Grab dict of weather data [temp, dewpoint]
weather = getWeatherInfo()


# Insert temperature
insertData(
    deviceId = deviceInfoTemp['deviceId'],
    indicatorId =  deviceInfoTemp['indicatorId'],
    value = str(weather['temperature']),
    objectId = deviceInfoTemp['objectId'],
    timestamp = getEpochTime())


insertData(
    deviceId = deviceInfoDew['deviceId'],
    indicatorId =  deviceInfoDew['indicatorId'],
    value = str(weather['dewpoint']),
    objectId = deviceInfoDew['objectId'],
    timestamp = getEpochTime())

dewPointLog = str(weather['dewpoint'])
logger.debug('Value: %s', dewPointLog)


if __name__ == "__main__":
    print "\n"
    print "Temp for Lancaster: "
    print "Device ID: {}".format(deviceInfoTemp['deviceId'])
    print "Indicator ID: {}".format(deviceInfoTemp['indicatorId'])
    print "Temp in F:  {}".format(str(weather['temperature']))
    print "Object ID: {} ".format(deviceInfoTemp['objectId'])
    print "Epoch Time: {} {}".format(int(getEpochTime()), '\n')

    print "Temp for Lancaster:"
    print "Device ID: {}".format(deviceInfoDew['deviceId'])
    print "Indicator ID: {}".format(deviceInfoDew['indicatorId'])
    print "Dew Point: {}".format(str(weather['dewpoint']))
    print "Object ID: {}".format(deviceInfoDew['objectId'])
    print "Epoch Time: {} {}".format(int(getEpochTime()), '\n')
