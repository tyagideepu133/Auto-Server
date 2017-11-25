from django.conf.urls import url, include
from .views import (DriverAPIView, CarAPIView)

urlpatterns = [
    url(r'^drivers/', DriverAPIView.as_view(), name='drivers'),
    url(r'^cars/', CarAPIView.as_view(), name='cars'),
]
