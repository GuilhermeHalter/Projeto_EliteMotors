from django.db import models
from elitemotors.models import Cor, Acessorio
from uploader.models import Image


class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Carros")
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="Carros")
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return self.modelo