import requests
import json
from bs4 import BeautifulSoup

def search(keyword):
    url = f'https://ajax.gogocdn.net/site/loadAjaxSearch?keyword={keyword}&id=-1'

    r = requests.get(url)
    load_json = json.loads(r.content)
    soup = BeautifulSoup(load_json['content'], 'html5lib')

    search_results = [ ]

    for item in soup.findAll('a'):
        search_results.append({
            'title' : item.text,
            'image_url' : item.div['style'].split('"')[1],
            'slug' : item['href'][9:]
        })

    return { 'data' : search_results }

