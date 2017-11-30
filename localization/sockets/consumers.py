from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
from ..models import CarStatus
from ..api.serializers import CarStatusModelSerializer
from django.http import Http404
from math import sin, cos, sqrt, atan2, radians


class StatusConsumer(JsonWebsocketConsumer):

    def get_object(self, pk):
        try:
            return CarStatus.objects.get(car_number=pk)
        except CarStatus.DoesNotExist:
            raise Http404

    def get_cars_radius(self, car_lat, car_lon):
        sm_car_lat = float(car_lat) - 0.020000
        lg_car_lat = float(car_lat) + 0.020000
        sm_car_lon = float(car_lon) - 0.030000
        lg_car_lon = float(car_lon) + 0.030000
        cars = CarStatus.objects.filter(car_lat__lte=lg_car_lat, car_lat__gte=sm_car_lat,car_lon__lte=lg_car_lon, car_lon__gte=sm_car_lon)
        return cars

    def connect(self, message, multiplexer, **kwargs):
        multiplexer.send({"status": "I just connected!"})

    def receive(self, content, multiplexer, **kwargs):
        print(content['car_lat'])
        car_status = self.get_object(content['car_number'])
        serializer = CarStatusModelSerializer(car_status, data=content, partial=True)
        if serializer.is_valid():
            serializer.save()
        cars = self.get_cars_radius(content['car_lat'], content['car_lon'])
        cars_serializer = CarStatusModelSerializer(cars, many=True)
        multiplexer.send(cars_serializer.data)


    def disconnect(self, message, multiplexer, **kwargs):
        print("Stream %s is closed" % multiplexer.stream)


class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "status": StatusConsumer,
    }