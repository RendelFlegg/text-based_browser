import argparse
import os
import requests
from bs4 import BeautifulSoup
from collections import deque


def save_cash(url, content):
    url = url.strip('https://')[:url.rfind('.')]
    with open(f'{directory}/{url}', 'w', encoding='utf-8') as f:
        f.write(content)


def save_cash_soup(url, content):
    url = url.strip('https://')[:url.rfind('.')]
    with open(f'{directory}/{url}', 'w', encoding='utf-8') as f:
        for line in content:
            if line.text == '':
                continue
            f.write(line.text + '\n')


def load_cash(page_address):
    with open(f'{directory}/{page_address}', 'r', encoding='utf-8') as f:
        print(f.read())


def url_check(page_address):
    if not page_address.startswith('https://'):
        page_address = 'https://' + page_address
    return page_address


parser = argparse.ArgumentParser(description='Text browser')
parser.add_argument('dir', nargs='?', type=str, default=False, help='Enter directory')
args = parser.parse_args()
directory = args.dir

if not os.access(directory, os.F_OK):
    os.mkdir(directory)

history = deque()

address = input()
while address.lower() != 'exit':
    if address.lower() == 'back':
        if history:
            history.pop()
            load_cash(history.pop())
    else:
        try:
            r = requests.get(url_check(address))
            soup = BeautifulSoup(r.content, 'html.parser')
            tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
            for tag in tags:
                if tag.text == '':
                    continue
                print(tag.text)
            save_cash_soup(address, tags)
            history.append(address[:address.rfind('.')])
        except requests.exceptions.ConnectionError:
            print('Incorrect URL')
    address = input()
