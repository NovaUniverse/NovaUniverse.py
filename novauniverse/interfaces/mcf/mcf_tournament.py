from ...objects.tournaments import NovaBasicTournament
from .. import InterfaceObject

class MCFTournament(NovaBasicTournament, InterfaceObject):
    """An individual mcf game/tournament."""
    def __init__(self, data:dict):
        self.__data = data

        NovaBasicTournament.__init__(self, self.__data)

        InterfaceObject.__init__(self,
            (self.id, self.display_name), object_class=self,
                properties_to_represent = [
                    ("id", self.id),
                    ("display_name", self.display_name),
                    ("winner_team_id", self.winner_team_id)
                ]
            )
