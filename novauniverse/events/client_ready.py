from . import Event, EventInfo

class ClientReady(Event):
    """Triggers when NovaClient is ready."""
    def __init__(self):
        super().__init__(self, EventInfo("client_ready"))

        self.__ready = False

    def loop(self) -> bool:
        if self.__ready is False:
            self.__ready = True
            return True
        else:
            return False
        
    def trigger_event(self):
        for function in self.functions_to_trigger:
            function()