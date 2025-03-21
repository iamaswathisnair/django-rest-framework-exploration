from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)