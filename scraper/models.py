from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)  # Nome do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    descricao = models.TextField()  # Descrição do produto

    def __str__(self):
        return self.nome
