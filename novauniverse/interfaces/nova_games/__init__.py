from __future__ import annotations

from .. import SearchInterface, SearchBy, Search, InterfaceObject
from .nova_games_tournament import NovaGamesTournament

from typing import List

class NovaGames(SearchInterface):
    """
    The interface for NovaAPI's ``/nova_games`` endpoint.
    Allows you to get the latest and all 🟥nova games tournament results and also allows you to search for them.
    """
    def __init__(self):
        super().__init__(self, supports=[SearchBy.id, SearchBy.name_])

        self.__nova_games_result_api = self.api(self.endpoints.NOVA_GAMES_RESULT)

    def find(self, search: Search) -> NovaGamesTournament | None:
        return super().find(search, self.get_all())

    def get_all(self) -> List[NovaGamesTournament]:
        """Returns all 🔥mcf tournament results from api in a list. Returns empty list if there are no results."""

        return [NovaGamesTournament(tournament_data) for tournament_data in self.__nova_games_result_api.get()]

    def get_latest(self) -> NovaGamesTournament|None:
        """Returns the latest 🟥Nova Games tournament result from api. Returns None if there are no results."""
        data = self.__nova_games_result_api.get()
        data.reverse()

        return (lambda uwu: None if uwu is [] else NovaGamesTournament(uwu[0]))(data)