import requests
from ... import Discord

def test_discord_stats():
    data_from_wrapper = Discord().get_stats().data
    data_from_raw_request = requests.get(url="https://api.novauniverse.net/v1/discord/").json()

    assert data_from_raw_request == data_from_wrapper