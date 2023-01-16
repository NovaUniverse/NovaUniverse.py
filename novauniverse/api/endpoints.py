BASE_DOMAIN = "https://novauniverse.net"

API_BASE_URL = BASE_DOMAIN + "/api"
CDN_BASE_URL = BASE_DOMAIN + "/cdn"

class Endpoints:
    """Class containing all Nova Universe API endpoints."""


    # Connectivity Check
    # --------------------
    
    connectivity_check = (
        API_BASE_URL + "/connectivity_check"
    )


    # News
    # -------------
    NEWS_ALL = (
        API_BASE_URL + "/news/all"
    )
        
    NEWS_LATEST = (
        API_BASE_URL + "/news/latest"
    )


    # Stats
    # ------------
    STATS_EXTENDED = (
        API_BASE_URL + "/stats/extended"
    )

    STATS_DISCORD = (
        API_BASE_URL + "/stats/discord"
    )


    # Players
    # ---------
    PLAYERS_ONLINE = (
        API_BASE_URL + "/players/online"
    )


    # MCF
    # ------
    MCF_RESULT = (
        API_BASE_URL + "/mcf/result"
    )


    # Nova Games
    # -----------
    NOVA_GAMES_RESULT = (
        API_BASE_URL + "/nova_games/result"
    )

    NOVA_GAMES_LIVE_STATS = (
        API_BASE_URL + "/nova_games/live_stats"
    )

    NOVA_GAMES_DYNAMIC_CONFIGURATION = (
        API_BASE_URL + "/nova_games/dynamic_configuration"
    )

class CDNEndpoints:
    """Class containing all Nova Universe CDN endpoints."""

    NOVA_GAMES_ICONS_TEAM = (
        CDN_BASE_URL + "/novagames/icons/team"
    )
