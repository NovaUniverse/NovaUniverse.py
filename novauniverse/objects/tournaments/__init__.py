from dataclasses import dataclass, field
from datetime import datetime

from typing import List

from .tournament_team import TournamentTeam
from .tournament_player import TournamentPlayer

@dataclass
class NovaBasicTournament:
    """Represents a base class for every tournament on nova universe."""
    __data:dict = field(repr=False)

    id:int = field(init=False)
    """Returns ID of game."""
    date:datetime = field(init=False)
    """Returns date the game took place."""
    display_name:str = field(init=False)
    """Returns the display name of the tournament."""
    winner_team_id:int = field(init=False)
    """Returns winner team id."""
    teams:List[TournamentTeam] = field(init=False)
    """Returns all the teams in that tournament."""
    players:List[TournamentPlayer] = field(init=False)
    """Returns all the players in that tournament."""

    def __post_init__(self):
        self.id = self.__data["id"]
        self.date = datetime.strptime(
            self.__data["date"], 
            "%Y-%m-%d"
        )
        self.display_name = self.__data["display_name"]
        self.winner_team_id = self.__data["winner_team_id"]
        self.teams = [TournamentTeam(team_data) for team_data in self.__data["teams"]]
        self.players = [TournamentPlayer(player_data) for player_data in self.__data["players"]]

        try:
            self.__init_subclass__(self.__data)
        except TypeError:
            pass