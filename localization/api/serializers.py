from rest_framework import serializers

from ..models import (Driver, Car, CarJourney, CarStatus, CarEmergency)


class DriverModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_dl',
            'driver_name',
            'driver_dob',
            'driver_uidai',
            'email',
            'password'
        ]


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'car_id',
            'car_password',
            'car_type',
        ]


class CarStatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarStatus
        fields = [
            'car_lat',
            'car_lon',
            'car_speed',
            'car_fuel',
            'car_temp',
            'car_status',
            'car_number',
            'car_type',
            'car_driver_id'
        ]


class CarJourneyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarJourney
        fields = [
            'id',
            'jstart_lat',
            'jstart_lon',
            'jend_lat',
            'jend_lon',
            'javg_speed',
            'jfuel_con',
            'jend_status',
            'jcar_number',
            'jdriver_id',
            'jdate',
            'jstart_time',
            'jend_time'
        ]


class EmergencyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEmergency
        fields = [
            'id',
            'vc_start_lat',
            'vc_start_lon',
            'vc_end_lat',
            'vc_end_lon',
            'vc_current_lat',
            'vc_current_lon',
            'ec_start_lat',
            'ec_start_lon',
            'ec_end_lat',
            'ec_end_lon',
            'ec_current_lat',
            'ec_current_lon',
            'vc_end_status',
            'ec_car_number',
            'ec_driver_id',
            'vc_car_number',
            'vc_driver_id',
            'edate',
            'estart_time',
            'eend_time'
        ]
