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

        return [MCFTournament(tournament_data) for tournament_data in self.__mcf_result_api.get()]

    def get_latest(self) -> MCFTournament|None:
        """Returns the latest 🔥mcf tournament result from api. Returns None if not found."""
        data = self.__mcf_result_api.get()
        data.reverse()

        return (lambda uwu: None if uwu is [] else MCFTournament(uwu[0]))(data)