from typing import List
from dataclasses import dataclass, field
from ...objects import NovaDataclass
from ...api import NovaCDN, CDNEndpoints

@dataclass(repr=False)
class TeamColour(NovaDataclass):
    team_number:str
    colour_name:str

@dataclass(repr=False)
class TeamName(NovaDataclass):
    team_number:str
    display_name:str

@dataclass(repr=False)
class TeamBadge(NovaDataclass):
    team_number:str
    code_name:str
    image_url:str = field(init=False)

    def __post_init__(self):
        self.image_url = CDNEndpoints.NOVA_GAMES_ICONS_TEAM + f"/{self.code_name[19:][:-3]}.png"

@dataclass(repr=False)
class NovaGamesDynamicConfig(NovaDataclass):
    __data:dict = field(repr=False)
    
    team_colours:List[TeamColour] = field(init=False)
    """Returns the team colours."""
    team_names:List[TeamName] = field(init=False)
    """Returns the team display names."""
    team_badges:List[TeamBadge] = field(init=False)

    # Aliases
    # ---------
    team_colors:List[TeamColour] = field(init=False)
    """Aliases for ``team_colours`` because you know some people don't spell colour the same way, smh 🙄."""

    def __post_init__(self):
        self.team_colours = [TeamColour(team_num, self.__data["team_colors"][team_num]) for team_num in self.__data["team_colors"]]
        self.team_names = [TeamName(team_num, self.__data["team_names"][team_num]) for team_num in self.__data["team_names"]]
        self.team_badges = [TeamBadge(team_num, self.__data["team_badges"][team_num]) for team_num in self.__data["team_badges"]]

        self.team_colors = self.team_colours
