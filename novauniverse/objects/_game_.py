class game(object):
    def __init__(self, game_dict:dict):
        self.name = game_dict["display_name"]
        self.code_name = game_dict["name"]
        
        self.display_name = self.name