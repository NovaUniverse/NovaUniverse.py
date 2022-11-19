import requests

from .errors import *
from .endpoints import Endpoints

from ..info import PACKAGE_NAME

class NovaAPI():
    """The main class that handles all requests to ``https://novauniverse.net/api/``. """

    def __init__(self, endpoint:str=None):
        self.endpoint = endpoint

        self.__http_session = requests.Session()
        self.__http_session.headers["User-Agent"] = PACKAGE_NAME

    @property
    def is_online(self) -> bool:
        try:
            response = self.__http_session.get(Endpoints.connectivity_check)
            success = response.json()["success"]
        except (requests.exceptions.RequestException, KeyError):
            return False

        if success == True:
            return True
        else:
            return False
        

    def get(self):
        """Send a get request to that endpoint."""

        if self.endpoint is None: raise NoEndpointPassed()
        if self.is_online is False: raise FailedConnectivityCheck()

        response_json:dict = self.__http_session.get(self.endpoint).json()

        if response_json.get("success", True):
            return response_json
        else:
            raise UnSuccessfulOperation()