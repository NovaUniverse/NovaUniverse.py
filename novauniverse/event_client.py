import sys
import time
from typing import List, Type, NoReturn, Dict, Callable
from devgoldyutils import LoggerAdapter

import logging
from . import nova_logger

from .api import NovaAPI
from .events import Event, EndpointEvent, Events

class EventClient():
    """A basic NU.PY client used to listen into events on the network."""
    def __init__(self, debug=False) -> None:
        self.__endpoint_events: Dict[str, List[EndpointEvent]] = {
            "NO_ENDPOINT" : []
        }

        if debug:
            nova_logger.setLevel(logging.DEBUG)

        self.logger = LoggerAdapter(nova_logger, prefix="EventClient")

        self.__stop = None

    # Event shit
    # ------------
    def add_event(self, event: Event) -> None:
        """Registers event on the client and starts running it."""
        active_event = event()

        if isinstance(active_event, EndpointEvent):
            try:
                self.__endpoint_events[active_event.data_api.endpoint].append(active_event)
            except KeyError:
                self.logger.debug(
                    f"The event api endpoint '{active_event.data_api.endpoint}' doesn't exist so I'm creating one in the client events dict."
                )
                self.__endpoint_events[active_event.data_api.endpoint] = []
                self.__endpoint_events[active_event.data_api.endpoint].append(active_event)
            except AttributeError:
                self.logger.debug(f"Event '{active_event.name}' data api is null so I'm adding it to NO_ENDPOINT list.")
                self.__endpoint_events["NO_ENDPOINT"].append(active_event)
            
            self.logger.debug(f"Added '{active_event.name}' to client event list.")

        # TODO: Don't forget to handle other type events here when they are added.

        return None

    def get_event_instance(self, event: Event) -> Event:
        """Gets the active instance of this event from the registered events pool in ``EventClient``."""
        for endpoint in self.__endpoint_events:
            for active_event in self.__endpoint_events[endpoint]:
                if isinstance(active_event, event):
                    return active_event

    # Decorator shit
    # ---------------
    def on_event(self, event: Events) -> None:
        """Decorator that allows you to run a function when an event occurs on NovaUniverse network."""
        if isinstance(event, EndpointEvent):
            if not event.value in [event.__class__ for endpoint in self.__endpoint_events for event in self.__endpoint_events[endpoint]]:
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
        nova_logger.info("Starting event loop and listening to events..."); self.__stop = False
        
        # Deee Loop, more like DEEZ NUTS!
        try:
            while True:
                nova_logger.debug("❤")
                
                for endpoint in self.__endpoint_events:
                    data = None
                    if not endpoint == "NO_ENDPOINT":
                        data = NovaAPI(endpoint).get()

                    for event in self.__endpoint_events[endpoint]:
                        if event.loop(data) is True: event.trigger_event()

                nova_logger.debug("\x1b[31;20m" + "❤" + "\x1b[0m" + "\n")

                if self.__stop: raise sys.exit(0)
                time.sleep(3)
        except KeyboardInterrupt:
            nova_logger.info("Event Loop Stopped!")

    def stop(self):
        """Stops the client from running. 😏If you can even get to this method."""
        self.__stop = True