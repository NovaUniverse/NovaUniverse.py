from __future__ import annotations

from abc import abstractmethod
from typing import List, Dict

from .. import SearchInterface

from novauniverse import objects
from novauniverse.utils.search import SearchBy, Search
from novauniverse.objects.order_by import OrderByNotSupported

class TournamentInterface(SearchInterface):
    """
    Tournaments at novauniverse are very similar so I made a whole separate interface class for it inheriting from the search interface. 
    Use this for all tournaments, components in this class can be overridden and added to if needed.
    """
    def __init__(
        self, 
        supports = [SearchBy.ID, SearchBy.NAME],
        keys = {
            SearchBy.ID: "id",
            SearchBy.NAME: "display_name"
        }
    ) -> None:
        super().__init__(supports, keys)

    def search(self, query: Search | int | str) -> objects.NovaBasicTournament | None:
        """Search for a tournament! Returns None if not found."""
        return super().search(query, self.get_all())

    @abstractmethod
    def get_all(self) -> List[objects.NovaBasicTournament]:
        """Returns all tournaments from the api in a list. Returns empty list if none."""
        ...

    @abstractmethod
    def get_latest(self) -> objects.NovaBasicTournament | None:
        """Returns the latest tournaments from the api. Returns None if there are no tournaments."""
        ...

    def get_top_players(self, order_by: objects.OrderBy = 0, max_players: int = 15) -> List[objects.TournamentPlayer]:
        """
        Returns the top ranked players in this tournament based on your parameters.
        
        This method returns a list of :py:meth:`~novauniverse.objects.tournaments.tournament_player.TournamentPlayer` but with all scores and kills from previous tournaments combined.
        """
        players: Dict[str, objects.TournamentPlayer] = {}

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