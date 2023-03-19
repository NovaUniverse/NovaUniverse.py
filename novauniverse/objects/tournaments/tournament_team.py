from dataclasses import dataclass, field

from .tournament_player import TournamentPlayer
from ..nova_dataclass import NovaDataclass

from typing import Tuple, List

@dataclass(repr=False)
class TournamentTeam(NovaDataclass):
    """Represents a team from a tournament."""
    data:dict = field(repr=False)
    players_data:List[TournamentPlayer] = field(repr=False)

    team_number:int = field(init=False)
    team_score:int = field(init=False)

    # Added fields.
    # ---------------
    players:Tuple[TournamentPlayer] = field(init=False)

    def __post_init__(self):
        super().__post_init__()

        self.team_number = self.get("team_number")
        self.team_score = self.get("team_score")

        # Added attributes
        # ------------------
        self.players = tuple([player for player in self.players_data if player.team_number == self.team_number])