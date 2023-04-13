from __future__ import annotations

from ... import Search, NovaAPI, Endpoints
from .. import TournamentInterface
from .nova_games_tournament import NovaGamesTournament

from typing import List, overload

class NovaGames(TournamentInterface):
    """
    The interface for NovaAPI's ``/tournaments/nova_games`` endpoint.
    Allows you to get latest, get all and search for 🟥nova games tournaments.
    """
    def __init__(self):
        super().__init__()

        self.nova_games_result_api = NovaAPI(Endpoints.NOVA_GAMES_RESULT)

    @overload
    def search(self, query: Search | int | str) -> NovaGamesTournament | None:
        """Search for an mcf tournament!"""
        ...

    def get_all(self) -> List[NovaGamesTournament]:
        """Returns all 🔥mcf tournament results from api in a list. Returns empty list if none."""
        return [NovaGamesTournament(tournament_data) for tournament_data in self.nova_games_result_api.get()]

    def get_latest(self) -> NovaGamesTournament | None:
        """Returns the latest 🔥mcf tournament result from api. Returns None if there are no tournaments."""
        data = self.nova_games_result_api.get()
        data.reverse()

        return (lambda uwu: None if uwu is [] else NovaGamesTournament(uwu[0]))(data)