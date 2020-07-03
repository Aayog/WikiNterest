from django.db import models
from django.contrib.auth.models import  User

class Category(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    url =  models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    favorites = models.ManyToManyField(Article)

    def __str__(self):
        return f'{self.user.username} Profile'
