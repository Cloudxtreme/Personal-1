import requests, pprint, json, termcolor import colored, cprint

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

def getQuestions():
    """ P
    rompt to answer the questions """

    allergyPoints = [ 'Nose', 'Throat', 'UpperLung', 'LowerLung', 'Flonase', 
                      'Inhailer', 'Tiredness', 'DrinksNightBefore' 'SmokeNightBefore']
    responseChoices = ['0', '1', '2', '3', '4', '5', '6']
    responses = {}

    print("\n")
    cprint("Allergy Input: ", 'red', attrs=['bold'])
    print("\n")
  
    ###################
    # Nose
    ###################

    while True:
      Nose = str(input("Nose: "))

      if Nose in responseChoices:
          
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
          responses.update({"Nose": Nose})
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
      Throat = str(input("Throat: "))

      if Throat in responseChoices:
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
          responses.update({"Throat": Throat})
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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
          ''' update dict with Nose value '''
          cprint("\n[[ OK ]]\n", 'yellow')
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

    pluginIndicatorTypeId = {
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
      'Flonase': 12032,
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
                      "indicatorId": indicatorId['DrinksNightBefore'],
                      "value": str(questionsDict['DrinksNightBefore'])
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

    print(dataDict)

    try:
      r = requests.post(post_indicatorData, headers=header,json=dataDict)

    except:
        print(r.text)

questionsDict = getQuestions()
print(insertData(questionsDict))


