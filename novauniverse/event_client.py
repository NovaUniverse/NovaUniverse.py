from __future__ import annotations

import time
from typing import List, Type, NoReturn, Dict
from devgoldyutils import LoggerAdapter

import logging
from . import nova_logger

from .api import NovaAPI
from .events import Event, EndpointEvent, Events

class EventClient():
    """A basic NU.PY client used to listen into events on the network."""
    def __init__(self, debug=False) -> None:
        self.__endpoint_events: Dict[str, List[EndpointEvent]] = {
            None: []
        }

        if debug:
            nova_logger.setLevel(logging.DEBUG)

        self.logger = LoggerAdapter(nova_logger, prefix="EventClient")

        self.__stop = None

    # Event shit
    # ------------
    def add_event(self, event: Type[Event]) -> None:
        """Registers event on the client and starts running it."""
        active_event = event()

        self.logger.debug(
            f"Adding the event '{active_event.name}'..."
        )

        if isinstance(active_event, EndpointEvent):
            try:
                self.__endpoint_events[active_event.endpoint].append(active_event)
            except KeyError:
                self.logger.debug(
                    f"The event endpoint '{active_event.endpoint}' doesn't exist so I'm creating one in the client's events dict."
                )
                self.__endpoint_events[active_event.endpoint] = []
                self.__endpoint_events[active_event.endpoint].append(active_event)
            
            self.logger.debug(f"Added '{active_event.name}' to client event list.")

        # TODO: Don't forget to handle other event types here when they are added.

        return None

    def get_event_instance(self, event: Event) -> Event | None:
        """Gets the active instance of this event from the registered events pool in ``EventClient``."""
        for endpoint in self.__endpoint_events:

            for active_event in self.__endpoint_events[endpoint]:

                if isinstance(active_event, event):
                    return active_event
        
        return None

    # Decorator shit
    # ---------------
    def on_event(self, event: Events) -> None:
        """Decorator that allows you to run a function when an event occurs on NovaUniverse network."""
        # I'm using issubclass() here instead of isinstance() because these are just references to a class and not an actual instance of a class. 
        # Hence isinstance() will not work for my case.
        if issubclass(event.value, EndpointEvent):
            if event.value not in [event.__class__ for endpoint in self.__endpoint_events for event in self.__endpoint_events[endpoint]]:
                self.add_event(event.value)

        # Handle other type of events here...

        def inner(func):
            # Add function to event trigger list.
            self.get_event_instance(event.value).add_function(func)

        return inner

    # Client stuff UwU.
    # ------------------
    def start(self) -> NoReturn:
        """Runs client and starts listening to events."""
        self.logger.info("Starting event loop and listening to events..."); self.__stop = False
        
        # Deee Loop, more like DEEZ NUTS!
        try:

            while self.__stop is not True:
                self.logger.debug("❤")
                
                for endpoint in self.__endpoint_events:
                    data = None

                    if endpoint is not None:
                        data = NovaAPI(endpoint).get()

                    for event in self.__endpoint_events[endpoint]:
                        if event.loop(data) is True: event.trigger_event()

                self.logger.debug("\x1b[31;20m" + "❤" + "\x1b[0m" + "\n")

                time.sleep(3)

        except KeyboardInterrupt:
            self.logger.info("Event Loop Stopped!")

    def stop(self):
        """Stops the client from running. 😏If you can even get to this method."""
        self.__stop = True