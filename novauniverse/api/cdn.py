from __future__ import annotations

import requests

from .errors import *
from .. import config

from . import NovaAPI

class NovaCDN(NovaAPI):
    """Class used to interact with CDN server at ``https://novauniverse.net/cdn/``."""
    def __init__(self, endpoint: str = None, silence_endpoint_warning:bool=False):
        self.silence_endpoint_warning = silence_endpoint_warning

        super().__init__(endpoint)
        self.is_cdn_endpoint()

    def is_cdn_endpoint(self) -> bool:
        """Check if this endpoint link is from the CDN and warns you if it's not."""
        if not self.silence_endpoint_warning:
            if "novauniverse.net/api" in self.endpoint:
                self.logger.warn("You are using an API endpoint in the 'NovaCDN' class. Please only use api endpoints in the 'NovaAPI' class or else you'll run into many bugs.")
                return False
            else:
                return True
        return None

    def get(self) -> requests.Response:
        """Send a get request to that CDN endpoint."""

        if self.endpoint is None: raise NoEndpointPassed()
        if config.performance_mode is False: # Does online check if performance mode is not enabled.
            if self.is_online is False: raise FailedConnectivityCheck()

        self.logger.info(f"Sending cdn get request to '{self.endpoint}'...")
        response_file = self.__http_session.get(self.endpoint)

        if response_file.status_code == 200:
            self.logger.info(f"CDN get request of '{self.endpoint}' was successful!")
            return response_file
        else:
            # I think all the error messages in the CDN are spit out in plain text on HTML. I'm not sure though. (Create a github issue if there's an issue with this anywhere.)
            raise UnSuccessfulOperation(response_file.text)