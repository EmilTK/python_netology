import json
import collections
import xml.etree.ElementTree as xml
from pprint import pprint


def parse_json(file_path, len_word=6):
    with open(file_path, encoding='utf-8') as file:
        json_data = json.load(file)

    description = []
    items = json_data['rss']['channel']['items']
    # description = list(filter(lambda x: len(x) > len_word, ' '.join([news['description'] for news in items]).split(' ')))
    for news in items:
        for word in news['description'].split(' '):
            if len(word) > len_word:
                description.append(word)
    return description


def parse_xml(file_path, len_word=6):
    parser = xml.XMLParser(encoding='utf-8')
    tree = xml.parse(file_path, parser)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    description = []
    for news in xml_items:
        for word in news.find('description').text.split(' '):
            if len(word) > len_word:
                description.append(word)
    return description


def main(descriptions, top_words=10):
    counter_words = collections.Counter(descriptions)
    return counter_words.most_common(top_words)


if __name__ == '__main__':
    pprint(main(parse_json('files/newsafr.json')))
    print()
    pprint(main(parse_xml('files/newsafr.xml')))
