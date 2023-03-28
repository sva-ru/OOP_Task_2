import os
from pprint import pprint

import requests

def intelligence_superhero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    rez = response.json()
    intelligence = {}
    for it in rez:
        if it['name'] == 'Hulk' or it['name'] == 'Captain America' or it['name'] == 'Thanos':
            intelligence[it['name']] = it['powerstats']['intelligence']
    return f'Самый умный супергерой {max(intelligence.items(), key=lambda x: x[1])[0]}'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # disk_file_path = os.path.abspath(file_path)
        disk_file_path = "Netology/"
        file_name = os.path.basename(file_path)
        href = self._get_upload_link(disk_file_path=disk_file_path+file_name).get("href")
        print(href)
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

if __name__ == '__main__':
    print(intelligence_superhero())
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:\\Users\\vasya\\PycharmProjects\\Netology\\OOP\\Task 2\\testFile.txt'
    token = ""
    print(path_to_file)
    #
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)