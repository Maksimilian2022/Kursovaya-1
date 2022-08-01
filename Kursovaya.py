
from pprint import pprint
import requests


def get_photo():
    photos_dict ={}
    url = 'https://api.vk.com/method/photos.get'
    params = {'owner_id': '1', 'album_id': 'wall', 'v': '5.81', 'access_token': access_token, 'extended': '1', 'count': '4', 'photo_sizes': '1'  }
    response = requests.get(url, params=params)
    for photo_max_size in response.json()['response']['items']:

        photos_dict[photo_max_size['likes']['count']] = photo_max_size['sizes'][-1]['url']
        if photos_dict[photo_max_size['likes']['count']] == photos_dict:
            photos_dict[photo_max_size['likes']['count']] = photo_max_size['data']

    with open('Photos', 'w') as open_file:
        open_file.write(str(photos_dict))
    a = photos_dict.values()
    return a


def post_ydisk():
    token = 'AQAAAABR6sW2AADLW-hiYhDRWkXIgVyXB5LPvQQ'
    y_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {'path': 'Vk', 'url': get_photo()}
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    for photo_post in get_photo():
        params = {'path': 'Vk', 'url': photo_post}
        put_resource = requests.post(url=y_url, params=params, headers=headers)

    return
print(post_ydisk())







