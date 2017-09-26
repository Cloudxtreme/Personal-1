import requests
import json
from suds.client import Client
from suds.cache import NoCache

###############################################################
''' SOAP Authentication '''
box = "10.0.0.60"
url = "http://{}/soap3/api.wsdl".format(box)
userName = 'aElchert'
password = ';TuMhmYu3AiNw#2'
###############################################################


###############################################################
# CREATE
###############################################################

def createDevice(deviceIp, objectName, pluginObjectTypeId, pluginIndicatorTypeId):
	'''
	core_createDevice

	return: ID of the new device on success, throws a SOAP exception on failure.
	deprecated: Use core_createDeviceInGroup instead. Add a device to the system. By default, discovery is disabled for this device.
	throws: SoapFault

	integer core_createDevice (string $deviceName, string $deviceIp, integer $peerId, string $deviceDescr)
	string $deviceName: Name of device.
	string $deviceIp: IP address of device.
	integer $peerId: Peer that this device will be added. Specify '-1' to search for the least loaded peer.
	string $deviceDescr: The description of the device.
	'''

	device = client.service.core_createDevice(deviceName, deviceIp, peerId, deviceDescr)
	return device

def createObject(deviceId, objectTypeId, name):
	# ASSOCIATE THE OBJECT ID WITH THE DEVICE
	'''
	plugin_deferred_createObject
	This creates an object.

	return: The ID of the new object type, or 0 on failure.

	integer plugin_deferred_createObject (integer $deviceId, integer $objectTypeId, string $name)
	integer $deviceId: The ID of the device for the object.
	integer $objectTypeId: The ID of the object type for the object.
	string $name: The name of the object. This must be unique per plugin per device.
	'''
	createObject = client.service.plugin_deferred_createObject(deviceId, objectType, name)
	return createObject

def createObjectType(objectName):
	# CREATES THE OBJECT ID
    '''
        plugin_deferred_createObjectType
        This creates an object type.

        return: The ID of the new object type, or 0 on failure.

        access: public
        integer plugin_deferred_createObjectType (integer $osId, string $name, [integer $parentId = null])
        integer $osId: The OS ID for the object type ( no longer used ).
        string $name: The name of the object type; this must be unique per OS.
        integer $parentId: The ID of the parent object type.
        objectType = client.service.plugin_deferred_createObjectType(
                deviceName,
                deviceIp,
                peerId,
                deviceDescr
                )
    '''
    objectType = client.service.plugin_deferred_createObjectType(
        name = objectName,
        parentId = null
    )
    return objectType

def createIndicatorType(objectTypeId, indicatorTypeName):
	# CREATES INDICATORS
	'''
    This creates an indicator type.

    return: The ID of the new indicator type, or 0 on failure.

    integer plugin_deferred_createIndicatorType (integer $objectTypeId, string $name)
    integer $objectTypeId: The ID for the object type to which this applies.
    string $name: The name of the indicator type; this must be unique per object type.
    '''
    #http://10.168.116.253/soap3/docs/Api/SevOneApi.html#methodplugin_deferred_createIndicatorType

	pluginIndicatorType = client.service.plugin_deferred_createIndicatorType(
		objectTypeId, indicatorTypeName)

	return pluginIndicatorType


###############################################################

def enableDeferredPluginForDevice(deviceId, isEnabled=1):
	'''
	plugin_deferred_enablePluginForDevice
	Plugin: DEFERRED.

	This will either enable or disable this plugin for the specified device. If this plugin becomes enabled, it will undergo discovery when the device is discovered. If this plugin is disabled, then all of its objects and historical data will be deleted at the next discovery time for this device.

	return: 1 on success, 0 on failure.
	throws: SoapFault
	access: public
	integer plugin_deferred_enablePluginForDevice (integer $deviceId, integer $isEnabled)
	integer $deviceId: The ID of the device to enable/disable this plugin on.
	integer $isEnabled: Whether to enable this plugin or not.
	'''

	enable = client.service.plugin_deferred_enablePluginForDevice(deviceId, isEnabled)

	return enable

def disableSNMP(deviceId, isEnabled=0):
	'''
	plugin_snmp_enablePluginForDevice
	Plugin: SNMP.

	This will either enable or disable this plugin for the specified device. If this plugin becomes enabled, it will undergo discovery when the device is discovered. If this plugin is disabled, then all of its objects and historical data will be deleted at the next discovery time for this device.

	return: 1 on success, 0 on failure.
	throws: SoapFault
	access: public
	integer plugin_snmp_enablePluginForDevice (integer $deviceId, integer $isEnabled)
	integer $deviceId: The ID of the device to enable/disable this plugin on.
	integer $isEnabled: Whether to enable this plugin or not.
	'''
	snmp = client.service.plugin_snmp_enablePluginForDevice(deviceId, isEnabled)
	return snmp






if __name__ == '__main__':

	newDeviceName = ''
	newDeviceIp = ''
	newObjectName = ''
	newIndicatorName = []

	objectType = createObjectType(newObjectName)

	indicatorType = createIndicatorType(objectType, newIndicatorName)

	newDevice = createDevice(deviceIp, objectName, objectType, indicatorType)

	newObject = createObject(deviceId, objectType, newObjectName)
