"""ZWay Session"""

import logging
import requests


_LOGGER = logging.getLogger(__name__)


class ZWaySession(object):
    def __init__(self,
                 baseurl: str,
                 username: str=None,
                 password: str=None):
        self._baseurl = baseurl
        self._session = requests.Session()
        self._session.auth = (username, password)

    def get(self, path):
        _LOGGER.debug("GET " + path)
        request_uri = self.apipath + path
        return self._session.get(request_uri)

    @property
    def apipath(self):
        return self._baseurl + "/ZAutomation/api/v1"
