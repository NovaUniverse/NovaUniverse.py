import datetime
from typing import List

from .. import API

class basic_player(object):
    def __init__(self, ENDPOINT:str, id:int, uuid:str, username:str):
        self.ENDPOINT = ENDPOINT

        self.id_ = id
        self.uuid_ = uuid
        self.username_ = username

    @property
    def id(self) -> str: #Returns Nova Universe id of player.
        """The Nova Universe id of the player."""
        return self.id_

    @property
    def uuid(self) -> str: #Returns Mojang uuid of player.
        """The Mojang uuid of the player."""
        return self.uuid_

    @property
    def username(self) -> str:
        """The “in game name”(ign) of the player."""
        return self.username_

    # Aliases
    name = username

class player(basic_player): #Player Object
    def __init__(self, ENDPOINT:str, id:int, uuid:str, username:str, first_join:dict, last_join:dict, is_online:int, sessions:list):
        super().__init__(ENDPOINT, id, uuid, username)
        self.ENDPOINT = ENDPOINT

        self.first_join_ = first_join
        self.last_join_ = last_join
        self.is_online_ = is_online
        self.sessions_ = sessions

    from . import _session_

    class player_session(_session_.basic_session): #Class for player's game sessions.
        def __init__(self, ENDPOINT:str, game: dict, session_id: int, metadata: str, total_places: int, player_placement:int, timestamp: dict):
            super().__init__(ENDPOINT, game, session_id, metadata, total_places, timestamp)

            self.player_placement_ = player_placement

        @property
        def player_placement(self) -> int:
            return self.player_placement_

    @property
    def first_join(self) -> datetime.datetime:
        """Returns datetime object of date and time the player first joined the Nova Universe network."""
        return datetime.datetime.strptime(self.first_join_, '%Y-%m-%d %H:%M:%S.%f')

    @property
    def last_join(self) -> datetime.datetime:
        """Returns datetime object of date and time the player last joined the Nova Universe network."""
        return datetime.datetime.strptime(self.last_join_, '%Y-%m-%d %H:%M:%S.%f')

    @property
    def is_online(self) -> bool: #Returns True/False if the player is currently present on the network.
        """Returns True/False if the player is currently present on the network."""
        if int(API.update(self, "is_online")) == 1: return True
        else: return False

    @property
    def sessions(self) -> List[player_session]: #Returns list of game sessions as session objects.
        """Returns list of sessions the player was in as player session objects"""
        sessions_list = []
        for session_ in self.sessions_:
            sessions_list.append(self.player_session(None, session_["game"], session_["session_id"], session_["metadata"], session_["total_places"], 
            session_["player_placement"], session_["timestamp"]))

        return sessions_list