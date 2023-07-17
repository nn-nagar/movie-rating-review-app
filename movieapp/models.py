from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to ='uploads/')
    genres = models.CharField(max_length=200)
    ratings = models.IntegerField(null=True, blank=True)
    year_release = models.IntegerField(null=True, blank=True)
    metacritic_rating = models.CharField(max_length=200, null=True)
    runtime = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.title
