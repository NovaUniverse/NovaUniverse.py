from . import API, objects

def license(key:str):
    """Returns information about a license key."""

    url = API.endpoints.URLs().license_tournament_system(key)
    plain_data = API.request(url)

    return objects._license_.License(plain_data["owner"], plain_data["expires_at"], plain_data["is_demo"], plain_data["is_active"])