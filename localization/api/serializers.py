from rest_framework import serializers

from ..models import Driver

class DriverModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_id',
            'driver_name',
            'driver_dob',
            'driver_uidai',
            'driver_password'
        ]