import argparse
import os
import telegram
import asyncio
import random
from dotenv import load_dotenv


async def publish_an_image(image_name, token, chat_id):
    bot = telegram.Bot(token = token)
    file = os.path.join("./images", image_name)
    with open (file, 'rb') as photo:
                await bot.send_photo(chat_id = chat_id, photo=photo)


def main():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument('--image_name', type=str, help="Введите название фото")
    parser_args = parser.parse_args()

    if not image_name:
        image_name = random.choice(
            tuple(os.walk('images'))[0][2]
        )

    asyncio.run(publish_an_image(parser_args.image_name, token, chat_id))
