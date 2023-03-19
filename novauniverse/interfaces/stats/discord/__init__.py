from __future__ import annotations

from ... import BasicInterface, NovaAPI, Endpoints
from .discord_stats import DiscordStats

class Discord(BasicInterface):
    """
    The interface for NovaAPI's ``/stats/discord`` endpoint.
    Allows you to get 🎮discord stats.
    """
    def __init__(self):
        super().__init__()
        
        self.api = NovaAPI(Endpoints.STATS_DISCORD)

    def get_stats(self) -> DiscordStats:
        """Get's and returns all server stats."""
        return DiscordStats(self.api.get())