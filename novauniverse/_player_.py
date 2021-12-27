import datetime

from .endpoints import nova, mojang
from .APIs import nova as nova_api, mojang as mojang_api

class basic_player(object):
    def __init__(self, id:int, uuid:str, username:str):
        self.id_ = id
        self.uuid_ = uuid
        self.username_ = username

    @property
    def id(self): #Returns Nova Universe id of player.
        id:str = self.id_; return id

    @property
    def uuid(self): #Returns Mojang uuid of player.
        uuid:str = self.uuid_; return uuid

    @property
    def username(self):
        username:str = self.username_; return username

    @property
    def name(self): #Alias of "player().username"
        return self.username

class player(basic_player): #Player Object
    def __init__(self, id:int, uuid:str, username:str, first_join:dict, last_join:dict, is_online:int, sessions:list):
        super().__init__(id, uuid, username)
        self.first_join_ = first_join
        self.last_join_ = last_join
        self.is_online_ = is_online
        self.sessions_ = sessions

    from . import _session_

    class player_session(_session_.basic_session): #Class for player's game sessions.
        def __init__(self, game: dict, session_id: int, metadata: str, total_places: int, player_placement:int, timestamp: dict):
            super().__init__(game, session_id, metadata, total_places, timestamp)

            self.player_placement_ = player_placement

        @property
        def player_placement(self):
            player_placement:int = self.player_placement_; return player_placement

    @property
    def first_join(self):
        datetime_object:datetime.datetime = datetime.datetime.strptime(self.first_join_, '%Y-%m-%d %H:%M:%S.%f')
        return datetime_object

    @property
    def last_join(self):
        datetime_object:datetime.datetime = datetime.datetime.strptime(self.last_join_, '%Y-%m-%d %H:%M:%S.%f')
        return datetime_object

    @property
    def is_online(self): #Returns True/False if the player is currently present on the network.
        online:int = self.is_online_

        if online == 1: return True
        else: return False

    @property
    def sessions(self): #Returns list of game sessions as session objects.
        sessions_list = []
        for session_ in self.sessions_:
            sessions_list.append(self.player_session(session_["game"], session_["session_id"], session_["metadata"], session_["total_places"], 
            session_["player_placement"], session_["timestamp"]))

        return sessions_list

    class _utls:
        def __init__(self):
            pass

        def player_name_to_uuid(self, player_name:str):
            short_uuid:str = (mojang_api.request(mojang.URLs().player_profile(player_name)))["id"]; return self.short_to_full_uuid(short_uuid)

        def short_to_full_uuid(self, short_uuid:str): #Converts short uuid to full uuid.
            return short_uuid[:8] + "-" + short_uuid[8:12] +  "-" + short_uuid[12:16] +  "-" + short_uuid[16:20] +  "-" + short_uuid[20:]