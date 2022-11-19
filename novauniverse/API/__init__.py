import requests
from .endpoints import Endpoints

from ..errors import NovaError
from ..info import PACKAGE_NAME

class NovaAPIError(NovaError):
    """Error raised when a known error occurs on the API."""
    def __init__(self, message:str) -> None:
        super().__init__(message)


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

        pass

    
