from rest_framework.serializers import ModelSerializer

from elitemotors.models import Carro

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"