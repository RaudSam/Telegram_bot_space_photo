import requests
import argparse
from basic_script import save_img


def fetch_spacex_last_launch(launch_id):
    url_sx = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_sx)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links):
        save_img(url=link, 
                 img_path=f'images/spacex{number}.jpg')
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', default='5eb87d47ffd86e000604b38a', type=str, help='launch id')
    args = parser.parse_args()


    fetch_spacex_last_launch(args.launch_id)
    

if __name__ == '__main__':
    main()
    