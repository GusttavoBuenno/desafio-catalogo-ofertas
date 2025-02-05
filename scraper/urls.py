from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('api/produtos/', views.api_lista_produtos, name='api_lista_produtos'),
]
