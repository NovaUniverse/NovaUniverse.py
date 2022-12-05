from __future__ import annotations

from .. import SearchInterface, SearchBy, Search, InterfaceObject
from .mcf_tournament import MCFTournament

from typing import List

class MCF(SearchInterface):
    """
    The interface for NovaAPI's ``/mcf`` endpoint.
    Allows you to get latest, get all and search for 🔥mcf tournaments.
    """
    def __init__(self):
        super().__init__(self, supports=[SearchBy.id, SearchBy.name_])

        self.__mcf_result_api = self.api(self.endpoints.MCF_RESULT)

    def find(self, search: Search) -> MCFTournament | None:
        return super().find(search, self.get_all())

    def get_all(self) -> List[MCFTournament]:
        """Returns all 🔥mcf tournament results from api in a list. Returns empty list if none."""
        tournaments:List[MCFTournament] = []

        data:list = self.__mcf_result_api.get()

        for tournament_data in data:
            tournaments.append(MCFTournament(tournament_data))

        return tournaments

    def get_latest(self) -> MCFTournament|None:
        """Returns the latest 🔥mcf tournament result from api. Returns None if not found."""
        data:list = self.__mcf_result_api.get()

        if data == []:
            return None

        data.reverse() # I hope this works. #Not-tested
        return data[0]
        