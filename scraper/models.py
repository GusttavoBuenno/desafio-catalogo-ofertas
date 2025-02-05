from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    link = models.URLField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
