from django.db import models

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="Carros")
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name="Carros")

    def __str__(self):
        return self.modelo
