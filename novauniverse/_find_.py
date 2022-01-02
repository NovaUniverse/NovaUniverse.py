from .endpoints import nova, mojang
from .APIs import nova as nova_api, mojang as mojang_api

from .objects import player as player_, session as session_

def Player(player_name:str=None, player_uuid:str=None): #Find a player and return data as player object.
    if player_uuid == None:
        if not player_name == None:
            player_uuid = player_name_to_uuid(player_name)
        else:
            raise Exception("Neither player name or player uuid was passed through the 'player object'. Please pass one of them in.")

    url = nova.URLs().player_stats(player_uuid)
    plain_data = nova_api.request(url)

    return player_(plain_data["id"], plain_data["uuid"], plain_data["username"], plain_data["first_join_timestamp"]["date"], plain_data["last_join_timestamp"]["date"], plain_data["is_online"], plain_data["sessions"])

def Session(session_id:str): #Find a game session and return data as a full session object.
    url = nova.URLs().session_stats(session_id)
    plain_data = nova_api.request(url)

    return session_(plain_data["game"], plain_data["session_id"], plain_data["metadata"], plain_data["total_places"], plain_data["timestamp"]["date"], plain_data["players"])



def player_name_to_uuid(player_name:str):
    short_uuid:str = (mojang_api.request(mojang.URLs().player_profile(player_name)))["id"]; return short_to_full_uuid(short_uuid)

def short_to_full_uuid(short_uuid:str): #Converts short uuid to full uuid.
    return short_uuid[:8] + "-" + short_uuid[8:12] +  "-" + short_uuid[12:16] +  "-" + short_uuid[16:20] +  "-" + short_uuid[20:]