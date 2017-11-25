from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Driver
from .serializers import DriverModelSerializer

class DriverListAPIView(APIView):
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