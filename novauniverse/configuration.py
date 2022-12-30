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
    def performance_mode(self, a:bool):
        config_dict["performance_mode"] = a
