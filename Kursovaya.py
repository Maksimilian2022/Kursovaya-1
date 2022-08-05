import json
import requests

access_token = 'vk1.a.FOPeogRotD8mxzUyIs1li1ENNH19zPZRy1nWnJHcR8Bj6nHOQSyraeCCtgNEJbZc4a1ZZVaAQVq7TYIM37R-VIKGMJ59PBLMbodtOhflLfv_r7iPM8R0DZukNT6fe6fCqu_oBnUXz0v_v25EgT9z_ofRhJfBq1Oeub81djXC0cs6dINYLX3OJ5OSUDCXQTCv'


def get_photo(user_id):
    photos_dict = {}
    url = 'https://api.vk.com/method/photos.get'
    params = {'owner_id': user_id, 'album_id': 'wall', 'v': '5.81', 'access_token': access_token, 'extended': '1',
              'count': '4', 'photo_sizes': '1'}
    response = requests.get(url, params=params)
    for photo_max_size in response.json()['response']['items']:
        photos_dict[photo_max_size['sizes'][-1]['url']] = [
            {"file_name": photo_max_size['likes']['count'], "size": photo_max_size['sizes'][-1]['type']}]

    with open('Photos', 'w') as open_file:
        json.dump(photos_dict, open_file)
    a = photos_dict.values()
    return a


def post_ydisk(id):
    token = 'AQAAAABR6sW2AADLW-hiYhDRWkXIgVyXB5LPvQQ'
    y_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    for photo_post in get_photo(1):
        print(photo_post)
        params = {'path': 'Vk', 'url': photo_post}
        put_resource = requests.post(url=y_url, params=params, headers=headers)
    return







