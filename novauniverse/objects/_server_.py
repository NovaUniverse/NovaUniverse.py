from datetime import datetime
from .. import API

class BasicServer(object):
    """Class for basic server stats."""
    def __init__(self, ENDPOINT:str, ENDPOINT_2:str, cached:bool):
        self.ENDPOINT = ENDPOINT
        self.ENDPOINT_2 = ENDPOINT_2

        self._cached = cached

    @property
    def player_count(self) -> int:
        """The amount of players on the network right now. (LIVE)"""
        return int(API.update(self, "player_count"))

    @property
    def server_count(self) -> int:
        """The amount of servers online on the network right now. (LIVE)"""
        return int(API.update(self, "server_count"))

    @property
    def cached(self) -> bool:
        """Has this data been cached by the API or not."""
        if self._cached == "true": return True
        else: return False

    @property
    def localtime(self) -> datetime:
        """The local time at Zeeraa's house... uMm, returns as python datetime object. (LIVE)"""
        return datetime.strptime(API.update(self, "localtime")["date"], '%Y-%m-%d %H:%M:%S.%f')

    @property
    def timezone(self) -> str:
        """The name of the timezone the API server is in."""
        return str(API.update(self, "localtime")["timezone"])
    
    datetime = localtime
    time = localtime

class Server(object):
    """Class for extended server stats."""
    def __init__(self, ENDPOINT:str, cached:bool):
        super().__init__(ENDPOINT, cached)