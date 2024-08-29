import datetime
import requests
from dotenv import load_dotenv
import os
from basic_script import save_img


def get_date(date):
    date = date.split(' ')[0]
    date = datetime.datetime.fromisoformat(date)
    date_epic = date.strftime('%Y/%m/%d')
    return date_epic


def fetch_nasa_epic_images(api_key):
    url_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key
    }
    response = requests.get(url_nasa_epic, params=params)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        date_epic = get_date(image['date'])
        image_name = image['image']
        nasa_epic_image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_epic}/png/{image_name}.png'
        save_img(url=nasa_epic_image_url,
                 img_path=f'images/nasa_epic{number}.png'
                 params = params)


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')


    fetch_nasa_epic_images(api_key)


if __name__ == '__main__':
    main()
