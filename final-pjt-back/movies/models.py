from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Ott(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movies')
    otts = models.ManyToManyField(Ott, related_name='movies')
    overview = models.TextField()
    release_date = models.DateField()
    popularity = models.FloatField()
    adult = models.BooleanField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    backdrop_path = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    key = models.CharField(max_length=50)