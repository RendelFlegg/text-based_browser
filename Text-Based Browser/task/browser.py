import argparse
import os
import requests
from bs4 import BeautifulSoup
from collections import deque
from colorama import Fore, Style


def save_cache(url, content):
    url = url.strip('https://')[:url.rfind('.')]
    with open(f'{directory}/{url}', 'w', encoding='utf-8') as f:
        for line in content:
            if line.text == '':
                continue
            if line.name == 'a':
                f.write(Fore.BLUE + line.text + '\n')
            else:
                f.write(Style.RESET_ALL + line.text + '\n')


def load_cache(url):
    with open(f'{directory}/{url}', 'r', encoding='utf-8') as f:
        print(f.read())


def url_check(url):
    if not url.startswith('https://'):
        url = 'https://' + url
    return url


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
            load_cache(history.pop())
    else:
        try:
            r = requests.get(url_check(address))
            soup = BeautifulSoup(r.content, 'html.parser')
            tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
            for tag in tags:
                if tag.text == '':
                    continue
                if tag.name == 'a':
                    print(Fore.BLUE + tag.text)
                else:
                    print(Style.RESET_ALL + tag.text)
            save_cache(address, tags)
            history.append(address[:address.rfind('.')])
        except requests.exceptions.ConnectionError:
            print('Incorrect URL')
    address = input()
