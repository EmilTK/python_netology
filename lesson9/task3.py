from pprint import pprint
import requests
import datetime


def stackoverflow():
    current_date = (datetime.datetime.today())
    past_data = (current_date - datetime.timedelta(days=2)).timestamp()
    url = 'https://api.stackexchange.com/2.3/questions'
    resp = requests.get(
        url,
        params={
            'fromdate': round(past_data),
            'todate': round(current_date.timestamp()),
            'order': 'desc',
            'sort': 'activity',
            'tagged': 'python',
            'site': 'stackoverflow'})
    print(resp.url)
    resp.raise_for_status()
    test = [{'title': query['title'], 'date': query['creation_date'], 'tags': query['tags']}
            for query in resp.json()['items']]
    pprint(test)


if __name__ == '__main__':
    stackoverflow()
