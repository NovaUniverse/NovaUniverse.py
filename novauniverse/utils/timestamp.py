import datetime

class Timestamp():
    """A NovaUniverse API timestamp object."""
    def __init__(self, timestamp_dict:dict) -> datetime.datetime:
        """Returns timestamp as python datetime object and more."""
        self.__date:str = timestamp_dict["date"]
        self.__timezone_type:int = timestamp_dict["timezone_type"]
        self.__timezone:str = timestamp_dict["timezone"]

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}' + 
            f'(date={self.date}, timezone_type={self.timezone_type}, timezone={self.timezone})'
        )

    @property
    def date(self) -> datetime.datetime:
        return datetime.datetime.strptime(
            self.__date, 
            "%Y-%m-%d %H:%M:%S.%f"
        )

    @property
    def timezone_type(self) -> int:
        return self.__timezone_type

    @property
    def timezone(self) -> str:
        return self.__timezone
