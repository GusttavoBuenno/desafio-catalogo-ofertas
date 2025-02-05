from django.urls import path
from .views import lista_produtos

urlpatterns = [
    path('produtos/', lista_produtos, name='lista_produtos'),
]
