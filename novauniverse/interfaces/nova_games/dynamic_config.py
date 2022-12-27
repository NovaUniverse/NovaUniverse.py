from typing import List
from dataclasses import dataclass, field
from ...interfaces import InterfaceObject

@dataclass
class TeamColour:
    team_number:str
    colour_name:str

@dataclass
class TeamName:
    team_number:str
    display_name:str

class NovaGamesDynamicConfig(InterfaceObject):
    def __init__(self, data:dict):
        self.__data = data

        super().__init__((None, None), self, 
            properties_to_represent = [
                ("team_colours", self.team_colours),
                ("team_names", self.team_names)
            ]
        )

    @property
    def team_colours(self) -> List[TeamColour]:
        """Returns the team colours."""
        return [TeamColour(team_num, self.__data["team_colors"][team_num]) for team_num in self.__data["team_colors"]]

    team_colors = team_colours

    @property
    def team_names(self) -> List[TeamName]:
        """Returns the team display names."""
        return [TeamName(team_num, self.__data["team_names"][team_num]) for team_num in self.__data["team_names"]]
