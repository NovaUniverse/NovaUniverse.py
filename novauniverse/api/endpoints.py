BASE_DOMAIN = "novauniverse.net"
BASE_API_URL = "https://api." + BASE_DOMAIN

# CDN
# --------
CDN_BASE_URL = "https://" + BASE_DOMAIN + "/cdn"

# APIS
# --------
LEGACY_API_URL = "https://" + BASE_DOMAIN + "/api"

V1_API_URL = BASE_API_URL + "/v1"


class Endpoints:
    """Class containing all Nova Universe API endpoints."""

    # Connectivity Check
    # --------------------
    connectivity_check = (
        V1_API_URL + "/connectivity_check"
    )


    # News
    # -------------
    # TODO: This endpoint is from the legacy api so it may be removed soon.
    NEWS_ALL = (
        LEGACY_API_URL + "/news/all"
    )
        
    NEWS_LATEST = (
        LEGACY_API_URL + "/news/latest"
    )


    # Stats
    # ------------
    STATS_EXTENDED = (
        V1_API_URL + "/novauniverse_mc/stats/extended"
    )

    STATS_DISCORD = (
        V1_API_URL + "/discord"
    )


    # Players
    # ---------
    PLAYERS_ONLINE = (
        V1_API_URL + "/novauniverse_mc/players/online"
    )


    # MCF
    # ------
    MCF_RESULT = (
        V1_API_URL + "/tournaments/mcf/result"
    )


    # Nova Games
    # -----------
    NOVA_GAMES_RESULT = (
        V1_API_URL + "/tournaments/nova_games/result"
    )
    
    # TODO: This only exists in the legacy api so it might be removed soon.
    NOVA_GAMES_LIVE_STATS = (
        LEGACY_API_URL + "/nova_games/live_stats"
    )
    
    # TODO: Another legacy api thing that might be removed in the future. 😥
    NOVA_GAMES_DYNAMIC_CONFIGURATION = (
        LEGACY_API_URL + "/nova_games/dynamic_configuration"
    )

class CDNEndpoints:
    """Class containing all Nova Universe CDN endpoints."""

    NOVA_GAMES_ICONS_TEAM = (
        CDN_BASE_URL + "/novagames/icons/team"
    )
