from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from elitemotors.models import Cor
from elitemotors.serializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer