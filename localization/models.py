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
    jstart_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    jstart_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    jend_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    jend_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    javg_speed = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    jfuel_con = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    jend_status = models.CharField(max_length=20, default="off", null=False)
    jcar_number = models.ForeignKey(Car)
    jdriver_id = models.ForeignKey(Driver)
    jdate = models.DateField(auto_now_add=True, null=True)
    jstart_time = models.TimeField(auto_now_add=True, null=True, editable=False)
    jend_time = models.TimeField(auto_now=True)


class CarEmergency(models.Model):
    vc_start_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    vc_start_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    vc_end_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    vc_end_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    vc_current_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    vc_current_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    ec_start_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    ec_start_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    ec_end_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    ec_end_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    ec_current_lat = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    ec_current_lon = models.DecimalField(null=False, default=0.0, max_digits=15, decimal_places=8)
    vc_end_status = models.CharField(max_length=20, default="off", null=False)
    ec_car_number = models.ForeignKey(Car)
    ec_driver_id = models.ForeignKey(Driver)
    ec_car_number = models.ForeignKey(Car)
    ec_driver_id = models.ForeignKey(Driver)
    edate = models.DateField(auto_now_add=True, null=True)
    estart_time = models.TimeField(auto_now_add=True, null=True, editable=False)
    eend_time = models.TimeField(auto_now=True)


    def __str__(self):
        return str(self.jcar_number)
