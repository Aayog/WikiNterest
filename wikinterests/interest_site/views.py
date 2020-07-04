from django.shortcuts import render
from .articles import getArticles

def home(request):
    articles = [getHtml(a) for a in getArticles(10)]
    context = {
        'title' : 'HOME',
        'articles' : articles
    }
    return render(request, 'interest_site/home.html', context)


def about(request):
    context = {
        'title' : 'ABOUT',
        'content' : 'Wikinterest is a site that has articles based on users interest.'
    }
    return render(request, 'interest_site/about.html', context)

def getHtml(article):
    return f"""
        <h3>{article['title']}</h3>
        <p>{article['summary']}</p>
        <a href="{article['url']}">See more...</a>
    """