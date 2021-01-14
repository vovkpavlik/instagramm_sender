import os
import urllib3
from PIL import Image
from instabot import Bot
from environs import Env

from utils import save_photos
from spacex import get_spacex_urls
from hubble import get_hubble_ids, get_hubble_urls


def upload_photos(inst_folder, username, password):
    bot = Bot()
    bot.login(username=username, password=password)
    pics = os.listdir(inst_folder)
    for pic in pics:
        bot.upload_photo(f"{inst_folder}/{pic}")
        os.remove(f"{inst_folder}/{pic}.REMOVE_ME")


def convert_photos(all_folder, inst_folder):
    pics = os.listdir(all_folder)
    for pic_number, pic in enumerate(pics):
        image = Image.open(f"{all_folder}/{pic}")
        rgb_image = image.convert("RGB")
        rgb_image.thumbnail((1080, 1080))
        rgb_image.save(f"{inst_folder}/{pic_number}.jpg", format="JPEG")


if __name__ == "__main__":
    all_folder = "images"
    inst_folder = "img to inst"

    os.makedirs(all_folder, exist_ok=True)
    os.makedirs(inst_folder, exist_ok=True)

    urllib3.disable_warnings()

    env = Env()
    env.read_env()

    inst_username = env.str("INST_USERNAME")
    inst_password = env.str("INST_PASSWORD")

    hubble_ids = get_hubble_ids()
    hubble_urls = get_hubble_urls(hubble_ids)

    save_photos(hubble_urls, "hubble", all_folder)
    save_photos(get_spacex_urls(), "spacex", all_folder)

    convert_photos(all_folder, inst_folder)
    upload_photos(inst_folder, inst_username, inst_password)
