from django.db import models
from driver.models import Driver
from end_location.models import EndLocation
from start_location.models import StartLocation


# Create your models here.
class Ride(models.Model):

    starting_at = models.ForeignKey(StartLocation, on_delete=models.CASCADE)
    ending_at = models.ForeignKey(EndLocation, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    time = models.DateTimeField()
    price = models.IntegerField()

    def __str__(self):
        return f'From {self.starting_at} to {self.ending_at}, at {self.time}'
