from django.shortcuts import render
from .models import Produto  # Certifique-se de que o modelo Produto está correto

def lista_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos no banco
    return render(request, 'lista_produtos.html', {'produtos': produtos})
