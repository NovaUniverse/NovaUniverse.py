import cProfile
import pstats

def get_results(profile:cProfile.Profile):
    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)

    print("")
    stats.print_stats(8)