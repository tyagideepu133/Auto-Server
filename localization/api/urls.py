from django.conf.urls import url, include
from .views import (DriverAPIView, CarAPIView, DriverDetailAPIView, CarDetailAPIView)

urlpatterns = [
    url(r'^drivers/$', DriverAPIView.as_view(), name='drivers'),
    url(r'^cars/$', CarAPIView.as_view(), name='cars'),
    url(r'^drivers/(?P<pk>[0-9]+)/$', DriverDetailAPIView.as_view(), name='driver'),
    url(r'^cars/(?P<username>\w+)/$', CarDetailAPIView.as_view(), name='cars')
]
