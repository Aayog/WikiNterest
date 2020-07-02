from django.shortcuts import render

def home(request):
    context = {
        'title' : 'HOME'
    }
    return render(request, 'interest_site/home.html', context)