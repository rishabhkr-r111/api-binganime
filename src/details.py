import requests
from bs4 import BeautifulSoup

def details(slug):
    r = requests.get(f'https://gogo-stream.com/videos/{slug}-episode-1')

    soup = BeautifulSoup(r.content, 'html5lib')

    items = soup.find('ul', attrs={'class' : 'listing items lists'})

    eps = [ ]

    for item in items.findAll('li'):
        eps.append({
           'date' : item.find('span',attrs={'class':'date'}).text,
            'image_url' : item.find('img')['src'],
            'slug' : item.a['href'][8:]
    
        })

    data = {
        'title' : soup.find('span', attrs={'class' : 'date'}).text,
        'details' : soup.find('div', attrs={'class' : 'content-more-js'}).text,
        'eps' : eps
    }

    return data

