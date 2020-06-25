from django.db import models

# Create your models here.


class Transactions(models.Model):
    pass

class Role(models.Model):
    title = models.CharField(max_length=20)

class Client(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=90)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    local_govt = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    latlong = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=13)
    profile_picture = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
