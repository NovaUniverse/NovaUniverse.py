from datetime import datetime

class License(object):
    def __init__(self, owner:str, expires_at:str, is_demo:str, is_active:str):
        self._owner = owner
        self._expires_at = expires_at
        self._is_demo = is_demo
        self._is_active = is_active

    @property
    def owner(self) -> str:
        """Returns the owner of the license key."""
        return self._owner

    @property
    def expires_at(self) -> datetime:
        """Returns the date the key expires as python datetime object."""
        return datetime.strptime(self._expires_at, '%Y-%m-%d %H:%M:%S')

    @property
    def is_demo(self) -> bool:
        if self._is_demo == "true": return True
        else: return False

    @property
    def is_active(self) -> bool:
        if self._is_active == "true": return True
        else: return False