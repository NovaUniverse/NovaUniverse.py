from __future__ import annotations

from ... import BasicInterface, NovaAPI, Endpoints

from typing import List, Any

from .server_info import ServerInfo
from .nova_online_player import NovaOnlinePlayer

class Server(BasicInterface):
    """
    The interface for NovaAPI's ``/stats/extended`` endpoint.
    Allows you to get all 🌐server stats/info and see which players are 🟢online.
    """
    def __init__(self):
        super().__init__()
        
        self.stats_extended_api = NovaAPI(Endpoints.STATS_EXTENDED)
        self.players_online_api = NovaAPI(Endpoints.PLAYERS_ONLINE)

    def get_stats(self) -> ServerInfo:
        """Get's and returns all server stats."""
        return ServerInfo(self.stats_extended_api.get(), self.players_online_api.get())
    
    def get_online_players(self) -> List[NovaOnlinePlayer]:
        """Returns list of just the online players."""
        return [NovaOnlinePlayer(player_data) for player_data in self.players_online_api.get()["players"]]