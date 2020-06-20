from django.db import models

# Create your models here.


class Waste(models.Model):
    userID = models.CharField(max_length=20)
    operatorID = models.CharField(max_length=20)
    pickup_time = models.DateTimeField()
    pickup_long = models.IntegerField()
    pickup_lat = models.IntegerField()