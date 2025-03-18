from rest_framework import serializers
from api_loja import models

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Cliente
        fields = "__all__"
        extra_kwargs={
            'id' : {'help_text':'Identificador do cliente'},
            'nome': {'help_text': 'Nome do cliente'}
        }

class MostruarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mostruario
        fields = "__all__"
        extra_kwargs={
            'id' : {'help_text':'Identificador do mostruário'},
            'nome': {'help_text': 'nome do produto'},
            'DataAlt':{'help_text': 'data de alteração do mostruario'},
            'Descricao':{'help_text': 'Descrição do que mostruario'},
            'Foto': {'help_text': 'Foto da roupa'}
        }

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrinho 
        fields = "__all__"
        extra_kwargs={
            'id' : {'help_text':'Identificador do Carrinho'},
            'Cliente':{'help_text': 'nome do cliente '},
            'Data_Criacao':{'help_text':'Data da criação do carrinho'},
            'Ativo':{'help_text': 'Se o carrinho está ativo ou foi finalizado'},
        }

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.ItemCarrinho
        fields = "__all__"
        extra_kwagers={
            'id': {'help_text': 'Identificador do Item no carrinho'},
            'Carrinho': {'help_text': 'Relaciona o item com o carrinho'},
            'Produto': {'help_text': 'Item do monstruario'},
            'Quantidade':{'help_text': 'Quantidade de produtos'},
            'PrecoUnitario': {'help_text': 'Preço de cada produto unidade'},
        }