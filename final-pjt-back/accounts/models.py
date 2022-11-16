from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Genre

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    collection = models.ManyToManyField(Movie)
    genre_preference = models.ManyToManyField(Genre, related_name='prefer_users', through='Preference')

class Preference(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score = models.IntegerField()
    like = models.BooleanField()