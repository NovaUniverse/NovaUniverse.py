import datetime
from typing import List

class basic_session(object): #Session object
    """A basic session object class."""
    def __init__(self, ENDPOINT:str, game:dict, session_id:int, metadata:str, total_places:int, timestamp:str):
        self.ENDPOINT = ENDPOINT
        
        self.game_dict_ = game
        self.session_id_ = session_id
        self.metadata_ = metadata
        self.total_places_ = total_places
        self.timestamp_ = timestamp

    from . import _game_

    @property
    def game(self) -> _game_.game: #Returns game object.
        """Returns game object countaining info about the game."""
        return self._game_.game(self.game_dict_)

    @property
    def id(self) -> str:
        """Returns id of session."""
        return self.session_id_

    @property
    def metadata(self) -> str:
        """The metadata of the session's game."""
        return self.metadata_

    @property
    def total_places(self) -> int:
        """The total amount of placement slots in the session's game."""
        return self.total_places_

    @property
    def datetime(self) -> datetime.datetime: #Returns date of sesstion in python datetime object.
        """Returns python datetime object of the date and time the session's game was created."""
        return datetime.datetime.strptime(self.timestamp_, '%Y-%m-%d %H:%M:%S.%f')

    # Aliases
    timestamp = datetime

class session(basic_session): #Class for full sessions data.
    """A full session object class. This includes a list of the players in the session."""
    def __init__(self, ENDPOINT:str, game_dict: dict, session_id: int, metadata: str, total_places: int, timestamp: dict, players:list):
        super().__init__(ENDPOINT, game_dict, session_id, metadata, total_places, timestamp)

        self.players_list = players

    from . import _player_

    @property
    def players(self) -> List[_player_.basic_player]: #Returns list of players as player objects.
        """Returns list of players who were in the session's game as basic player objects."""
        players_list = []
        for player_ in self.players_list:
            players_list.append(self._player_.basic_player(player_["player"]["player_id"], player_["player"]["uuid"], player_["player"]["username"]))

        return players_list

