import time
import sys
from typing import List, Type, NoReturn, Dict, Callable

import logging
from . import nova_logger

from .api import NovaAPI
from .events import Event, Events

class NovaClient():
    """The NovaUniversePy client used for events."""
    def __init__(self, debug=False) -> None:
        self.__events:Dict[str, List[Event]] = {
            "NO_ENDPOINT" : []
        }

        if debug:
            nova_logger.setLevel(logging.DEBUG)

        self.__stop = False

    # Event shit
    # ================
    def add_event(self, event:Event):
        """Registers event on client and starts running. Returns false if already added."""
        active_event:Event = event()
        try:
            self.__events[active_event.data_api.endpoint].append(active_event)
        except KeyError:
            nova_logger.debug(f"The event api endpoint '{active_event.data_api.endpoint}' doesn't exist so I'm creating one in the client events dict.")
            self.__events[active_event.data_api.endpoint] = []
            self.__events[active_event.data_api.endpoint].append(active_event)
        except AttributeError:
            nova_logger.debug(f"Event '{active_event.code_name}' data api is null so I'm adding it to NO_ENDPOINT list.")
            self.__events["NO_ENDPOINT"].append(active_event)
        
        nova_logger.debug(f"Added '{active_event.code_name}' to client event list.")

    def get_event_instance(self, event:Type[Event]) -> Event:
        """Gets the active instance of this event from the registered events pool in ``NovaClient``."""
        for endpoint in self.__events:
            for active_event in self.__events[endpoint]:
                if isinstance(active_event, event):
                    return active_event

    # Decorator shit
    # ================
    def on_event(self, event:Events):
        """Decorator that allows you to run a function when an event occur in NovaUniverse."""
        if not event.value in [event.__class__ for endpoint in self.__events for event in self.__events[endpoint]]:
            self.add_event(event.value)

        def inner(func):
            # Add function to event trigger list.
            self.get_event_instance(event.value).add_function(func)

        return inner

    # Client stuff UwU.
    # ======================
    def start(self) -> NoReturn:
        """Runs client and starts listening to events."""
        nova_logger.info("Starting event loop and listening to events..."); self.__stop = False
        
        # Deee Loop, more like DEEZ NUTS!
        try:
            while True:
                nova_logger.debug("❤")
                
                for endpoint in self.__events:
                    data = None
                    if not endpoint == "NO_ENDPOINT":
                        data = NovaAPI(endpoint).get()

                    for event in self.__events[endpoint]:
                        if event.loop(data) is True: event.trigger_event()

                nova_logger.debug("\x1b[31;20m" + "❤" + "\x1b[0m" + "\n")

                if self.__stop: raise sys.exit(0)
                time.sleep(3)
        except KeyboardInterrupt:
            nova_logger.info("Event Loop Stopped!")

    def stop(self):
        """Stops the client from running. 😏If you can even get to this method."""
        self.__stop = True