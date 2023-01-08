from __future__ import annotations

from dataclasses import dataclass, field

from ..nova_player import NovaBasicPlayer

@dataclass(repr=False)
class TournamentPlayer(NovaBasicPlayer):
    """A base tournament player class, used in interfaces like mcf and nova games because player data is very similar between them."""

    uid:int = field(init=False)
    """Returns uid of tournament player."""
    has_nova_account:bool = field(init=False)
    """Returns True or False if player has nova account."""
    nova_account_name:str|None = field(init=False)
    """Returns nova account name of tournament player."""
    team_number:int = field(init=False)
    """Returns the team number of the player."""
    score:int = field(init=False)
    """Returns the score the player currently achieved."""
    kills:int = field(init=False)
    """Returns the current amount of kills the player achieved."""

    def __post_init_subclass__(self, data:dict) -> None:
        self.uid = self.get("uid")
        self.has_nova_account = self.get("has_nova_account")
        self.nova_account_name = self.get("nova_account_name")
        self.team_number = self.get("team_number")
        self.score = self.get("score", default=0)
        self.kills = self.get("kills", default=0)
