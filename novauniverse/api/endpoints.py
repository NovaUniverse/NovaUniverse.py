BASE_DOMAIN = "https://novauniverse.net"
BASE_URL = BASE_DOMAIN + "/api"

class Endpoints:
    """Class containing all Nova Universe API endpoints."""


    # Connectivity Check
    # --------------------
    
    connectivity_check = (
        BASE_URL + "/connectivity_check"
    )


    # News
    # -------------
    NEWS_ALL = (
        BASE_URL + "/news/all"
    )
        
    NEWS_LATEST = (
        BASE_URL + "/news/latest"
    )


    # Stats
    # ------------
    STATS_EXTENDED = (
        BASE_URL + "/stats/extended"
    )

    STATS_DISCORD = (
        BASE_URL + "/stats/discord"
    )


    # Players
    # ---------
    PLAYERS_ONLINE = (
        BASE_URL + "/players/online"
    )


    # MCF
    # ------
    MCF_RESULT = (
        BASE_URL + "/mcf/result"
    )


    # Nova Games
    # -----------
    NOVA_GAMES_RESULT = (
        BASE_URL + "/nova_games/result"
    )

    NOVA_GAMES_LIVE_STATS = (
        BASE_URL + "/nova_games/live_stats"
    )

    NOVA_GAMES_DYNAMIC_CONFIGURATION = (
        BASE_URL + "/nova_games/dynamic_configuration"
    )
