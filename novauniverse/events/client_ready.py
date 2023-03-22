from . import EndpointEvent

class ClientReady(EndpointEvent):
    """Triggers when NovaClient is ready."""
    def __init__(self):
        super().__init__("client_ready", endpoint=None)

        self.__ready = False

    def loop(self, data) -> bool:
        if self.__ready is False:
            return True

        return False
        
    def trigger_event(self):
        for function in self.functions_to_trigger:
            self.__ready = True
            function()