from __future__ import annotations

from ....utils.search import Search, SearchBy
from ... import Interface, InterfaceObject

from typing import List, Any

from .server_info import ServerInfo

class Server(Interface):
    """
    The interface for NovaAPI's ``/stats/extended`` endpoint.
    Allows you to get all 🌐server stats/info and see which players are 🟢online.
    """
    def __init__(self):
        super().__init__()
        
        self.__stats_extended_api = self.api(self.endpoints.STATS_EXTENDED)

    def get_stats(self) -> ServerInfo:
        """Get's and returns all server stats."""
        return ServerInfo(self.__stats_extended_api.get())