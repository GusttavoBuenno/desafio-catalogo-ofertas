from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from .selenium_scraper import obter_produtos

# Função para listar os produtos
def lista_produtos(request):
    produtos = Produto.objects.all()  # Lista todos os produtos armazenados
    return render(request, 'scraper/lista_produtos.html', {'produtos': produtos})

# Função para atualizar os produtos (utilizando a lógica de scraping)
def atualizar_produtos(request):
    produtos = obter_produtos()  # Chama a função do scraper para obter os dados

    # Atualiza ou cria novos produtos no banco de dados
    for produto in produtos:
        Produto.objects.update_or_create(
            nome=produto['nome'],
            defaults={'preco': produto['preco'], 'descricao': produto['descricao']}
        )

    return HttpResponse("Produtos atualizados com sucesso!")
