from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()
    link = models.URLField()
    desconto = models.FloatField()

    class Meta:
        db_table = 'scraper_produto'  # Tabela única
