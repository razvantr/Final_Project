from django.db import models


# Create your models here.
class EndLocation(models.Model):
    city = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    address = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.district} {self.city}'
