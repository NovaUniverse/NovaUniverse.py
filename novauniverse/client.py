import time
import sys
from typing import List, Type

from . import nova_logger

from .events import Event, Events

class NovaClient():
    """The client used for events."""
    def __init__(self) -> None:
        self.__events:List[Event] = []

        self.__stop = False

    # Event shit
    # ================
    def add_event(self, event:Event):
        """Registers event on client and starts running. Returns false if already added."""
        self.__events.append(event())

    def get_event_instance(self, event:Type[Event]) -> Event:
        """Gets the active instance of this event from the registered events pool in ``NovaClient``."""
        for active_event in self.__events:
            print(active_event)
            if isinstance(active_event, event):
                return active_event

    # Decorator shit
    # ================
    def on_event(self, event:Event):
        """Decorator that allows you to run a function when an event occur in NovaUniverse."""
        if not event in self.__events:
            self.add_event(event)

        def inner(func):
            # Add function to event trigger list.
            self.get_event_instance(event).add_function(func)

        return inner

    # Client stuff UwU.
    # ======================
    def start(self):
        """Runs client and starts listening to events."""
        nova_logger.info("Starting event loop and listening to events..."); self.__stop = False
        
        while True:
            for event in self.__events:
                if event.loop() is True: event.trigger_event()

            nova_logger.debug("\x1b[31;20m" + "❤" + "\x1b[0m")

            if self.__stop: raise sys.exit(0)
            time.sleep(1)

    def stop(self):
        """Stops the client from running. 😏If you can even get to this method."""
        self.__stop = True