import requests
from dotenv import load_dotenv
import os
import argparse
from basic_script import save_img, file_extension


def fetch_nasa_apod_images(count, api_key):
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key, 
        'count': count
    }
    response = requests.get(url_nasa, params=params)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        extension = file_extension(image["url"])
        save_img(url=image['url'],
                 img_path=f'images/nasa_apod{number}{extension}')
        
    
def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')

    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default=3, type=int, help='Введите количество фотографий, которые хотите скачать')
    args = parser.parse_args()


    os.makedirs('images', exist_ok=True)
    

    fetch_nasa_apod_images(args.count, api_key)


if __name__ == '__main__':
    main()