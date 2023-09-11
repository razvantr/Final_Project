from django.db import models
from ride.models import Ride


# Create your models here.
class Client(models.Model):

    name = models.CharField(max_length=60)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
