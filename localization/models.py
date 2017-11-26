from django.db import models
# from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Driver(models.Model):
    user = models.OneToOneField(User)
    driver_name = models.CharField(max_length=150)
    driver_dob = models.DateField()
    driver_uidai = models.IntegerField(unique=True)
    driver_dl = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.driver_name)


class Car(models.Model):
    car_id = models.CharField(max_length=20, unique=True, primary_key=True)
    car_password = models.CharField(max_length=150)
    car_type = models.CharField(max_length=20, default="normal")

    def __str__(self):
        return str(self.car_id)


class CarStatus(models.Model):
    car_lat = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    car_lon = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    car_speed = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    car_fuel = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    car_temp = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    car_status = models.CharField(max_length=20, default="off")
    car_number = models.OneToOneField(Car, primary_key=True)
    car_driver_id = models.ForeignKey(Driver)

    def __str__(self):
        return str(self.car_number)


class CarJourney(models.Model):
    jstart_lat = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    jstart_lon = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    jend_lat = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    jend_lon = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    javg_speed = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    jfuel_con = models.DecimalField(null=False, default=0.0, max_digits=6, decimal_places=6)
    jend_status = models.CharField(max_length=20, default="off")
    jcar_number = models.ForeignKey(Car)
    jdriver_id = models.ForeignKey(Driver)
    jdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.jcar_number)
