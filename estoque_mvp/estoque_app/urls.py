from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_entrada', views.add_entrada),
    path('add_entrada_form', views.add_entrada_form),

    path('add_produto', views.add_produto),
    path('add_produto_form', views.add_produto_form),

    path('ver_tabelas', views.ver_tabelas),
    path('contabilizar', views.contabilizar),
]
