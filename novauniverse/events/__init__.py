from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

from .. import nova_logger

@dataclass
class EventInfo:
    """Details about a event."""
    code_name:str


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


    @abstractmethod
    def loop(self) -> bool:
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

class Events(Enum):
    """An enum class of all available events. These can be used in ``NovaClient().on_event()`` function decorator."""

    CLIENT_READY = ClientReady
    """Triggers when NovaClient is ready."""

    PLAYER_JOIN = PlayerJoin
    """Triggers each time a player joins any lobby on the Nova Universe network. Passes ``NovaOnlinePlayer`` object to function."""