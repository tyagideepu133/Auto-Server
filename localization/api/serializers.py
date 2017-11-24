from rest_framework import serializers

from ..models import Driver

class DriverModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_id',
            'name',
            'data_of_birth',
            'addhar_number'
        ]