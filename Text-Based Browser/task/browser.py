import argparse
import os
import requests
from collections import deque


def save_cash(url, content):
    url = url.strip('https://')[:url.rfind('.')]
    with open(f'{directory}/{url}', 'w', encoding='utf-8') as f:
        f.write(content)


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
    elif '.' not in address:
        if address in os.listdir(directory):
            load_cash(address)
            history.append(address)
        else:
            print('Error: Incorrect URL')
    else:
        r = requests.get(url_check(address))
        print(r.text)
        save_cash(address, r.text)
        history.append(address[:address.rfind('.')])
    address = input()
