from suds.import Client
from suds.cache import NoCache
import socket

# MUST RUN SevOne-api-change-ip on the box before this work with
# an internal box!

box = "s5310"
url = "http://{}/soap3/api.wsdl".format(box)

def authenticate(applianceIP, userName, password):
	try:
		client = Client(url, cache=NoCache())
		result = client.service.authenticate(userName,password)
		print('Client established')
	except:
		#print: "Exception: {}".format(e)
		print('Could not establish the client')
		exit()
	return client

def core_getDevices():
    devices = client.service.core_getDevices()
    return devices

def createDevice(deviceName,deviceIp,peerId,deviceDescr):
    deviceInGroup = client.service.core_createDevice(
        deviceName,
        deviceIp,
        peerId,
        deviceDescr
        )
    #print "from createDevice: {}".format(deviceInGroup)
    return deviceInGroup

def getDeviceIdByName(deviceName):
    deviceId = client.service.core_getDeviceIdByName(deviceName)
    #print "from getDeviceIdByName: {}".format(deviceId)
    return deviceId

def rediscoverDevice(deviceId):
    discoverDevice = client.service.core_rediscoverDevice(deviceId,1)
    #print "from core_setDeviceDiscovery: {}".format(deviceId)
    return discoverDevice

def getDeviceGroups():
    groups = client.service.core_getDeviceGroups()
    return groups


if __name__ == '__main__':
	client = authenticate(url,'aelchert','sevone')
	a = core_getDevices()
	print(a)
