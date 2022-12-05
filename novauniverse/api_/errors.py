from ..errors import NovaError

# BASE EXCEPTION
#------------------
class NovaAPIError(NovaError):
    """Error raised when a known error occurs on the API."""
    def __init__(self, message:str) -> None:
        super().__init__(message)


# Other exceptions.
#---------------------

class NoEndpointPassed(NovaAPIError):
    """Raised when no endpoint is passed to NovaAPI."""
    def __init__(self) -> None:
        super().__init__("No endpoint was passed to NovaAPI(), an endpoint must be passed to use it's methods.")

class FailedConnectivityCheck(NovaAPIError):
    """Raised when failed to connect to Nova Universe API."""
    def __init__(self) -> None:
        super().__init__("Failed to establish a connection with Nova Universe API. Failed connect check. The API is probably offline. Blame Anton.")

class UnSuccessfulOperation(NovaAPIError):
    """Raised when Nova Universe API returns unsuccessful operation."""
    def __init__(self) -> None:
        super().__init__("That operation was return as unsuccessful by Nova Universe.")