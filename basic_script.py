import requests
import os
from urllib.parse import urlsplit, unquote


def save_img(url, img_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(img_path, 'wb') as file:
        file.write(response.content)


def file_extension(url):
    parsed_url = urlsplit(url)
    path = unquote(parsed_url.path)
    file_extension = os.path.splitext(path)[1]
    return file_extension







