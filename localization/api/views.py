from rest_framework import generics

from ..models import Driver
from .serializers import DriverModelSerializer

class DriverListAPIView(generics.ListAPIView):
    serializer_class = DriverModelSerializer

    def get_queryset(self):
        return Driver.objects.all()
