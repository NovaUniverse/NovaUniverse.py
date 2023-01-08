from typing import List, Dict
import sys; sys.path.insert(0, '..')
from prettyprinter import cpprint

from novauniverse import MCF, NovaGames, News

# Get top 5 mcf players.
# ------------------------
print("Top MCF Players!\n-------------------------------------")
all_mcfs = MCF().get_all()
all_mcf_players:Dict[str, dict] = {}

for mcf in all_mcfs:
    for player in mcf.players:
        if player.uuid in all_mcf_players:
            all_mcf_players[player.uuid]["score"] += player.score
        else:
            all_mcf_players[player.uuid] = {}
            all_mcf_players[player.uuid]["name"] = player.name
            all_mcf_players[player.uuid]["score"] = player.score

cpprint(sorted(all_mcf_players.items(), key=(lambda x: x[1]["score"]), reverse=True)[:5])
print("")


# Get top 5 nova games players.
# -------------------------------
print("Top Nova Games Players!\n-------------------------------------")
all_nova_games = NovaGames().get_all()
all_ng_players:Dict[str, dict] = {}

for nova_game in all_nova_games:
    for player in nova_game.players:
        if player.uuid in all_ng_players:
            all_ng_players[player.uuid]["score"] += player.score
        else:
            all_ng_players[player.uuid] = {}
            all_ng_players[player.uuid]["name"] = player.name
            all_ng_players[player.uuid]["score"] = player.score

cpprint(sorted(all_ng_players.items(), key=(lambda x: x[1]["score"]), reverse=True)[:5])
print("")

# Get newsletters.
# -----------------
all_newsletters = News().get_all()
for newsletter in all_newsletters:
    newsletter.