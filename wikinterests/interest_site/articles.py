import requests
from bs4 import BeautifulSoup

def getArticle(title):
    baseurl = 'https://en.wikipedia.org/api/rest_v1/page/summary/' + title
    resp = requests.get(baseurl)
    data = resp.json()
    return data['extract']

def getSummary(response):
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    information = {}
    information['title'] = soup.find_all("h1", class_="firstHeading")[0].text
    paras = soup.find("div", class_= 'mw-parser-output')
    if "empty" not in str(paras.p):
        if len(paras.p.text) > 2:
            information['summary'] = paras.p.text
    information['url'] = response.url
    return information
    # mw-body-content mw-content-ltr mw-parser-output
    
def getArticles(n):
    articles = []
    i = 0 
    while i < n:
        url = 'https://en.wikipedia.org/wiki/Special:Random'
        resp = requests.get(url)
        info = getSummary(resp)
        if info.get('summary') is None:
            continue
        i += 1
        articles.append(info)
    return articles
    