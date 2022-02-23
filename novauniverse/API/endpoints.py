class URLs:
    def __init__(self):
        self.base_url = "https://novauniverse.net/api"

        # Player
        self.player_stats_url = "/stats/player/{}"
        
        # Sessions
        self.session_stats_url = "/stats/session/by_id/{}"

        # Server Stats
        self.players_online_url = "/players/online/"
        self.basic_server_stats_url = "/stats/basic"
        self.extended_server_stats_url = "/stats/extended"

        # Tournament System validate license key.
        self.license_tournament_system_url = "/license/tournament_system/{}"

        # Internal Mojang API
        self.internal_mojang_api_url = "/private/mojang"
        

    def player_stats(self, player_uuid):
        return self.base_url + self.player_stats_url.format(player_uuid)

    def session_stats(self, session_id):
        return self.base_url + self.session_stats_url.format(session_id)

    def players_online(self):
        return self.base_url + self.players_online_url

    def basic_server_stats(self):
        return self.base_url + self.basic_server_stats_url

    def extended_server_stats(self):
        return self.base_url + self.extended_server_stats_url

    def license_tournament_system(self, key:str):
        return self.base_url + self.license_tournament_system_url.format(key)

    def name_to_uuid(self, ign:str):
        return self.base_url + self.internal_mojang_api_url + f"/name_to_uuid/{ign}"