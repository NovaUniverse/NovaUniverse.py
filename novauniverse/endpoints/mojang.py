class URLs:
    def __init__(self):
        self.base_url = "https://api.mojang.com"

        # Player
        self.player_profile_url = "/users/profiles/minecraft/{}"

    def player_profile(self, player_name):
        return self.base_url + self.player_profile_url.format(player_name)