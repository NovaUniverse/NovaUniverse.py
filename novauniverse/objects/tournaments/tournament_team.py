from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class TournamentTeam:
    """Represents a team from a tournament."""
    __data:dict = field(repr=False)

    team_number:int = field(init=False)
    team_score:int = field(init=False)

    def __post_init__(self):
        self.id = self.__data["id"]
        self.date = datetime.strptime(
            self.__data["date"], 
            "%Y-%m-%d"
        )
        self.team_number = self.__data["team_number"]
        self.team_score = self.__data["team_score"]

        try:
            self.__init_subclass__(self.__data)
        except TypeError:
            pass