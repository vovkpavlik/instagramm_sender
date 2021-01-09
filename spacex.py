import os
import requests


def save_spacex_photos(url_pic_spacex):
    filename = "picture_spacex"
    for url_number, url in enumerate(url_pic_spacex):
        response = requests.get(f"{url}", verify=False)
        extension = os.path.splitext(url)[-1]
        with open(f"images/{filename}{url_number}{extension}", 'wb') as file:
            file.write(response.content)


def get_spacex_urls():
    url = "https://api.spacexdata.com/v4/"
    response = requests.get(f"{url}launches/latest")
    return response.json()["links"]["flickr"]["original"]
