from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from elitemotors.models import Acessorio
from elitemotors.serializers import AcessorioSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer