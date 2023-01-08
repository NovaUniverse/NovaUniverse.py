from __future__ import annotations

from .. import SearchInterface, SearchBy, Search
from .mcf_tournament import MCFTournament
from ...objects.tournaments import TournamentPlayer
from ...objects.order_by import OrderBy, OrderByNotSupported

from typing import List, Dict

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

    def get_top_players(self, order_by:OrderBy=0, max_players:int=5) -> List[TournamentPlayer]:
        """
        Returns the top ranked players based on your function prompts.
        
        This method returns ``novauniverse.objects.tournaments.tournament_player.TournamentPlayer`` but with all scores and kills combined.
        """
        players:Dict[str, TournamentPlayer] = {}

        if isinstance(order_by, OrderBy): order_by = order_by.value

        if order_by in [0, 1]:
            for player in [player for mcf in self.get_all() for player in mcf.players]:
                if player.uuid in players:
                    players[player.uuid].score += player.score
                    players[player.uuid].kills += player.kills
                else:
                    player.team_number = None; player.uid = None
                    players[player.uuid] = player

            key = (lambda: (lambda x: x[1].score) if order_by == 0 else (lambda x: x[1].kills))()

            return [item[1] for item in sorted(players.items(), key=key, reverse=True)[:max_players]]
        
        raise OrderByNotSupported(order_by)