from rest_framework import serializers

from ..models import (Driver, Car, CarJourney, CarStatus)

class DriverModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_dl',
            'driver_name',
            'driver_dob',
            'driver_uidai',
            'user',
        ]
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'car_id',
            'car_password',
            'car_type',
        ]
class CarJourneyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarJourney
        fields = [
        'jstart_lat',
        'jstart_lon',
        'jend_lat',
        'jend_lon',
        'javg_speed',
        'jfuel_con',
        'jend_status',
        'jcar_number',
        'jdriver_id',]