import os
import requests


def save_photos(urls, prefix):
    for url_number, url in enumerate(urls):
        response = requests.get(url, verify=False)
        response.raise_for_status()
        extension = os.path.splitext(url)[-1]
        with open(f"images/{prefix}{url_number}{extension}", 'wb') as file:
            file.write(response.content)
