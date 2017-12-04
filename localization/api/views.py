from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import (Driver, Car, CarStatus, CarJourney, CarEmergency)
from .serializers import (DriverModelSerializer, CarModelSerializer, CarStatusModelSerializer,
                          CarJourneyModelSerializer, EmergencyModelSerializer)


class DriverListAPIView(APIView):

    def get(self, request):
        drivers = Driver.objects.all()
        serializer=DriverModelSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        driver = self.get_object(pk)
        serializer = DriverModelSerializer(driver)
        return Response(serializer.data)

    def put(self, request, pk):
        driver = self.get_object(pk)
        serializer = DriverModelSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        driver = self.get_object(pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarListAPIView(APIView):

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarModelSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=CarModelSerializer(data=request.data)
        if serializer.is_valid():
            # old_password = request.data['car_password']
            # salt = haser.salt()
            # new_password=haser.encode(old_password,"smart-car")
            # request.data['car_password']=new_password
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Car.objects.get(car_id=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, username):
        car = self.get_object(username)
        serializer = CarModelSerializer(car)
        return Response(serializer.data)

    def put(self, request, username):
        car = self.get_object(username)
        if 'car_password' in request.data:
            request.data['car_id'] = car.car_id
        else:
            request.data['car_password'] = car.car_password
            request.data['car_id'] = car.car_id
        serializer = CarModelSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        car = self.get_object(username)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarStatusListAPIView(APIView):

    def get(self, request):
        cars = CarStatus.objects.all()
        serializer = CarStatusModelSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=CarStatusModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarStatusDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return CarStatus.objects.get(car_number=pk)
        except CarStatus.DoesNotExist:
            raise Http404

    def get(self, request, username):
        car_status = self.get_object(username)
        serializer = CarStatusModelSerializer(car_status)
        return Response(serializer.data)

    def put(self, request, username):
        car_status = self.get_object(username)
        serializer = CarStatusModelSerializer(car_status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        car_status = self.get_object(username)
        car_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarsJourneyListAPIView(APIView):

    def get(self, request):
        cars_journey = CarJourney.objects.all()
        serializer = CarJourneyModelSerializer(cars_journey, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=CarJourneyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarJourneysListAPIView(APIView):

    def get_object(self, pk):
        try:
            return CarJourney.objects.filter(jcar_number=pk)
        except CarJourney.DoesNotExist:
            raise Http404

    def get(self, request, username):
        car_journeys = self.get_object(username)
        serializer = CarJourneyModelSerializer(car_journeys, many= True)
        car_journeys_res = {"results":serializer.data}
        return Response(car_journeys_res)


class CarJourneyDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return CarJourney.objects.get(pk=pk)
        except CarJourney.DoesNotExist:
            raise Http404

    def get(self, request, username, pk):
        car_journey = self.get_object(pk)
        serializer = CarJourneyModelSerializer(car_journey)
        return Response(serializer.data)

    def put(self, request, username, pk):
        car_journey = self.get_object(pk)
        serializer = CarJourneyModelSerializer(car_journey, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, pk):
        car_journeys = self.get_object(pk)
        car_journeys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmergencyListAPIView(APIView):

    def get(self, request):
        cars = CarEmergency.objects.all()
        serializer = EmergencyModelSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=EmergencyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmergencyDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return CarEmergency.objects.get(pk=pk)
        except CarEmergency.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        emergency = self.get_object(pk)
        serializer = EmergencyModelSerializer(emergency)
        return Response(serializer.data)

    def put(self, request, pk):
        emergency = self.get_object(pk)
        serializer = EmergencyModelSerializer(emergency, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emergency = self.get_object(pk)
        emergency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)