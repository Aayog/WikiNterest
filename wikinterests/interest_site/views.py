from django.shortcuts import render

def home(request):
    context = {
        'title' : 'HOME'
    }
    return render(request, 'interest_site/home.html', context)


def about(request):
    context = {
        'title' : 'ABOUT',
        'content' : 'Wikinterest is a site that has articles based on users interest.'
    }
    return render(request, 'interest_site/about.html', context)
