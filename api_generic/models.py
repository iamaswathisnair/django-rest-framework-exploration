from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name
    
