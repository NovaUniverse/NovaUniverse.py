from __future__ import annotations

from devgoldyutils import LoggerAdapter, Colours

from .endpoints import Endpoints

from .. import nova_logger
from ..info import PACKAGE_NAME_WITH_VER

from . import cache_dict, errors
from .. import config

if config.py_script_mode:
    from . import pyscript
else:
    import aiohttp

class NovaAsyncAPI():
    """Identical to NovaAPI() but it's asynchronous, WOW OMG."""
    def __init__(self, endpoint: str = None):
        self.endpoint = endpoint
        self.__http_session = cache_dict.get("async_http_session", None)

        if not config.py_script_mode:

            if self.__http_session is None:
                self.__http_session = aiohttp.ClientSession()
                self.__http_session.headers["User-Agent"] = PACKAGE_NAME_WITH_VER

                cache_dict["async_http_session"] = self.__http_session

        self.logger = LoggerAdapter(nova_logger, prefix=Colours.RED.apply("NovaAsyncAPI"))

    @property
    async def is_online(self) -> bool:
        try:
            self.logger.debug("Checking if Nova Universe API is online...")

            if config.py_script_mode:
                response_json = await pyscript.request(self.endpoint, headers = {"User-Agent": PACKAGE_NAME_WITH_VER})
            else:
                response = await self.__http_session.get(Endpoints.connectivity_check)
                response_json = await response.json()

            success = response_json["success"]
        except KeyError:
            return False

        if success:
            self.logger.debug("Yes API is Online!")
            return True
        else:
            return False


    async def get(self) -> dict|list:
        """Send an asynchronous get request to that endpoint."""
        if self.endpoint is None: raise errors.NoEndpointPassed()

        if config.performance_mode is False: 
            # Doesn't do online check if performance mode is enabled.
            if await self.is_online is False: raise errors.FailedConnectivityCheck()

        self.logger.info(f"Sending get request to '{self.endpoint}'...")

        if config.py_script_mode:
            response_json = await pyscript.request(self.endpoint, headers = {"User-Agent": PACKAGE_NAME_WITH_VER})
        else:
            response = await self.__http_session.get(self.endpoint)
            response_json = await response.json()

        self.logger.debug(f"Data from request --> {response_json}")

        if isinstance(response_json, list):
            # If it's a list just return it. (The consistency in this api, smh lol)
            return response_json

        response_json: dict
        if response_json.get("success", True):
            self.logger.info(f"Get request of '{self.endpoint}' was successful!")

            # Log if response was cached.
            if response_json.get("cached"): self.logger.warning(f"This response from '{self.endpoint}' was indicated cached by the API!")

            return response_json
        else:
            # I'm getting message and error here because some endpoints don't error with a message key. (again the consistency in this api 🤬)
            raise errors.UnSuccessfulOperation(response_json.get("message", response_json.get("error")))


    async def close(self) -> None:
        """Closes the asynchronous http session."""
        await self.__http_session.close()