from django.db import models

class Cor(models.Model):
    descricao: models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
 
    def __str__(self):
        return self.modelo
# Create your models here.
