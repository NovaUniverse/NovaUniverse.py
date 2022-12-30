from ...objects.tournaments import NovaBasicTournament
from .. import InterfaceObject

from dataclasses import dataclass, field

@dataclass(repr=False)
class MCFTournament(NovaBasicTournament, InterfaceObject):
    """An individual nova games tournament."""

    def __post_init_subclass__(self, data:dict):
        InterfaceObject.__init__(self, (data["id"], data["display_name"]), dataclass=self)
