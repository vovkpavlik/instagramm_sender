import os
import urllib3
from PIL import Image
from instabot import Bot
from environs import Env

from hubble import save_hubble_photos, get_hubble_urls, get_image_ids
from spacex import save_spacex_photos, get_spacex_urls


def upload_photos(inst_folder):
    bot = Bot()
    bot.login(username=inst_username, password=inst_password)
    pics = os.listdir(inst_folder)
    for pic in pics:
        bot.upload_photo(f"{inst_folder}/{pic}")
        os.remove(f"{inst_folder}/{pic}.REMOVE_ME")


def convert_photos(all_folder):
    pics = os.listdir(all_folder)
    for pic_number, pic in enumerate(pics):
        image = Image.open(f"{all_folder}/{pic}")
        rgb_image = image.convert("RGB")
        rgb_image.thumbnail((1080, 1080))
        rgb_image.save(f"img to inst/{pic_number}.jpg", format="JPEG")


if __name__ == "__main__":
    all_folder = "images"
    inst_folder = "images to inst"

    os.makedirs(all_folder, exist_ok=True)
    os.makedirs(inst_folder, exist_ok=True)

    urllib3.disable_warnings()

    env = Env()
    env.read_env()

    inst_username = env.str("INST_USERNAME")
    inst_password = env.str("INST_PASSWORD")

    image_ids = get_image_ids()
    image_urls = get_hubble_urls(image_ids)

    save_hubble_photos(image_urls)
    save_spacex_photos(get_spacex_urls())
    convert_photos(all_folder)
    upload_photos(inst_folder)
