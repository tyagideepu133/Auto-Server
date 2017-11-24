from django.conf.urls import url, include
from .views import (DriverListAPIView)

urlpatterns = [
    url(r'^drivers/', DriverListAPIView.as_view(), name='drivers')
]
