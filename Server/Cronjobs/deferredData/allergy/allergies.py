import requests, pprint, json 
from termcolor import colored, cprint
from SevOneCommon import *
import mysql.connector
from datetime import datetime

responses = {}
allergyPoints = ['Nose', 'FaceInflamation', 'UpperLung', 'LowerLung', 'Flonase', 'Inhailer', 
'Tiredness', 'DrinksSinceUpdate', 'SmokeNightBefore']

def getQuestion(topicName):
    responseChoices = [str(x) for x in range(0,11)]

    while True:
      topicVar = str(input("{}: ".format(topicName)))

      if topicVar in responseChoices:
          # update dict with value
          cprint("[[ OK ]]\n", 'yellow')
          return({topicName: topicVar})
      else:
          # If not in responses, ask again
          print("Incorrect Input")
          
          # Continue Loop
          continue

    
def insertData(questionsDict):
    
    deviceInfo = { 
        'deviceId': 209, 
        'objectId': 1384, 
        'objectTypeId': 1586, 
        'pluginId': 10,
        'objectType': 1586,
        'objectSubtypes': 1426  
        }

    pluginIndicatorTypeId = {
        'Nose': 12925,
        'FaceInflamation' : 12926,
        'UpperLung': 12927,
        'LowerLung': 12928,
        'Flonase': 12929,
        'Inhailer': 12930,
        'Tiredness': 12931,
        'DrinksSinceUpdate': 12932,
        'SmokeNightBefore': 12933,
        'PollenCount': 12934
      }

    indicatorId = {
      'Nose': 12028,
      'FaceInflamation': 12029,
      'UpperLung': 12030,
      'LowerLung': 12031,
      'Flonase': 12032,
      'Inhailer': 12033,      
      'Tiredness': 12034,
      'DrinksSinceUpdate': 12035,
      'SmokeNightBefore': 12036,
      'PollenCount': 12247
    }

    post_indicatorData = url + "/device-indicators/data"

    header = {
        "Accept":"application/json",
        "X-AUTH-TOKEN":"{}".format(get_api_token())
        }

    currentEpochtime = int(getEpochTime())
    dataDict = [
                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['Nose'],
                      "value": str(questionsDict['Nose'])
                    },
                    {
                      "indicatorId": indicatorId['FaceInflamation'],
                      "value": str(questionsDict['FaceInflamation'])
                    },
                    {
                      "indicatorId": indicatorId['UpperLung'],
                      "value": str(questionsDict['UpperLung'])
                    },
                    {
                      "indicatorId": indicatorId['LowerLung'],
                      "value": str(questionsDict['LowerLung'])
                    },
                    {
                      "indicatorId": indicatorId['Flonase'],
                      "value": str(questionsDict['Flonase'])
                    },
                    {
                      "indicatorId": indicatorId['Inhailer'],
                      "value": str(questionsDict['Inhailer'])
                    },
                    {
                      "indicatorId": indicatorId['Tiredness'],
                      "value": str(questionsDict['Tiredness'])
                    },
                    {
                      "indicatorId": indicatorId['DrinksSinceUpdate'],
                      "value": str(questionsDict['DrinksSinceUpdate'])
                    },
                    {
                      "indicatorId": indicatorId['SmokeNightBefore'],
                      "value": str(questionsDict['SmokeNightBefore'])
                    }, 
                    {
                      "indicatorId": indicatorId['PollenCount'],
                      "value": str(pollenData[0])
                    },
                  ],
                  "objectId": deviceInfo['objectId'],
                  "timestamp": currentEpochtime
                }
              ]

    try:
      r = requests.post(post_indicatorData, headers=header,json=dataDict)
    except:
        print(r.text)


def getPollenData():
  ''' uses pollen.com's api for values '''
  cprint("[[ Getting Pollen.com Data ]]\n", 'green')
  pollenURL = 'https://www.claritinblueskyliving.com/webservice/allergyforecast.php?zip=17602'
  r = requests.get(pollenURL)
  pattern = r.text
  # remove all the slashes in rawJson
  allergyStripped = pattern.replace("\\", " ")
  #remove the first two characters and then last two
  rawJSON = allergyStripped[1:len(allergyStripped) - 1]
  #convert string to  json object
  jsonObject = json.loads(rawJSON)
  # returns float from json
  allergyValueFloat = jsonObject[0]['pollenForecast ']['forecast '][0]
  # multiple float to int value
  allergyValue  = int(allergyValueFloat * 10)
  allergySources = jsonObject[0]['pollenForecast ']['pp ']
  cprint("[[ Pollen Data - OK ]]\n", 'green')
  return([allergyValue, allergySources])

# Run it
if __name__ == '__main__':

  '''
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| Date              | datetime     | NO   |     | NULL    |       |
| Nose              | varchar(2)   | NO   |     | 0       |       |
| FaceInflamation   | varchar(2)   | NO   |     | 0       |       |
| UpperLung         | varchar(2)   | NO   |     | 0       |       |
| LowerLung         | varchar(2)   | NO   |     | 0       |       |
| Flonase           | varchar(2)   | NO   |     | 0       |       |
| Inhailer          | varchar(2)   | NO   |     | 0       |       |
| Tiredness         | varchar(2)   | NO   |     | 0       |       |
| DrinksSinceUpdate | varchar(2)   | NO   |     | 0       |       |
| SmokeNightBefore  | varchar(2)   | NO   |     | 0       |       |
| Comments          | varchar(255) | YES  |     | NULL    |       |
| PollenCount       | varchar(5)   | YES  |     | NULL    |       |
| PollenDetail      | varchar(255) | YES  |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
'''
  print_cyan_on_red("---- Allergy Log ----\n")

  # Ask each question
  for allergy in allergyPoints:
        responses.update(getQuestion(allergy))

#   # insert into mysql database 'allergies'

  cnx = mysql.connector.connect(host='10.0.0.50', user='root', password='CuIeyy7j!!', database='allergies', buffered=True)
  cursor = cnx.cursor()

  # Get comment from user input
  comments = str(input("Comments: "))
  responses.update({"Comments": comments})

  # Get Pollen data from Pollen.com
  pollenData = getPollenData()
  responses.update({'PollenCount': pollenData[0]})
  responses.update({'PollenDetail': pollenData[1]})

  # Inserts the data into SevOne via API
  insertData(responses)

  sql = "INSERT INTO allergies \
       (Date, Nose, FaceInflamation, UpperLung, LowerLung, Flonase, Inhailer, Tiredness, DrinksSinceUpdate, SmokeNightBefore, Comments, PollenCount, PollenDetail) \
       VALUES \
       (NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  dataDict = (responses['Nose'], responses['FaceInflamation'], responses['UpperLung'], responses['LowerLung'], \
        responses['Flonase'], responses['Inhailer'], responses['Tiredness'], responses['DrinksSinceUpdate'], \
        responses['SmokeNightBefore'], responses['Comments'], responses['PollenCount'], responses['PollenDetail'])

  # DEBUG  
  #print("Data Dict: {}".format(dataDict))

  cursor.execute(sql, dataDict)

  cnx.commit()

  cursor.close()
  cnx.close()

  #Print Values to screen
  print("\n")
  cprint("---- Responses ----\n", 'cyan', attrs=['bold'])
  for key,value in sorted(responses.items()):
      print(key, value)
