from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from elitemotors.models import Carro
from elitemotors.serializers import CarroSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
