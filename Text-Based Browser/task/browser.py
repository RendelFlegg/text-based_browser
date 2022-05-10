import argparse
import os

parser = argparse.ArgumentParser(description='Text browser')
parser.add_argument('dir', nargs='?', type=str, default=False, help='Enter directory')
args = parser.parse_args()
directory = args.dir

if not os.access(directory, os.F_OK):
    os.mkdir(directory)

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

url_dictionary = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
address = input()
while address.lower() != 'exit':
    if '.' not in address and address in os.listdir(directory):
        with open(f'{directory}/{address}', 'r') as f:
            print(f.read())
    elif address in url_dictionary:
        print(url_dictionary[address])
        with open(f'{directory}/{address[:-4]}', 'w', encoding='utf-8') as f:
            f.write(url_dictionary[address])
    else:
        print('Error: Incorrect URL')
    address = input()
