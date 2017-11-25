from django.contrib import admin

# Register your models here.
from .models import (Driver, Car, CarJourney, CarStatus)

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(CarJourney)
admin.site.register(CarStatus)