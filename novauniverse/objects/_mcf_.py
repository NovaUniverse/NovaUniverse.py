from __future__ import annotations
import datetime
from typing import List

class MCFPlayer(object):
    def __init__(self, data:dict):
        self.uid_:int = data["uid"]
        self.has_nova_account_:bool = data["has_nova_account"]
        self.nova_account_name_:str|None = data["nova_account_name"]
        self.username_:str = data["username"]
        self.uuid_:str = data["uuid"]
        self.team_number_:int = data["team_number"]
        self.score_:int = data["score"]
        self.kills_:int = data["kills"]

    @property
    def id(self):
        """Returns the MCF id of the player."""
        return self.uid_

    @property
    def has_nova_account(self):
        """Returns True/False if the player is linked to a novauniverse account."""
        return self.has_nova_account_

    @property
    def nova_account_name(self):
        """Returns the name of the nova universe account this player is linked to."""
        return self.nova_account_name_
    
    @property
    def username(self):
        """Returns the player's mojang username."""
        return self.username_

    @property
    def uuid(self):
        """Returns the player's mojang uuid."""
        return self.uuid_

    @property
    def team_number(self):
        """Returns the number of the team the player is in."""
        return self.team_number_

    @property
    def score(self):
        """Returns the total score this player achived."""
        return self.score_

    @property
    def kills(self):
        """Returns the amount of kills this player got."""
        return self.kills_

    uid = id
    """Returns the MCF id of the player."""

    name = username
    """Returns the player's mojang username."""

class BasicMCFTeam(object):
    def __init__(self, team_number:int, team_score:int):
        self.team_number_ = team_number
        self.team_score_ = team_score

    @property
    def team_number(self):
        """Returns the number of this team."""
        return self.team_number_

    @property
    def team_score(self):
        """Returns the total score of this team."""
        return self.team_score_

class ExtendedMCFTeam(BasicMCFTeam):
    def __init__(self, team_players:list, team_number:int, team_score:int):
        self.players_:list = team_players
        super().__init__(team_number, team_score)

    @property
    def players(self) -> List[MCFPlayer]:
        """Returns list of player objects of the players in that team."""
        player_list = []
        for player in self.players_:
            player_list.append(MCFPlayer(player))

        return player_list

class MCF(object):
    """This class represents a MCF tournament session/week."""

    def __init__(self, data:dict):
        self.data = data

        self.id_:int = data["id"]
        self.date_:str = data["date"]
        self.display_name_:str = data["display_name"]
        self.winner_team_id_:int = data["winner_team_id"]
        self.teams_:list = data["teams"]
        self.players_:list = data["players"]

    @property
    def id(self):
        return self.id_

    @property
    def date(self) -> datetime.datetime:
        return datetime.datetime.strptime(self.date_, '%Y-%m-%d')

    @property
    def display_name(self):
        """The display name of the MCF session."""
        return self.display_name_

    @property
    def winner_team_id(self):
        """The team number of the winning team."""
        return self.winner_team_id_

    @property
    def winner_team(self) -> ExtendedMCFTeam:
        """Returns team object of the winning team."""
        for team in self.teams:
            if team.team_number == self.winner_team_number:
                return team

    @property
    def teams(self) -> List[ExtendedMCFTeam]:
        """Returns list of all teams that played in this MCF."""
        teams_list = []
        for team in self.teams_:

            # Find the players of this team.
            team_players_list = []
            for player in self.players_:
                if player["team_number"] == team["team_number"]:
                    team_players_list.append(player)

            teams_list.append(ExtendedMCFTeam(team_players_list, team["team_number"], team["team_score"]))

        return teams_list

    winner_team_number = winner_team_id