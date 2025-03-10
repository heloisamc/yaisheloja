from rest_framework import viewsets 
from api_loja.api import serializer
from api_loja import models 

class ClienteViewsets(viewsets.ModelViewSet):
    serializer_class = serializer.ClienteSerializer
    queryset = models.Cliente.objects.all()

class MostruarioViewsets(viewsets.ModelViewSet):
    serializer_class= serializer.MostruarioSerializer
    queryset = models.Mostruario.objects.all()

class CarrinhoViewsets(viewsets.ModelViewSet):
    serializer_class = serializer.CarrinhoSerializer
    queryset = models.Carrinho.objects.all()

class ItemCarrinhoViewsets(viewsets.ModelViewSet):
    serializer_class = serializer.ItemCarrinhoSerializer
    queryset = models.ItemCarrinho.objects.all()