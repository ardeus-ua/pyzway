import unittest
import requests
import zway.controller
import zway.devices


DATA_DEV_BINARY = {
    'creationTime': 1449765074,
    'creatorId': 5,
    'customIcons': {},
    'deviceType': 'switchBinary',
    'h': 1192966519,
    'hasHistory': False,
    'id': 'ZWayVDev_zway_6-0-37',
    'location': 13,
    'metrics': {
        'level': 'on',
        'icon': 'switch',
        'title': 'Examplw Binary Switch',
        'modificationTime': 1488753398,
        'lastLevel': 'off'
    },
    'permanently_hidden': False,
    'probeType': '',
    'tags': ['Light'],
    'visibility': True,
    'updateTime': 1492458033
}

DATA_DEV_RGBW = {
    'creationTime': 1449765079,
    'creatorId': 5,
    'customIcons': {},
    'deviceType': 'switchRGBW',
    'h': -925189473,
    'hasHistory': False,
    'id': 'ZWayVDev_zway_19-0-51-rgb',
    'location': 15,
    'metrics': {
        'icon': 'multilevel',
        'title': 'Example RGB',
        'color': {'r': 24, 'g': 13, 'b': 25},
        'level': 'on',
        'rgbColors': 'rgb(7,29,56)',
        'modificationTime': 1488646141,
        'lastLevel': 'on'
    },
    'permanently_hidden': False,
    'probeType': 'switchColor_rgb',
    'tags': ['Light'],
    'visibility': True,
    'updateTime': 1492453626
}


class TestZwayDevices(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.prefix = "http://localhost/ZAutomation/api/v1"

    def test_create_binary(self):
        dev = zway.devices.SwitchBinary(DATA_DEV_BINARY, self.session, self.prefix)

    def test_create_rgbw(self):
        dev = zway.devices.SwitchRGBW(DATA_DEV_RGBW, self.session, self.prefix)


if __name__ == '__main__':
    unittest.main()
