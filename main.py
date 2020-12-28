import os
import requests
import urllib3
from PIL import Image
from instabot import Bot
from environs import Env

urllib3.disable_warnings()


def upload_photo_inst():
    bot = Bot()
    bot.login(username=username, password=password)
    directory = "img to inst"
    pics = os.listdir(directory)
    for pic in pics:
        try:
            bot.upload_photo(f"{directory}/{pic}")
        finally:
            try:
                os.remove(f"{directory}/{pic}")
            except FileNotFoundError:
                os.remove(f"{directory}/{pic}.REMOVE_ME")


def convert_photos():
    directory = "images"
    pics = os.listdir(directory)
    for pic_number, pic in enumerate(pics):
        image = Image.open(f"{directory}/{pic}")
        rgb_image = image.convert("RGB")
        rgb_image.thumbnail((1080, 1080))
        rgb_image.save(f"img to inst/{pic_number}.jpg", format="JPEG")


def save_photos_spacex(url_pic_spacex):
    filename = "picture_spacex"
    for url_number, url in enumerate(url_pic_spacex):
        response = requests.get(f"{url}", verify=False)
        extansion = os.path.splitext(url)[-1]
        with open(f"images/{filename}{url_number}{extansion}", 'wb') as file:
            file.write(response.content)

def get_url_pic_spacex():
    url = "https://api.spacexdata.com/v4/"
    response = requests.get(f"{url}launches/latest")
    return response.json()["links"]["flickr"]["original"]



def save_photos_hubble(url_pic_hubble):
    filename = "picture_hubble"
    for url_number, url in enumerate(url_pic_hubble):
        response = requests.get(f"http:{url}", verify=False)
        extansion = os.path.splitext(url)[-1]
        with open(f"images/{filename}{url_number}{extansion}", 'wb') as file:
            file.write(response.content)


def get_url_pic_hubble(images_id):
    url_hubble = "http://hubblesite.org/api/v3"
    images_url = []
    for pic_id in images_id:
        response = requests.get(f"{url_hubble}/image/{pic_id}")
        images_url.append(response.json()["image_files"][-1]["file_url"])
    return images_url


def get_images_id():
    url_hubble = "http://hubblesite.org/api/v3"
    response = requests.get(f"{url_hubble}/images/holiday_cards")
    response.raise_for_status()
    pictures_id = []
    for pic in response.json():
        image_id = pic["id"]
        pictures_id.append(image_id)
    return pictures_id


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("img to inst", exist_ok=True)

    env = Env()
    env.read_env()

    username = env.str("USERNAME")
    password = env.str("PASSWORD")

    save_photos_hubble(get_url_pic_hubble(get_images_id()))
    save_photos_spacex(get_url_pic_spacex())
    convert_photos()
    upload_photo_inst()

