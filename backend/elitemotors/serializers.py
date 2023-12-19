from rest_framework.serializers import ModelSerializer

from elitemotors.models import Carro, Cor, Acessorio

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
