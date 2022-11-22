from ... import InterfaceObject

from .global_ import Global
from .player_preview import PlayerPreview
from .nova_server import NovaServer
from .system import System

from typing import List

class ServerInfo(InterfaceObject):
    def __init__(self, data:dict):
        self.__data = data

        super().__init__(
            id_and_name=(None, None), object_class=self,

            properties_to_represent= [
                ("player_count", self.player_count),
                ("server_count", self.server_count),
                ("player_preview", self.player_preview)
            ]
        )

    @property
    def global_(self) -> Global:
        """Returns class that contains global ``player_count`` and ``server_count``."""
        return Global(self.__data["global"])

    @property
    def player_count(self) -> int:
        """Returns global player count of Nova Universe."""
        return self.global_.player_count

    @property
    def server_count(self) -> int:
        """Returns global server count of Nova Universe."""
        return self.global_.server_count

    @property
    def player_preview(self) -> PlayerPreview:
        """Returns player preview."""
        return PlayerPreview(self.__data["player_preview"])

    @property
    def servers(self) -> List[NovaServer]:
        """Returns all servers on the Nova Universe network."""
        return [NovaServer(server_data) for server_data in self.__data["servers"]]

    @property
    def cached(self) -> bool:
        """Returns whether this data is cached or not."""
        return self.__data["cached"]

    @property
    def system(self) -> System:
        """Returns the system class that lets you see get details like the localtime."""
        return System(self.__data["system"])