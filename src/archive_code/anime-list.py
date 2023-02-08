import json
import requests
from bs4 import BeautifulSoup

def anime_list():
    url = 'https://www2.kickassanime.rs/anime-list'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    data = soup.findAll('script')
    print(data[5])


anime_list()
