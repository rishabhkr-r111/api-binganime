import json
import re

def slugfy(title):
    slug = re.sub('[^A-Za-z\d\s]+','',title)
    slug = '-'.join(slug.split(' '))
    return slug

f = open('tt.txt','r')
txt = f.read()
f.close()

load_data = json.loads(txt)
data = [ ]
for item in load_data['animes']:
    data.append({
        'title' : item['name'],
        'slug' : slugfy(item['name']),
        'description' : item['description'],
        'eps' : item['eps'],
        'filter_id' : item['filter_id'],
        'genre_id' : item['genre_id']
    })


f = open('animes_data.json','w')
json.dump({'data' : data},f)
f.close()
