from flask import Flask,jsonify
from src.search import search
from src.links import links
from src.recents import recent_sub,recent_dub
from src.details import details
from src.watch import watch

app = Flask(__name__)

@app.route('/subbed')
def Subbed():
    return jsonify(recent_sub())

@app.route('/subbed/<string:page>')
def getRecentSub(page):
    return jsonify(recent_sub(page))

@app.route('/dubbed')
def Dubbed():
    return jsonify(recent_dub())

@app.route('/dubbed/<string:page>')
def getRecentDub(page):
    return jsonify(recent_dub(page))

@app.route('/links/<string:url>')
def getLinks(url):
    return jsonify(links(url))

@app.route('/details/<string:slug>')
def getDetails(slug):
    return jsonify(details(slug))

@app.route('/watch/<string:slug>')
def Watch(slug):
    return jsonify(watch(slug))

@app.route('/search/<string:keyword>')
def getSearch(keyword):
    return jsonify(search(keyword))

if __name__ == '__main__':
   app.run(threaded=True)
