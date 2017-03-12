"""Python module for ZWay"""

import logging
from zway.session import ZWaySession
import zway.devices


class Controller(object):
    def __init__(self,
                 baseurl: str,
                 username: str=None,
                 password: str=None):
        self._logger = logging.getLogger(__name__).getChild(self.__class__.__name__)
        self._zsession = ZWaySession(baseurl, username, password)

    @property
    def devices(self):
        return self.get_all_devices()

    def get_all_devices(self):
        response = self._zsession.get("/devices")
        all_devices = []
        for device_dict in response.json().get('data').get('devices'):
            device_type = device_dict['deviceType']
            if device_dict['permanently_hidden']:
                continue
            if device_type == 'switchBinary':
                all_devices.append(zway.devices.SwitchBinary(self._zsession, device_dict))
            elif device_type == 'switchMultilevel':
                all_devices.append(zway.devices.SwitchMultilevel(self._zsession, device_dict))
            elif device_type == 'switchRGBW':
                all_devices.append(zway.devices.SwitchRGBW(self._zsession, device_dict))
            elif device_type == 'sensorBinary':
                all_devices.append(zway.devices.SensorBinary(self._zsession, device_dict))
            elif device_type == 'sensorMultilevel':
                all_devices.append(zway.devices.SensorMultilevel(self._zsession, device_dict))
            else:
                all_devices.append(zway.devices.GenericDevice(self._zsession, device_dict))
        return all_devices
