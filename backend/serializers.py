from rest_framework import serializers
from .models import Chambres, Client
class ChambresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chambres
        fields="__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields="__all__"
