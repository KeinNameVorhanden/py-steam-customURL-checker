import urllib.request
from bs4 import BeautifulSoup
import os
import time

path = os.path.dirname(os.path.abspath(__file__))
base_url = 'https://steamcommunity.com/id/'
# url_path = path + '/list.txt'
id = ''


# Writes to output
def write_file(id):
    f = open(path + '/freeones.txt', 'a+')
    f.write(id)
    f.close()


def split_nickname(input, nickname):
    words = input.split(",")
    for i in words:
        soup = BeautifulSoup(urllib.request.urlopen(base_url + i), features="html.parser")
        if soup.title.string == "Steam Community :: Error":
            print('useable: ' + i)
            i = i + "\n"
            write_file(i)
        else:
            print('taken: ' + i)
    return nickname


nickname = ""
input = input("Username you want to check: ")
split_nickname(input, nickname)
