class URLs:
    def __init__(self):
        self.base_url = "https://novauniverse.net/api"

        # Player
        self.player_stats_url = "/stats/player/{}"
        
        # Sessions
        self.session_stats_url = "/stats/session/by_id/{}"
        

    def player_stats(self, player_uuid):
        return self.base_url + self.player_stats_url.format(player_uuid)

    def session_stats(self, session_id):
        return self.base_url + self.session_stats_url.format(session_id)