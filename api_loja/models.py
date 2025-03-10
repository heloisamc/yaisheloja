from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)  # Nome do cliente
    email = models.EmailField(unique=True)  # Email único
    senha = models.CharField(max_length=100)  # Senha (idealmente criptografada)
    telefone = models.CharField(max_length=15, blank=True, null=True)  # Telefone (opcional)

    def __str__(self):
        return self.nome
    
class Mostruario(models.Model):
    nome = models.CharField(max_length=200)  # Nome da roupa
    foto = models.ImageField(upload_to='mostruario_fotos/')  # Foto da roupa, armazenada na pasta 'mostruario_fotos'
    descricao = models.TextField()  # Descrição da roupa

    def __str__(self):
        return self.nome
    
class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relaciona o carrinho ao cliente
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação do carrinho
    ativo = models.BooleanField(default=True)  # Se o carrinho está ativo ou foi finalizado

    def __str__(self):
        return f'Carrinho de {self.cliente.nome}'

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)  # Relaciona o item ao carrinho
    produto = models.ForeignKey(Mostruario, on_delete=models.CASCADE)  # Produto (item do mostruário)
    quantidade = models.PositiveIntegerField(default=1)  # Quantidade do item no carrinho
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Preço de cada unidade do item

    def __str__(self):
        return f'{self.quantidade} x {self.produto.nome}'

    def total_item(self):
        """Retorna o preço total desse item (quantidade * preço unitário)."""
        return self.quantidade * self.preco_unitario

