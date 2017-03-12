"""Python module for ZWay Devices"""

import logging
from zway.session import ZWaySession


class GenericDevice(object):
    def __init__(self, zsession: ZWaySession, data: dict):
        self._logger = logging.getLogger(__name__).getChild(self.__class__.__name__)
        self._zsession = zsession
        self.update(data)

    def refresh(self):
        data = self._zsession.get("/devices/" + self.id).json().get('data')
        self.update(data)

    def update(self, data: dict):
        self._data = data
        self.id = self._data['id']
        self.title = self._data['metrics'].get('title')
        self.visible = self._data['visibility']


class SwitchBinary(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, data: dict):
        super().update(data)
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


class SwitchMultilevel(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, data: dict):
        super().update(data)
        self._level = data['metrics']['level']

    @property
    def level(self):
        self.refresh()
        return self._level


class SwitchRGBW(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, data: dict):
        super().update(data)
        if data['metrics']['level'] == 'on':
            self._state = True
        elif data['metrics']['level'] == 'off':
            self._state = False
        else:
            self._state = None
        self._red = data['metrics']['color']['r']
        self._green = data['metrics']['color']['g']
        self._blue = data['metrics']['color']['b']

    @property
    def state(self):
        self.refresh()
        return self._state

    @property
    def rgb(self):
        self.refresh()
        return (self._red, self._green, self._blue)


class SensorBinary(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, data: dict):
        super().update(data)
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


class SensorMultilevel(GenericDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, data: dict):
        super().update(data)
        self._level = data['metrics']['level']
        self._unit = data['metrics']['scaleTitle']

    @property
    def level(self):
        self.refresh()
        return self._level

    @property
    def unit(self):
        self.refresh()
        return self._unit
