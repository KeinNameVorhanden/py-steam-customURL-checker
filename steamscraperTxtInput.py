import urllib.request
from bs4 import BeautifulSoup
import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
base_url = 'https://steamcommunity.com/id/'
url_path = path + '/steam_list.txt'
i = ''

with open(url_path, 'r+') as fp:
    for line in fp:
        i = line
        soup = BeautifulSoup(urllib.request.urlopen(base_url + i), features="html.parser")
        if soup.title.string == "Steam Community :: Error":
            print('useable: ' + i)
            i = i
            f = open(path + '/freeones.txt', 'a+')
            f.write(i)
            f.close()
        else:
            print('taken: ' + i)

sys.exit(0)
