from dataclasses import dataclass, field
from datetime import datetime

from typing import List

from .. import NovaDataclass
from .tournament_team import TournamentTeam
from .tournament_player import TournamentPlayer

@dataclass(repr=False)
class NovaBasicTournament(NovaDataclass):
    """Represents a base dataclass for every tournament on nova universe."""
    data:dict = field(repr=False)

    id:int = field(init=False)
    """Returns ID of tournament."""

    date:datetime = field(init=False)
    """Returns date the tournament took place."""

    display_name:str = field(init=False)
    """Returns the display name of the tournament."""

    winner_team_id:int = field(init=False)
    """Returns winner team id."""

    players:List[TournamentPlayer] = field(init=False)
    """Returns all the players in that tournament."""
    
    teams:List[TournamentTeam] = field(init=False)
    """Returns all the teams in that tournament."""

    # Added properties.
    # -------------------
    winner_team:TournamentTeam = field(init=False)
    """Returns the team that won."""

    def __post_init__(self):
        self.id = self.get("id")
        self.date = datetime.strptime(self.get("date"), "%Y-%m-%d")
        self.display_name = self.get("display_name")
        self.winner_team_id = self.get("winner_team_id")
        self.players = [TournamentPlayer(player_data) for player_data in self.get("players")]
        self.teams = [TournamentTeam(team_data, self.players) for team_data in self.get("teams")]
        self.winner_team = [team for team in self.teams if team.team_number == self.winner_team_id][0]

        super().__init__()