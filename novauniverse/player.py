import datetime

from .endpoints import nova, mojang
from .APIs import nova as nova_api, mojang as mojang_api

class player(): #Player Object
    def __init__(self, player_name:str=None, player_uuid:str=None):

        if player_uuid == None:
            if not player_name == None:
                player_uuid = self._utls().player_name_to_uuid(player_name)
            else:
                raise Exception("Neither player name or player uuid was passed through the 'player object'. Please pass one of them in.")

        self.url = nova.URLs().player_stats(player_uuid)

        self.plain_data = nova_api.request(self.url)

    @property
    def id(self): #Returns Nova Universe id of player.
        id:str = self.plain_data["id"]; return id

    @property
    def uuid(self): #Returns Mojang uuid of player.
        uuid:str = self.plain_data["uuid"]; return uuid

    @property
    def username(self):
        username:str = self.plain_data["username"]; return username

    @property
    def first_join(self):
        datetime_object:datetime.datetime = datetime.datetime.strptime(self.plain_data["first_join_timestamp"]["date"], '%Y-%m-%d %H:%M:%S.%f')
        return datetime_object

    @property
    def last_join(self):
        datetime_object:datetime.datetime = datetime.datetime.strptime(self.plain_data["last_join_timestamp"]["date"], '%Y-%m-%d %H:%M:%S.%f')
        return datetime_object

    @property
    def is_online(self): #Returns True/False if the player is currently present on the network.
        online:int = self.plain_data["is_online"]

        if online == 1: return True
        else: return False

    class _utls:
        def __init__(self):
            pass

        def player_name_to_uuid(self, player_name:str):
            short_uuid:str = (mojang_api.request(mojang.URLs().player_profile(player_name)))["id"]; return self.short_to_full_uuid(short_uuid)

        def short_to_full_uuid(self, short_uuid:str): #Converts short uuid to full uuid.
            return short_uuid[:8] + "-" + short_uuid[8:12] +  "-" + short_uuid[12:16] +  "-" + short_uuid[16:20] +  "-" + short_uuid[20:]