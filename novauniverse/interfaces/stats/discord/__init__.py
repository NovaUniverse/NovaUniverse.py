from __future__ import annotations

from ... import Interface
from .discord_stats import DiscordStats

class Discord(Interface):
    """
    The interface for NovaAPI's ``/stats/discord`` endpoint.
    Allows you to get 🎮discord stats.
    """
    def __init__(self):
        super().__init__()
        
        self.__stats_discord_api = self.api(self.endpoints.STATS_DISCORD)

    def get_stats(self) -> DiscordStats:
        """Get's and returns all server stats."""
        return DiscordStats(self.__stats_discord_api.get())