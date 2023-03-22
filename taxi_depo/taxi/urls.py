from django.urls import path, include
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register(r'passenger', PassengerAPIViewSet)
router.register(r'car', CarAPIViewSet)
router.register(r'driver', DriverAPIViewSet)
router.register(r'flight', FlightAPIViewSet)

urlpatterns = [

]

urlpatterns += router.urls