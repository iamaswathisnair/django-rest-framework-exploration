from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)  # Movie title
    director = models.CharField(max_length=255)  # Director name
    release_year = models.IntegerField()  # Release year
    genre = models.CharField(max_length=100)  # Movie genre

    def __str__(self):
        return self.title  # Show title in admin panel

