from . import API, objects

def server():
    """Returns stats about the server. (E.g. player count, server count...)"""

    url = API.endpoints.URLs().basic_server_stats()
    url_2 = API.endpoints.URLs().players_online()
    plain_data = API.request(url)
    players_list = API.request(url_2)["players"]

    return objects._server_.BasicServer(url, url_2, plain_data["cached"], players_list)
