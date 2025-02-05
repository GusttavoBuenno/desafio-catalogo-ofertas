from django.shortcuts import render
from .scraper import coletar_produtos
from .models import Produto

def lista_produtos(request):
    # Coleta os produtos
    produtos = coletar_produtos()
    # Renderiza a página com a lista de produtos
    return render(request, 'scraper/lista_produtos.html', {'produtos': produtos})

def atualizar_produtos(request):
    # Coleta os produtos
    produtos = coletar_produtos()
    
    # Atualiza ou cria produtos no banco de dados
    for produto in produtos:
        Produto.objects.update_or_create(
            nome=produto['nome'],
            defaults={
                'preco': produto['preco'],
                'desconto': produto['desconto'],
                'link': produto['link']
            }
        )
    
    # Renderiza a página com os produtos atualizados
    return render(request, 'scraper/produtos_atualizados.html', {'produtos': produtos})
