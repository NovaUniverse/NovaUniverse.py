from dataclasses import dataclass, field
from datetime import datetime

from .tournament_player import TournamentPlayer
from ..nova_dataclass import NovaDataclass

from typing import Tuple, List

@dataclass(repr=False)
class TournamentTeam(NovaDataclass):
    """Represents a team from a tournament."""
    __data:dict = field(repr=False)
    __players:List[TournamentPlayer] = field(repr=False)

    team_number:int = field(init=False)
    team_score:int = field(init=False)

    # Added fields.
    # ---------------
    players:Tuple[TournamentPlayer] = field(init=False)

    def __post_init__(self):
        self.team_number = self.__data["team_number"]
        self.team_score = self.__data["team_score"]

        # Added attributes
        # ------------------
        self.players = tuple([player for player in self.__players if player.team_number == self.team_number])

        try:
            self.__init_subclass__(self.__data)
        except TypeError:
            pass