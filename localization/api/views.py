from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import BCryptPasswordHasher

from ..models import (Driver,Car)
from .serializers import (DriverModelSerializer, CarModelSerializer)

class DriverAPIView(APIView):
    def get(self, request, format = None):
        drivers = Driver.objects.all();
        serializer = DriverModelSerializer(drivers, many = True);
        return Response(serializer.data);

    def post(self, request, format = None):
        serializer = DriverModelSerializer(data = request.data);
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarAPIView(APIView):

    def get(self, request, format = None):
        cars = Car.objects.all();
        serializer = CarModelSerializer(cars, many = True);
        return Response(serializer.data);
    def post(self, request, format = None):
        haser = BCryptPasswordHasher();
        serializer = CarModelSerializer(data = request.data);
        if serializer.is_valid():
            old_password = request.data['car_password']
            salt = haser.salt()
            #new_password = haser.encode(old_password,"smart-car")
            #request.data['car_password'] = new_password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
