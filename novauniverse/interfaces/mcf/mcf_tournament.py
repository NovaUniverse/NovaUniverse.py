from ...objects.tournaments import NovaBasicTournament
from .. import InterfaceObject

class MCFTournament(InterfaceObject, NovaBasicTournament):
    """An individual mcf game/tournament."""
    def __init__(self, data:dict):
        self.__data = data

        super(NovaBasicTournament, self).__init__()

        super().__init__(
            (self.__data["id"], self.__data["display_name"]), object_class=self,
                properties_to_represent = [
                    ("id", self.__data["id"]),
                    ("display_name", self.display_name),
                    ("winner_team_id", self.winner_team_id)
                ],
                __data = self.__data
            )
