import requests as requests
from config import token
import json

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, access_token, version='5.131', owner_id=None):
        self.access_token = token
        self.version = version
        self.params = {
            'access_token': access_token,
            'v': version
        }
        self.friends = []
        if owner_id is None:
            resp = requests.get(self.url+'users.get', self.params).json()
        else:
            self.params['user_ids'] = owner_id
            resp = requests.get(self.url+'users.get', self.params).json()

        self.owner_id = resp['response'][0]['id']
        self.first_name = resp['response'][0]['first_name']
        self.last_name = resp['response'][0]['last_name']

    def get_friends(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        get_friends_url = self.url + 'friends.get'
        friends_params = {'user_id': user_id}
        resp = requests.get(get_friends_url, params={**self.params, **friends_params}).json()
        if 'error' in resp.keys():
            return 'Пользователь с указанным ID не существует'
        else:
            self.friends.extend(resp['response']['items'])

    def __and__(self, other):
        if not isinstance(other, VkUser):
            return 'Объект не являются экземпляром класс VkUser'
        mutual = [VkUser(token, '5.131', friend) for friend in self.friends if friend in other.friends]
        return mutual

    def __str__(self):
        return f'https://vk.com/id{self.owner_id}'


if __name__ == '__main__':
    pass