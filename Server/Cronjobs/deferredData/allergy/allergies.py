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

def getQuestions():
    """ P
    rompt to answer the questions """

    allergyPoints = [ 'Nose', 'Throat', 'UpperLung', 'LowerLung', 'Flonase', 
                      'Inhailer', 'Tiredness', 'DrinksNightBefore' 'SmokeNightBefore']
    responseChoices = ['0', '1', '2', '3', '4', '5', '6']
    responses = {}
  
    ###################
    # Nose
    ###################

    while True:
      nose = str(input("Nose: "))

      if nose in responseChoices:
          
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"Nose": nose})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # Throat
    ###################

    while True:
      throat = str(input("Throat: "))

      if throat in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"throat": throat})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # UpperLung
    ###################

    while True:
      UpperLung = str(input("UpperLung: "))

      if UpperLung in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"UpperLung": UpperLung})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # LowerLung
    ###################

    while True:
      LowerLung = str(input("LowerLung: "))

      if LowerLung in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"LowerLung": LowerLung})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # Flonase
    ###################

    while True:
      Flonase = str(input("Flonase: "))

      if Flonase in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"Flonase": Flonase})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # Inhailer
    ###################

    while True:
      Inhailer = str(input("Inhailer: "))

      if Inhailer in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"Inhailer": Inhailer})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # Tiredness
    ###################

    while True:
      Tiredness = str(input("Tiredness: "))

      if Tiredness in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"Tiredness": Tiredness})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # DrinksNightBefore
    ###################

    while True:
      DrinksNightBefore = str(input("DrinksNightBefore: "))

      if DrinksNightBefore in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"DrinksNightBefore": DrinksNightBefore})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue

    ###################
    # SmokeNightBefore
    ###################

    while True:
      SmokeNightBefore = str(input("SmokeNightBefore: "))

      if SmokeNightBefore in responseChoices:
          ''' update dict with nose value '''
          print("\n[[ OK ]]\n")
          responses.update({"SmokeNightBefore": SmokeNightBefore})
          ''' break loop '''
          break
      else:
          ''' If not in responses, ask again '''
          print("Incorrect Input")
          
          ''' continue loop '''
          continue
  
    return responses
    
def insertData(questionsDict):
    
    deviceInfo = { 
        'deviceId': 209, 
        'objectId': 1384, 
        'objectTypeId': 1586, 
        'pluginId': 10,
        'objectType': 1586,
        'objectSubtypes': 1426  
        }

    objectTypeId = {
        'Nose': 12925,
        'Throat' : 12926,
        'UpperLung': 12927,
        'LowerLung': 12928,
        'Flonase': 12929,
        'Inhailer': 12930,
        'Tiredness': 12931,
        'DrinksNightBefore': 12932,
        'SmokeNightBefore': 12933
      }

    indicatorId = {
      'Nose': 12028,
      'Throat': 12029,
      'UpperLung': 12030,
      'LowerLung': 12031,
      'Flonsase': 12032,
      'Inhailer': 12033,      
      'Tiredness': 12034,
      'DrinksNightBefore': 12035,
      'SmokeNightBefore': 12036
    }

    post_indicatorData = url + "/device-indicators/data"

    header = {
        "Accept":"application/json",
        "X-AUTH-TOKEN":"{}".format(get_api_token())
        }
    currentEpochtime = getEpochTime()
    dataDict = [
                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['Nose'],
                      "value": str(questionsDict['Nose'])
                    }
                  ],
                  "objectId": objectTypeId['Nose'],
                  "timestamp": currentEpochtime
                },
                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['Throat'],
                      "value": str(questionsDict['Throat'])
                    }
                  ],
                  "objectId": objectTypeId['Throat'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['UpperLung'],
                      "value": str(questionsDict['UpperLung'])
                    }
                  ],
                  "objectId": objectTypeId['UpperLung'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['LowerLung'],
                      "value": str(questionsDict['LowerLung'])
                    }
                  ],
                  "objectId": objectTypeId['LowerLung'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['Flonase'],
                      "value": str(questionsDict['Flonase'])
                    }
                  ],
                  "objectId": objectTypeId['Flonase'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['Inhailer'],
                      "value": str(questionsDict['Inhailer'])
                    }
                  ],
                  "objectId": objectTypeId['Inhailer'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['Tiredness'],
                      "value": str(questionsDict['Tiredness'])
                    }
                  ],
                  "objectId": objectTypeId['Tiredness'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['DrinksNightBefore'],
                      "value": str(questionsDict['DrinksNightBefore'])
                    }
                  ],
                  "objectId": objectTypeId['DrinksNightBefore'],
                  "timestamp": currentEpochtime
                },
                                {
                  "deviceId": deviceInfo['deviceId'],
                  "indicatorDataDtos": [
                    {
                      "indicatorId": indicatorId['SmokeNightBefore'],
                      "value": str(questionsDict['SmokeNightBefore'])
                    }
                  ],
                  "objectId": objectTypeId['SmokeNightBefore'],
                  "timestamp": currentEpochtime
                }
              ]

    try:
      r = requests.post(post_indicatorData, headers=header,json=dataDict)

    except:
        print(r.text)

questionsDict = getQuestions()
print(insertData(questionsDict))


