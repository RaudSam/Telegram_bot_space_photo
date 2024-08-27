import argparse
import os
import random
import time
import telegram
import asyncio
from dotenv import load_dotenv


async def send_messages(chat_id, token, time_sleep):
    bot = telegram.Bot(token = token)
    document_dir = os.listdir("./images")
    while document_dir:
        random.shuffle(document_dir)
        for image in document_dir:
            path_to_file = f"./images/{image}"
            await bot.send_photo(chat_id = chat_id, photo=open(path_to_file, 'rb'))
            time.sleep(time_sleep)
    

def main():
    load_dotenv()
    token = os.getenv('TG_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument('--time', default=14400, help="Введите время задержки отправления фото",
                        type=int)
    parser_args = parser.parse_args()


    asyncio.run(send_messages(chat_id, token, parser_args.time))


if __name__ == "__main__":
    main()