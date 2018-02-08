from django.db import models

# Create your models here.
from django.db import models


class scrapedData(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    adress = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200)
    date = models.DateTimeField('date published')