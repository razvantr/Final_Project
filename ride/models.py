from django.contrib.auth.models import User
from django.db import models
from car.models import Car
from driver.models import Driver
from end_location.models import EndLocation
from start_location.models import StartLocation


# Create your models here.
class Ride(models.Model):

    starting_at = models.ForeignKey(StartLocation, on_delete=models.CASCADE)
    ending_at = models.ForeignKey(EndLocation, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    ride_time = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return f'From {self.starting_at} to {self.ending_at}, at {self.ride_time}'


class HistoryRide(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
