from __future__ import annotations

from .. import SearchInterface, SearchBy, Search, NovaAPI, Endpoints
from .mcf_tournament import MCFTournament
from ... import objects
from ...objects.order_by import OrderByNotSupported

from typing import List, Dict

class MCF(SearchInterface):
    """
    The interface for NovaAPI's ``/mcf`` endpoint.
    Allows you to get latest, get all and search for 🔥mcf tournaments.
    """
    def __init__(self):
        super().__init__(
            supports = [SearchBy.ID, SearchBy.NAME],
            keys = {
                SearchBy.ID: "id",
                SearchBy.NAME: "display_name"
            }
            
        )

        self.mcf_result_api = NovaAPI(Endpoints.MCF_RESULT)

    def search(self, query: Search | int | str) -> MCFTournament | None:
        """Search for an mcf tournament!"""
        return super().search(query, self.get_all())

    def get_all(self) -> List[MCFTournament]:
        """Returns all 🔥mcf tournament results from api in a list. Returns empty list if none."""
        return [MCFTournament(tournament_data) for tournament_data in self.mcf_result_api.get()]

    def get_latest(self) -> MCFTournament | None:
        """Returns the latest 🔥mcf tournament result from api. Returns None if there are no tournaments."""
        data = self.mcf_result_api.get()
        data.reverse()

        return (lambda uwu: None if uwu is [] else MCFTournament(uwu[0]))(data)

    def get_top_players(self, order_by: objects.OrderBy = 0, max_players: int = 15) -> List[objects.TournamentPlayer]:
        """
        Returns the top ranked players based on your parameters.
        
        This method returns a list of ``novauniverse.objects.tournaments.tournament_player.TournamentPlayer`` but with all scores and kills from previous tournaments combined.
        """
        players:Dict[str, objects.TournamentPlayer] = {}

        if isinstance(order_by, objects.OrderBy): order_by = order_by.value

        if order_by in [0, 1]:
            for player in [player for mcf in self.get_all() for player in mcf.players]:
                if player.uuid in players:
                    players[player.uuid].score += player.score
                    players[player.uuid].kills += player.kills
                else:
                    player.team_number = None; player.uid = None # We null these properties as they are irrelevant and are different in every tournament.
                    players[player.uuid] = player

            key = (lambda: (lambda x: x[1].score) if order_by == 0 else (lambda x: x[1].kills))()

            return [item[1] for item in sorted(players.items(), key=key, reverse=True)[:max_players]]
        
        raise OrderByNotSupported(order_by)