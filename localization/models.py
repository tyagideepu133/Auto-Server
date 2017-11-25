from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    user = models.OneToOneField(User)
    driver_name = models.CharField(max_length=150)
    driver_dob = models.DateField()
    driver_uidai = models.IntegerField(unique=True)
    driver_password = models.CharField(max_length=30,default="123456")
    driver_dl = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.driver_name)
