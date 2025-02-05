from django.shortcuts import render
from django.http import JsonResponse
from catalogo.models import Produto


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'scraper/lista_produtos.html', {'produtos': produtos})


def api_lista_produtos(request):
    produtos = Produto.objects.all()


    preco_min = request.GET.get('preco_min', None)
    preco_max = request.GET.get('preco_max', None)
    nome = request.GET.get('nome', None)


    if preco_min:
        try:
            preco_min = float(preco_min)
            produtos = produtos.filter(preco__gte=preco_min)
        except ValueError:
            return JsonResponse({'error': 'Preço mínimo inválido'}, status=400)

    if preco_max:
        try:
            preco_max = float(preco_max)
            produtos = produtos.filter(preco__lte=preco_max)
        except ValueError:
            return JsonResponse({'error': 'Preço máximo inválido'}, status=400)

    if nome:
        produtos = produtos.filter(nome__icontains=nome)


    if produtos.exists():
        produtos_data = list(produtos.values('nome', 'preco', 'link', 'percentual_desc', 'imagem', 'parcelamento', 'tipo_entrega', 'frete_gratis'))
        return JsonResponse({'produtos': produtos_data})
    else:
        return JsonResponse({'message': 'Nenhum produto encontrado no banco de dados.'})
