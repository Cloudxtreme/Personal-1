import requests, pprint, json 
from termcolor import colored, cprint
from SevOneCommon import *
import pymysql.cursors

responses = {}
allergyPoints = ['Nose', 'Throat', 'UpperLung', 'LowerLung', 'Flonase', 'Inhailer', 
'Tiredness', 'DrinksSinceUpdate', 'SmokeNightBefore']

def getQuestion(topicName):
    responseChoices = [str(x) for x in range(0,11)]

    while True:
      topicVar = str(input("{}: ".format(topicName)))

      if topicVar in responseChoices:
          ''' update dict with value '''
          cprint("[[ OK ]]\n", 'yellow')
          return({topicName: topicVar})
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
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
        'Throat' : 12926,
        'UpperLung': 12927,
        'LowerLung': 12928,
        'Flonase': 12929,
        'Inhailer': 12930,
        'Tiredness': 12931,
        'DrinksSinceUpdate': 12932,
        'SmokeNightBefore': 12933
      }

    indicatorId = {
      'Nose': 12028,
      'Throat': 12029,
      'UpperLung': 12030,
      'LowerLung': 12031,
      'Flonase': 12032,
      'Inhailer': 12033,      
      'Tiredness': 12034,
      'DrinksSinceUpdate': 12035,
      'SmokeNightBefore': 12036
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
                      "indicatorId": indicatorId['Throat'],
                      "value": str(questionsDict['Throat'])
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
                    }
                  ],
                  "objectId": deviceInfo['objectId'],
                  "timestamp": currentEpochtime
                }
              ]

    try:
      r = requests.post(post_indicatorData, headers=header,json=dataDict)

    except:
        print(r.text)


# Run it
if __name__ == '__main__':

    # Insert Data into SevOne
    for allergy in allergyPoints:
        responses.update(getQuestion(allergy))
    
    insertData(responses)

    ''' insert into mysql database 'allergies' '''

    connection = pymysql.connect(
                host='localhost',
                password='CuIeyy7j!!',
                db='allergies',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

    comment = str(input("Comment: "))

    try:
      with connection.cursor() as cursor:
        for allergy in allergyPoints:
          sql = "INSERT INTO 'allergies' (%s) VALUES (%s)"
          cursor.execute(sql, (allergy, responses[allergy]))
        cursor.execute(sql, "Comments", comment)
        
    finally:
      connection.close()
    
    # Print Values to screen
    for key,value in responses.items():
        print(key, value)




