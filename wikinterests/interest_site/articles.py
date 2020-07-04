import wikipedia as wiki
from random import randint
def getArticles(n):
    articles = {}
    count = 0
    while True:
        num = randint(0, 100000)
        try:
            url = wiki.page(num)
            articles[url.url] = f'''
                <h3>{url.title}</h3>
                <p>{url.summary}</p>
                <a href='{url.url}'>See more...</a>
            '''
            count += 1
        except:
            pass
        if count == n:
            break
    return articles
