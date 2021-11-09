import os
import requests
from config import ya_token
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def check(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        resp = requests.get(url, params={'path': file_path}, headers=self.token)
        resp.raise_for_status()
        items = resp.json()['_embedded']['items']
        files = [{'filename': file['name'], 'filesize': file['size'] / 1024} for file in items]
        pprint(files)

    def upload(self, file: str, upload_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        resp = requests.get(
            url,
            params={'path': f'{upload_path}/{os.path.basename(file)}', 'overwrite': 'true'},
            headers=ya_token
        )
        resp.raise_for_status()

        with open(file, 'rb') as f:
            resp = requests.put(resp.json()['href'], files={'file': f})
            resp.raise_for_status()
        return f'Загрузка файла {os.path.basename(file)} успешно завершена.'


if __name__ == '__main__':
    uploader = YaUploader(ya_token)
    result = uploader.upload('files/wall.jpg', '/netology')
    print(result)
