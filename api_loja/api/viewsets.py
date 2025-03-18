from rest_framework import viewsets 
from api_loja.api import serializer
from api_loja import models 
from drf_yasg.utils import swagger_auto_schema


class ClienteViewsets(viewsets.ModelViewSet):
    serializer_class = serializer.ClienteSerializer
    queryset = models.Cliente.objects.all()

    @swagger_auto_schema(
        operation_description="Lista de todos os clientes",
        responses={200: serializer.ClienteSerializer (many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(
        operation_description="Crie um novo cliente",
        responses={201: "Cliente criado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Altera o cliente conforme ID e dados informados",
        responses={200: "Cliente alterado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deletar o cliente conforme ID e dados informados",
        responses={200: "Cliente deletado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    

class MostruarioViewsets(viewsets.ModelViewSet):
    serializer_class= serializer.MostruarioSerializer
    queryset = models.Mostruario.objects.all()
   
    @swagger_auto_schema(
        operation_description="Listar todos os mostruários",
        responses={200: serializer.MostruarioSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #metodo get

    @swagger_auto_schema(
        operation_description="Criar um novo mostruário",
        responses={201:"Mostruário criado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #metodo post
    
    @swagger_auto_schema(
        operation_description="Alterar o mostruario conforme ID e dados informados",
        responses={200: "mostruario alterado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Deleta o mostruario confrome ID informado",
        responses={204: "mostruario deletada com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)




class CarrinhoViewsets(viewsets.ModelViewSet):
    serializer_class = serializer.CarrinhoSerializer
    queryset = models.Carrinho.objects.all()

    @swagger_auto_schema(
        operation_description="Listar carrinho",
        responses={200: serializer.MostruarioSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #metodo get

    @swagger_auto_schema(
        operation_description="Adicionar ao carrinho",
        responses={201:"Adicionado ao carrinho com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #metodo post
    
    @swagger_auto_schema(
        operation_description="Deletar carrinho",
        responses={200: "Carrinho apagado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    




class ItemCarrinhoViewsets(viewsets.ModelViewSet):
    serializer_class = serializer.ItemCarrinhoSerializer
    queryset = models.ItemCarrinho.objects.all()

    @swagger_auto_schema(
        operation_description="Listar todos os itens do carrinho",
        responses={200: serializer.CarrinhoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #metodo get
    @swagger_auto_schema(
        operation_description="Adicionar um novo item",
        responses={201:"Item adicionado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    #metodo post
    
    @swagger_auto_schema(
        operation_description="Altera item do carrinho",
        responses={200: "Alteração feita com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_description="Deleta o item do carrinho confrome ID informado",
        responses={204: "Item deletado com sucesso"}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
