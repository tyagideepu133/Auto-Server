from channels.generic.websockets import WebsocketDemultiplexer, JsonWebsocketConsumer
from ..models import CarStatus
from ..api.serializers import CarStatusModelSerializer
from django.http import Http404


class StatusConsumer(JsonWebsocketConsumer):

    def get_object(self, pk):
        try:
            return CarStatus.objects.get(car_number=pk)
        except CarStatus.DoesNotExist:
            raise Http404

    def connect(self, message, multiplexer, **kwargs):
        multiplexer.send({"status": "I just connected!"})

    def receive(self, content, multiplexer, **kwargs):
        print(content['car_lat'])
        car_status = self.get_object(content['car_number'])
        serializer = CarStatusModelSerializer(car_status, data=content, partial=True)
        if serializer.is_valid():
            serializer.save()


    def disconnect(self, message, multiplexer, **kwargs):
        print("Stream %s is closed" % multiplexer.stream)


class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "status": StatusConsumer,
    }