from __future__ import annotations
from . import endpoints

import requests
import json

from .. import info

api_name = "NOVA API"
headers = {'User-Agent': (str(info.PACKAGE_NAME))[0:-2]}
error_format = f"\u001b[31m{api_name}" + ": [{}] {}\u001b[0m"

class NovaAPIError(Exception):
    pass

def request(url:str):
    """Makes request to api then returns data in json."""
    #Make request.
    response = requests.get(url, headers=headers)
    data:dict = response.json()
    
    try: # Nova Universe API error catcher.
        if data["success"] == False:
            error = data["error"]
            message = data["message"]

            raise NovaAPIError(error_format.format(error, message))
    except KeyError:
        pass

    try:
        return data["data"]
    except KeyError:
        return data

def request_list(url:str):
    """Makes request to api then returns data in json."""
    #Make request.
    response = requests.get(url, headers=headers)
    data:list = response.json()

    return data

def update(object, data_name):
    """Requests for specific pieces of data from the API. (Used for LIVE object attributes.)"""
    if not object.ENDPOINT == None:
        data = request(object.ENDPOINT)
        return data[f"{data_name}"]
    else:
        return None