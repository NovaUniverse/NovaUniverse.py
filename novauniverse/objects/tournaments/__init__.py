from dataclasses import dataclass, field
from datetime import datetime

from typing import List

from .tournament_team import TournamentTeam
from .tournament_player import TournamentPlayer

from devgoldyutils.console import ConsoleColours

class NovaBasicTournament():
    """Represents a base class for every tournament on nova universe."""
    def __init__(self, data:dict) -> None:
        self.__data = data

    @property
    def id(self) -> int:
        """Returns ID of tournament."""
        return self.__data["id"]

    @property
    def date(self) -> datetime:
        """Returns date the tournament took place."""
        return datetime.strptime(
            self.__data["date"], 
            "%Y-%m-%d"
        )

    @property
    def display_name(self) -> str:
        """Returns the display name of the tournament."""
        return self.__data["display_name"]

    @property
    def winner_team_id(self) -> int:
        """Returns winner team id."""
        return self.__data["winner_team_id"]
    
    @property
    def players(self) -> List[TournamentPlayer]:
        """Returns all the players in that tournament."""
        return [TournamentPlayer(player_data) for player_data in self.__data["players"]]
    
    @property
    def teams(self) -> List[TournamentTeam]:
        """Returns all the teams in that tournament."""
        return [TournamentTeam(team_data, self.players) for team_data in self.__data["teams"]]

    # Added properties.
    # -------------------
    
    @property
    def winner_team(self) -> TournamentTeam:
        return [team for team in self.teams if team.team_number == self.winner_team_id][0]