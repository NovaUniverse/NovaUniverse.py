import sys

config_dict = {
    "performance_mode" : False
}

class Config():
    """NovaUniverse.py config."""

    @property
    def performance_mode(self) -> bool:
        """
        When enabled some unnecessary features are disabled in favour for performance.

        WARNING: This will make the api wrapper less stable and friendly. So watch out it may bite 😳🐻.
        """
        return config_dict["performance_mode"]

    @performance_mode.setter
    def performance_mode(self, x:bool):
        config_dict["performance_mode"] = x


    @property
    def py_script_mode(self) -> bool:
        """
        Returns True if novauniverse.py is running in the browser with PyScript (Pyodide) or any other Emscripten based build.

        When enabled nupy will use Pyodide's http methods instead of the requests library since the requests library is not supported in Pyodide.
        """
        if sys.platform == 'emscripten':
            # This means we are running in Pyodide or any other Emscripten based build of Python.
            return True
        else:
            return False