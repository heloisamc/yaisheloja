from rest_framework import serializers
from api_loja import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Cliente
        fields = "__all__"

class MostruarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mostruario
        fields = "__all__"

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrinho 
        fields = "__all__"

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.ItemCarrinho
        fields = "__all__"