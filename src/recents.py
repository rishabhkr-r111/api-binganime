import requests
from bs4 import BeautifulSoup

def recent_sub(page = 1):
    url = f'https://ajax.gogocdn.net/ajax/page-recent-release.html?page={page}&type=1'
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    items = soup.find('ul', attrs={'class' : 'items'})

    recents = [ ]
    for item in items.findAll('li'):
        recents.append({
            'title' : item.a['title'],
            'image_url' : item.img['src'],
            'slug' : item.a['href'][1:],
            'episode' : item.find('p' ,attrs = {'class':'episode'}).text,
            'type' : item.div.a.div['class'][1][3:]
        })

    return { 'data' : recents }

def recent_dub(page = 1):
    url = f'https://ajax.gogocdn.net/ajax/page-recent-release.html?page={page}&type=2'
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    items = soup.find('ul', attrs={'class' : 'items'})

    recents = [ ]
    for item in items.findAll('li'):
        recents.append({
            'title' : item.a['title'],
            'image_url' : item.img['src'],
            'slug' : item.a['href'][1:],
            'episode' : item.find('p' ,attrs = {'class':'episode'}).text,
            'type' : item.div.a.div['class'][1][3:]
        })

    return { 'data' : recents }

