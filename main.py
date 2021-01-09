import os
import urllib3
from PIL import Image
from instabot import Bot
from environs import Env

from hubble import save_hubble_photos, get_hubble_urls, get_image_ids
from spacex import save_spacex_photos, get_spacex_urls


def upload_photos():
    bot = Bot()
    bot.login(username=username_inst, password=password_inst)
    directory = inst_folder
    pics = os.listdir(directory)
    for pic in pics:
        bot.upload_photo(f"{directory}/{pic}")
        os.remove(f"{directory}/{pic}.REMOVE_ME")


def convert_photos():
    directory = all_folder
    pics = os.listdir(directory)
    for pic_number, pic in enumerate(pics):
        image = Image.open(f"{directory}/{pic}")
        rgb_image = image.convert("RGB")
        rgb_image.thumbnail((1080, 1080))
        rgb_image.save(f"img to inst/{pic_number}.jpg", format="JPEG")


if __name__ == "__main__":
    all_folder = "images"
    inst_folder = "images_to_inst"

    os.makedirs(all_folder, exist_ok=True)
    os.makedirs(inst_folder, exist_ok=True)

    urllib3.disable_warnings()

    env = Env()
    env.read_env()

    username_inst = env.str("USERNAME_INST")
    password_inst = env.str("PASSWORD_INST")

    image_ids = get_image_ids()
    image_urls = get_hubble_urls(image_ids)

    save_hubble_photos(image_urls)
    save_spacex_photos(get_spacex_urls())
    convert_photos()
    upload_photos()
