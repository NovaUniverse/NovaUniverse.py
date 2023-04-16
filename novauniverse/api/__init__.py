from __future__ import annotations

import requests
from devgoldyutils import LoggerAdapter

from . import errors
from .endpoints import Endpoints

from .. import nova_logger
from ..info import PACKAGE_NAME_WITH_VER

from .. import config

cache_dict = {
    "http_session": None,
    "async_http_session": None
}

class NovaAPI():
    """The main class that handles all requests to the web server at ``https://novauniverse.net/api/``. """
    def __init__(self, endpoint:str=None):
        self.endpoint:str = endpoint
        
        self.__http_session = cache_dict.get("http_session", None)

        if self.__http_session is None:
            self.__http_session = requests.Session()
            self.__http_session.headers["User-Agent"] = PACKAGE_NAME_WITH_VER
            
            cache_dict["http_session"] = self.__http_session

        self.logger = LoggerAdapter(nova_logger, prefix="NovaAPI")

    @property
    def is_online(self) -> bool:
        try:
            self.logger.debug("Checking if Nova Universe API is online...")

            response = self.__http_session.get(Endpoints.connectivity_check)
            success = response.json()["success"]
        except (requests.exceptions.RequestException, KeyError):
            return False

        if success:
            self.logger.debug("Yes API is Online!")
            return True
        else:
            return False


    def get(self) -> dict|list:
        """Send a get request to that endpoint."""
        if self.endpoint is None: raise errors.NoEndpointPassed()
        if config.py_script_mode is True: raise errors.OnlyAsyncSupportedOnPyScript()

        if config.performance_mode is False: 
            # Doesn't do online check if performance mode is enabled.
            if self.is_online is False: raise errors.FailedConnectivityCheck()

        self.logger.info(f"Sending get request to '{self.endpoint}'...")
        response_json = self.__http_session.get(self.endpoint).json()
        self.logger.debug(f"Data from request --> {response_json}")

        if isinstance(response_json, list):
            # If it's a list just return it. (The consistency in this api, smh lol)
            return response_json

        response_json:dict
        if response_json.get("success", True):
            self.logger.info(f"Get request of '{self.endpoint}' was successful!")

            # Log if response was cached.
            if response_json.get("cached"): self.logger.warning(f"This response from '{self.endpoint}' was indicated cached by the API!")

            return response_json
        else:
            # I'm getting message and error here because some endpoints don't error with a message key. (again the consistency in this api 🤬)
            raise errors.UnSuccessfulOperation(response_json.get("message", response_json.get("error")))


from .cdn import NovaCDN
from .async_api import NovaAsyncAPI