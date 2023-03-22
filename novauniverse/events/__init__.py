from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import Callable
from devgoldyutils import LoggerAdapter

from ..api import NovaAPI
from .. import nova_logger

class Event():
    def __init__(self, event_name:str) -> None:
        """A base class all NovaUniverse.py events inherited from."""
        self.name = event_name

        self.functions_to_trigger:list = []

        self.logger = LoggerAdapter(nova_logger, prefix=self.name)
    
    def add_function(self, func:Callable):
        """Used by ``EventClient`` to add functions to events."""
        self.functions_to_trigger.append(func)
        self.logger.debug(
            f"Added '{func.__name__}' function to '{self.name}' func trigger list."
        )

class EndpointEvent(ABC, Event):
    """Allows you to easily create events from NovaUniverse.py endpoints."""
    def __init__(self, event_name, endpoint:str):
        self.data_api = (lambda: NovaAPI(endpoint) if endpoint is not None else None)()
        """The event's data api."""

        super().__init__(event_name)

    @abstractmethod
    def loop(self, data:dict|None) -> bool:
        """
        This method is called each ``EventClient`` 💖heartbeat if the event is in use.

        -------------------
        
        Returning ``True`` indicates to the ``EventClient`` that the data has changed and it can trigger the event.

        Returning ``False`` indicates to the ``EventClient`` that the data has not changed and it shouldn't trigger the event.
        """
        ...

    @abstractmethod
    def trigger_event(self):
        """This method is ran when ``NovaClient`` gets an indication that the data has changed from ``Event.loop``."""
        ...


# Import all events under this module.
# --------------------------------------------
from .client_ready import ClientReady
from .player_join import PlayerJoin
from .player_leave import PlayerLeave

class Events(Enum):
    """
    An enum class of all available events.
    
    ---------------
    ### ***``Example:``***

    These can be used like this:

    ```python
    client = NovaClient()

    @client.on_event(Events.CLIENT_READY)
    def client_is_ready():
        print("Client is ready!")

    @client.on_event(Events.PLAYER_JOIN)
    def on_player_join(player:NovaOnlinePlayer):
        print(f"{player.username} joined {player.server_name}!")

    @client.on_event(Events.PLAYER_LEAVE)
    def on_player_join(player:NovaOnlinePlayer):
        print(f"{player.username} left {player.server_name}!")

    client.start()
    ```
    """

    CLIENT_READY = ClientReady
    """Triggers when NovaClient is ready."""

    PLAYER_JOIN = PlayerJoin
    """Triggers each time a player joins any lobby on the Nova Universe network. Passes ``NovaOnlinePlayer`` object to function."""

    PLAYER_LEAVE = PlayerLeave
    """Triggers each time a player leaves any lobby on the Nova Universe network. Passes ``NovaOnlinePlayer`` object to function."""