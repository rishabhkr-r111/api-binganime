import requests
from bs4 import BeautifulSoup


def getRequest(url):
    try :
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        return soup
    except :
        print ('connection error occured :' + url)

def links(slug):
    links = [ ]
    soup = getRequest('https://gogo-stream.com/videos/' + slug)

    if soup.find('body').text == '404\n' :
        print('404 :' + url)
        return {'links' : links}

    #find iframe
    iframe_url = soup.find('iframe')['src']
    iframe_url = 'https:' + iframe_url

    #goto iframe link
    soup = getRequest(iframe_url)
    #find tag having linkserver
    linksHtml = soup.findAll('li', attrs={'class' : 'linkserver', 'data-status' : '1'})

    for link in linksHtml :
        links.append({link.text : link['data-video']})
    
    return { 'links' : links }


