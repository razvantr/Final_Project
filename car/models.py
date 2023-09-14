from django.contrib.auth.models import User
from django.db import models
from driver.models import Driver


# Create your models here.
class Car(models.Model):

    plate = models.CharField(max_length=9)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate


class HistoryCar(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
