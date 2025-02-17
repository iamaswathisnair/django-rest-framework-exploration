from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    rating = models.FloatField()
    
    def __str__(self):
        return self.title