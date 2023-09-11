from django.db import models
from driver.models import Driver


# Create your models here.
class Car(models.Model):

    plate = models.CharField(max_length=9)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate
