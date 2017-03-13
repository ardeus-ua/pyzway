"""Python module for ZWay Devices"""

import logging
from zway.session import ZWaySession


class GenericDevice(object):
    def __init__(self, data: dict, zsession: ZWaySession):
        self._logger = logging.getLogger(__name__).getChild(self.__class__.__name__)
        self._zsession = zsession
        self.update_attrs(data)

    def refresh(self):
        data = self._zsession.get("/devices/" + self.id).json().get('data')
        self.update_attrs(data)

    def update_attrs(self, data: dict):
        self._data = data
        self.id = self._data['id']
        self.title = self._data['metrics'].get('title')
        self.visible = self._data['visibility']


class GenericBinaryDevice(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update_attrs(self, data: dict):
        super().update_attrs(data)
        if data['metrics']['level'] == 'on':
            self._state = True
        elif data['metrics']['level'] == 'off':
            self._state = False
        else:
            self._state = None

    @property
    def state(self):
        self.refresh()
        return self._state


class GenericMultiLevelDevice(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update_attrs(self, data: dict):
        super().update_attrs(data)
        self._level = data['metrics']['level']

    @property
    def level(self):
        self.refresh()
        return self._level


class SwitchBinary(GenericBinaryDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SwitchMultilevel(GenericMultiLevelDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SwitchRGBW(SwitchBinary):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update_attrs(self, data: dict):
        super().update_attrs(data)
        self._red = data['metrics']['color']['r']
        self._green = data['metrics']['color']['g']
        self._blue = data['metrics']['color']['b']

    @property
    def rgb(self):
        self.refresh()
        return (self._red, self._green, self._blue)


class SensorBinary(GenericBinaryDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SensorMultilevel(GenericMultiLevelDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update_attrs(self, data: dict):
        super().update_attrs(data)
        self._unit = data['metrics']['scaleTitle']
