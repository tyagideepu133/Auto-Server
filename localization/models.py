from django.db import models
from django.conf import settings


# Create your models here.
class Driver(models.Model):
    driver_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=150)
    data_of_birth = models.DateField()
    addhar_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.name, self.driver_id, self.data_of_birth, self.addhar_number)
