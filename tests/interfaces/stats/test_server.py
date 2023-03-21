import requests
from ... import Server

def test_server_stats():
    data_from_wrapper = Server().get_stats().data
    data_from_raw_request = requests.get(url="https://api.novauniverse.net/v1/novauniverse_mc/stats/extended").json()

    data_from_wrapper["cached"] = None
    data_from_raw_request["cached"] = None

    data_from_wrapper["system"]["localtime"] = None
    data_from_raw_request["system"]["localtime"] = None

    assert data_from_raw_request == data_from_wrapper