from __init__ import cProfile, get_results

import sys
sys.path.insert(0, '...')

# Run profile.
#================
with cProfile.Profile() as profile:
    ...

get_results(profile)