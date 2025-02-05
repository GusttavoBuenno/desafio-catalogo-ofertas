from django.db import models
import uuid

class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imagem = models.URLField()
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_sem_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentual_desc = models.FloatField(null=True, blank=True)
    parcelamento = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField()
    tipo_entrega = models.CharField(max_length=50, choices=[('Full', 'Full'), ('Normal', 'Normal')])
    frete_gratis = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'catalogo_produto'  # Garantindo que a tabela tenha um nome único
