from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.models import Car
from api.serializers import CarSerializer
from example.permissions import CarPermission


class CarList(ListCreateAPIView):
    """
    API for /api/cars
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CarPermission,)


class CarListDetail(RetrieveUpdateDestroyAPIView):
    """
    API for /api/cars/:id
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CarPermission,)
