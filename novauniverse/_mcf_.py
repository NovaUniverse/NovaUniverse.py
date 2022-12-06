from typing import List
from . import API, objects

def mcf() -> List[objects._mcf_.MCF]:
    """Returns list of MCF tournament results."""

    url = API.endpoints.URLs().mcf_result()
    plain_data = API.request_list(url)
    
    mcf_session_list = []
    for mcf_session in plain_data:
        mcf_session_list.append(objects._mcf_.MCF(mcf_session))

    return mcf_session_list
