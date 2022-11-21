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

    