from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from hackathon.models import Cargo
from hackathon.serializers import CargoSerializer

class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer