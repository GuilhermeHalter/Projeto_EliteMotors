from django.db import models
from elitemotors.models import Cor, Acessorio

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Carros")
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="Carros")

    def __str__(self):
        return self.modelo