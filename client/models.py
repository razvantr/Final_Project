from django.db import models
from ride.models import Ride


# Create your models here.
class Client(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
