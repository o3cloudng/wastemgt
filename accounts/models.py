from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    state = models.CharField(max_length=200)
    profile_pics = models.ImageField(upload_to="pics",max_length=100, default="default.jpg")
    address = models.TextField(max_length=200)
    lga = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username