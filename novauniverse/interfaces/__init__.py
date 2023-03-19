from ..api import NovaAPI, Endpoints

class Interface():
    """The base interface where all NovaUniverse.py endpoint interfaces inherit from."""
    def __init__(self) -> None:
        ...

class BasicInterface(Interface):
    """A basic interface, nothing more... nothing less..."""
    # TODO: Change this docstring lmao

    def __init__(self) -> None:
        super().__init__()