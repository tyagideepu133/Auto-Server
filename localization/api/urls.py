from django.conf.urls import url, include
from .views import (DriverListAPIView, CarListAPIView, CarStatusListAPIView, CarsJourneyListAPIView,
                    CarJourneysListAPIView, EmergencyListAPIView, DriverDetailAPIView, CarDetailAPIView,
                    CarStatusDetailAPIView, CarJourneyDetailAPIView, EmergencyDetailAPIView)

urlpatterns = [
    url(r'^drivers/$', DriverListAPIView.as_view(), name='drivers'),
    url(r'^cars/$', CarListAPIView.as_view(), name='cars'),
    url(r'^emergency/$', EmergencyListAPIView.as_view(), name='cars'),
    url(r'^cars/status/$', CarStatusListAPIView.as_view(), name='cars-status'),
    url(r'^cars/journey/$', CarsJourneyListAPIView.as_view(), name='cars-journey'),
    url(r'^drivers/(?P<pk>[0-9]+)/$', DriverDetailAPIView.as_view(), name='driver'),
    url(r'^emergency/(?P<pk>[0-9]+)/$', EmergencyDetailAPIView.as_view(), name='driver'),
    url(r'^cars/(?P<username>\w+)/$', CarDetailAPIView.as_view(), name='cars'),
    url(r'^cars/(?P<username>\w+)/status/$', CarStatusDetailAPIView.as_view(), name='cars'),
    url(r'^cars/(?P<username>\w+)/journeys/$', CarJourneysListAPIView.as_view(), name='car-journeys'),
    url(r'^cars/(?P<username>\w+)/journeys/(?P<pk>[0-9]+)/$', CarJourneyDetailAPIView.as_view(), name='car-journey'),
]
