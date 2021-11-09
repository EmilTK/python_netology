import requests
from config import superhero


def main(heroes):
    token = superhero
    url = 'https://superheroapi.com/api/'
    top_intelligence = 0
    top_hero = ''
    for hero in heroes:
        resp = requests.get(url+token+'search/'+hero)
        resp.raise_for_status()
        data = resp.json()
        intelligence = int(data['results'][0]['powerstats']['intelligence'])
        if intelligence > top_intelligence:
            top_intelligence = intelligence
            top_hero = hero
    return top_hero, top_intelligence


print(main(['Hulk', 'Captain America', 'Thanos']))