import requests
import cloudscraper
from bs4 import BeautifulSoup

def watch(slug):
    #r = requests.get(f'https://gogoplay1.com/videos/{slug}')

    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})

    html = scraper.get(f'https://gogoplay1.com/videos/{slug}').content

    soup = BeautifulSoup(html, 'html5lib')

    items = soup.find('ul', attrs={'class' : 'listing items lists'})
    #print(r.content)

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
        'eps' : eps,
        'current_ep' : slug.split('-').pop(),
        'slug' : createSlug(slug),
        'links' : links(soup.find('iframe')['src'])
    }

    return data

def links(iframe_url):
    iframe_url = 'https:' + iframe_url

    #goto iframe link
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform':'windows','mobile': False})

    html = scraper.get(iframe_url).content

    soup = BeautifulSoup(html, 'html5lib')

    #find tag having linkserver
    linksHtml = soup.findAll('li', attrs={'class' : 'linkserver', 'data-status' : '1'})
    
    links = [ ]

    for link in linksHtml :
        links.append({link.text : link['data-video']})
    
    return links
    
def createSlug(slug):
    epslug = slug.split('-')
    epslug.pop()
    epslug.pop()
    return '-'.join(epslug)
