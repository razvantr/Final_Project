from django.db import models
from django_google_maps import fields as map_fields


# Create your models here.
class StartLocation(models.Model):
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    address = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.district} {self.city}'
