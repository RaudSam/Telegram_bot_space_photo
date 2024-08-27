import argparse
import os
import telegram
import asyncio
from dotenv import load_dotenv


async def publish_an_image(image_name, token, chat_id):
    bot = telegram.Bot(token = token)
    file = os.path.join("./images", image_name)
    await bot.send_photo(chat_id = chat_id, photo=open(file, 'rb'))


def main():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument('--image_name', type=str, help="Введите название фото")
    parser_args = parser.parse_args()


    asyncio.run(publish_an_image(parser_args.image_name, token, chat_id))