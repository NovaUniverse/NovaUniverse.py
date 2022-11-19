from . import API
from . import objects

def player(player_name:str=None, player_uuid:str=None) -> objects._player_.player:
    """Finds the player and returns player object."""

    if player_uuid == None:
        if not player_name == None:
            player_uuid = player_name_to_uuid(player_name)
        else:
            raise Exception("Neither player name or player uuid was passed through the 'player object'. Please pass one of them in.")

    url = API.endpoints.URLs().player_stats(player_uuid)
    plain_data = API.request(url)

    return objects._player_.player(url, plain_data["id"], plain_data["uuid"], plain_data["username"], plain_data["first_join_timestamp"]["date"], plain_data["last_join_timestamp"]["date"], plain_data["is_online"], plain_data["sessions"])

def session(session_id:str) -> objects._session_.session:
    """Finds the game session and returns full session object."""

    url = API.endpoints.URLs().session_stats(session_id)
    plain_data = API.request(url)

    return objects._session_.session(url, plain_data["game"], plain_data["session_id"], plain_data["metadata"], plain_data["total_places"], plain_data["timestamp"]["date"], plain_data["players"])


def player_name_to_uuid(player_name:str):
    return (API.request(API.endpoints.URLs().name_to_uuid(player_name)))["full_uuid"]

"""
def short_to_full_uuid(short_uuid:str): #Converts short uuid to full uuid.
    return short_uuid[:8] + "-" + short_uuid[8:12] +  "-" + short_uuid[12:16] +  "-" + short_uuid[16:20] +  "-" + short_uuid[20:]
"""