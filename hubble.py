import requests


def get_hubble_urls(image_ids):
    url = "http://hubblesite.org/api/v3"
    image_urls = []
    for pic_id in image_ids:
        response = requests.get(f"{url}/image/{pic_id}")
        response.raise_for_status()
        image_urls.append(f'http:{(response.json()["image_files"][-1]["file_url"])}')
    return image_urls


def get_hubble_ids():
    hubble_url = "http://hubblesite.org/api/v3"
    response = requests.get(f"{hubble_url}/images/holiday_cards")
    response.raise_for_status()
    picture_ids = [pic["id"] for pic in response.json()]
    return picture_ids
