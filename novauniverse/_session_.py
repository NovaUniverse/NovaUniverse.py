import datetime

from .endpoints import nova
from .APIs import nova as nova_api
from . import objects

class basic_session(object): #Session object
    def __init__(self, game:dict, session_id:int, metadata:str, total_places:int, timestamp:dict):
        self.game_dict_ = game
        self.session_id_ = session_id
        self.metadata_ = metadata
        self.total_places_ = total_places
        self.timestamp_ = timestamp

    @property
    def game(self): #Returns game object.
        return objects.game(self.game_dict_)

    @property
    def id(self):
        id:int = self.session_id_; return id

    @property
    def metadata(self):
        metadata:str = self.metadata_; return metadata

    @property
    def total_places(self):
        total_places:int = self.total_places_; return total_places

    @property
    def datetime(self): #Returns date of sesstion in python datetime object.
        datetime_object:datetime.datetime = datetime.datetime.strptime(self.timestamp_, '%Y-%m-%d %H:%M:%S.%f')
        return datetime_object

    @property
    def timestamp(self): #Alias of "session().datetime".
        return self.datetime

class session(basic_session): #Class for full sessions data.
    def __init__(self, game_dict: dict, session_id: int, metadata: str, total_places: int, timestamp: dict, players:list):
        super().__init__(game_dict, session_id, metadata, total_places, timestamp)

        self.players_list = players

    @property
    def players(self): #Returns list of players as player objects.
        from . import _player_
        players_list = []
        for player_ in self.players_list:
            players_list.append(_player_.basic_player(player_["player"]["player_id"], player_["player"]["uuid"], player_["player"]["username"]))

        return players_list