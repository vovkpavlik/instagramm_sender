import os
import requests


def save_hubble_photos(hubble_pics_url):
    filename = "picture_hubble"
    for url_number, url in enumerate(hubble_pics_url):
        response = requests.get(f"http:{url}", verify=False)
        extension = os.path.splitext(url)[-1]
        with open(f"images/{filename}{url_number}{extension}", 'wb') as file:
            file.write(response.content)


def get_hubble_urls(image_ids):
    hubble_url = "http://hubblesite.org/api/v3"
    image_urls = []
    for pic_id in image_ids:
        response = requests.get(f"{hubble_url}/image/{pic_id}")
        image_urls.append(response.json()["image_files"][-1]["file_url"])
    return image_urls


def get_image_ids():
    hubble_url = "http://hubblesite.org/api/v3"
    response = requests.get(f"{hubble_url}/images/holiday_cards")
    response.raise_for_status()
    picture_ids = []
    for pic in response.json():
        image_id = pic["id"]
        picture_ids.append(image_id)
    return picture_ids
