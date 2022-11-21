import requests

from .errors import *
from .endpoints import Endpoints

from .. import nova_logger
from ..info import PACKAGE_NAME_WITH_VER

class NovaAPI():
    """The main class that handles all requests to ``https://novauniverse.net/api/``. """

    def __init__(self, endpoint:str=None):
        self.endpoint = endpoint

        self.__http_session = requests.Session()
        self.__http_session.headers["User-Agent"] = PACKAGE_NAME_WITH_VER

        self.__logger = nova_logger

    @property
    def is_online(self) -> bool:
        try:
            self.__logger.debug("Checking if Nova Universe API is online...")

            response = self.__http_session.get(Endpoints.connectivity_check)
            success = response.json()["success"]
        except (requests.exceptions.RequestException, KeyError):
            return False

        if success:
            self.__logger.debug("Yes API is Online!")
            return True
        else:
            return False
        

    def get(self):
        """Send a get request to that endpoint."""

        if self.endpoint is None: raise NoEndpointPassed()
        if self.is_online is False: raise FailedConnectivityCheck()

        self.__logger.info(f"Sending get request to '{self.endpoint}'...")
        response_json:dict = self.__http_session.get(self.endpoint).json()

        if response_json.get("success", True):
            self.__logger.info(f"Get request of '{self.endpoint}' was successful!")

            # Log if response was cached.
            if response_json.get("cached"): self.__logger.warning(f"This response from '{self.endpoint}' was indicated cached by the API!")

            return response_json
        else:
            raise UnSuccessfulOperation()