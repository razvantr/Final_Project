from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Driver(models.Model):

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    date_hired = models.DateField()
    date_fired = models.DateField(null=True)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles_driver/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class HistoryDriver(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
