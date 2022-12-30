from __init__ import cProfile, get_results

import sys
sys.path.insert(0, '../..')

# Run profile.
#================
with cProfile.Profile() as profile:
    from novauniverse import NovaGames
    
    nova_games = NovaGames().get_latest()

    print(nova_games)


get_results(profile)