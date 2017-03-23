"""Python module for ZWay"""

import logging
from zway.session import ZWaySession
import zway.devices


_LOGGER = logging.getLogger(__name__)


class Controller(object):
    def __init__(self,
                 baseurl: str,
                 username: str=None,
                 password: str=None):
        self._zsession = ZWaySession(baseurl, username, password)

    @property
    def devices(self):
        return self._get_all_devices()

    def _get_all_devices(self):
        response = self._zsession.get("/devices")
        all_devices = []
        for device_dict in response.json().get('data').get('devices'):
            device_type = device_dict['deviceType']
            if device_dict['permanently_hidden']:
                continue
            if device_type == 'switchBinary':
                all_devices.append(zway.devices.SwitchBinary(device_dict, self._zsession))
            elif device_type == 'switchMultilevel':
                all_devices.append(zway.devices.SwitchMultilevel(device_dict, self._zsession))
            elif device_type == 'switchRGBW':
                all_devices.append(zway.devices.SwitchRGBW(device_dict, self._zsession))
            elif device_type == 'sensorBinary':
                all_devices.append(zway.devices.SensorBinary(device_dict, self._zsession))
            elif device_type == 'sensorMultilevel':
                all_devices.append(zway.devices.SensorMultilevel(device_dict, self._zsession))
            else:
                all_devices.append(zway.devices.GenericDevice(device_dict, self._zsession))
        return all_devices
