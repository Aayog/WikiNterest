from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='site-home'),
    path('about', views.about, name='site-about')
]