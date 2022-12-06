from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Callable

from ..api import NovaAPI
from .. import nova_logger

@dataclass
class EventInfo:
    """Details about a event."""
    code_name:str
    data_api:NovaAPI|None


# Base Event Class
# -------------------------
class Event(ABC):
    """A base class for all NovaUniverse.py events."""
    def __init__(self, event_class:object, info:EventInfo):
        self.__event_class = event_class
        self.__info = info

        self.functions_to_trigger:list = []

    @property
    def code_name(self) -> str:
        """Returns code name of event."""
        return self.__info.code_name

    @property
    def data_api(self) -> NovaAPI|None:
        """Returns data function/callable from event info."""
        return self.__info.data_api


    @abstractmethod
    def loop(self, data:dict|None) -> bool:
        """
        This method is called each ``NovaClient`` 💖heartbeat if the event is in use.

        -------------------
        
        Returning ``True`` indicates to ``NovaClient`` that the data has changed and it can trigger the event.

        Returning ``False`` indicates to ``NovaClient`` that the data has not changed and it shouldn't trigger the event.
        """
        ...

    @abstractmethod
    def trigger_event(self):
        """This method is ran when ``NovaClient`` gets an indication that the data has changed from ``Event.loop``."""
        ...


    def add_function(self, func):
        """Used by ``NovaClient`` to add functions to events."""
        self.functions_to_trigger.append(func)
        nova_logger.debug(f"Added '{func.__name__}' function to '{self.code_name}' func trigger list.")


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