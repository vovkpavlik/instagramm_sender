import requests


def get_spacex_urls():
    url = "https://api.spacexdata.com/v4"
    response = requests.get(f"{url}/launches/latest")
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]
