from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('atualizar/', views.atualizar_produtos, name='atualizar_produtos'),
]
