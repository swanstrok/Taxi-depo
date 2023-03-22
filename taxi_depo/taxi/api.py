import datetime

from rest_framework import viewsets

from .models import *
from .serializers import *


class PassengerAPIViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class CarAPIViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(body__body_type='Хэтчбэк')
    serializer_class = CarSerializer


class DriverAPIViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.filter(age__lte=40)
    serializer_class = DriverSerializer


class FlightAPIViewSet(viewsets.ModelViewSet):
    flight_date = datetime.date(2023, 3, 21)
    queryset = Flight.objects.filter(date_flight__date=(flight_date))
    serializer_class = FlightSerializer
