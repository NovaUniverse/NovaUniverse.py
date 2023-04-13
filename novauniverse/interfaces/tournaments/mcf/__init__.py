from __future__ import annotations

from ... import Search, NovaAPI, Endpoints
from .. import TournamentInterface
from .mcf_tournament import MCFTournament

from typing import List, overload

class MCF(TournamentInterface):
    """
    The interface for NovaAPI's ``/tournaments/mcf`` endpoint.
    Allows you to get latest, get all and search for 🔥mcf tournaments.
    """
    def __init__(self):
        super().__init__()

        self.mcf_result_api = NovaAPI(Endpoints.MCF_RESULT)

    @overload
    def search(self, query: Search | int | str) -> MCFTournament | None:
        """Search for an mcf tournament!"""
        ...

    def get_all(self) -> List[MCFTournament]:
        """Returns all 🔥mcf tournament results from api in a list. Returns empty list if none."""
        return [MCFTournament(tournament_data) for tournament_data in self.mcf_result_api.get()]

    def get_latest(self) -> MCFTournament | None:
        """Returns the latest 🔥mcf tournament result from api. Returns None if there are no tournaments."""
        data = self.mcf_result_api.get()
        data.reverse()

        return (lambda uwu: None if uwu is [] else MCFTournament(uwu[0]))(data)