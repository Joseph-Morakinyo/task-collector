from django.db import models
from django.contrib.auth.models import AbstractUser


# The OTP when used, changes the device-id

class User(AbstractUser, models.Model):
    device_id = models.CharField(max_length=12, null=False)
    authenticated = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now=True)


class OneTimePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
