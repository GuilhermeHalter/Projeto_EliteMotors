from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from elitemotors.models import Carro, Cor
from elitemotors.serializers import CarroSerializer, CorSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer