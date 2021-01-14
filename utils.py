import os
import requests


def save_photos(urls, prefix, all_folder):
    for url_number, url in enumerate(urls):
        response = requests.get(url, verify=False)
        response.raise_for_status()
        extension = os.path.splitext(url)[-1]
        with open(f"{all_folder}/{prefix}{url_number}{extension}", 'wb') as file:
            file.write(response.content)
