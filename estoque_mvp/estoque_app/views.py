from django.shortcuts import render
import django.http

# Create your views here.
from .models import Produto, Entrada, Estoque


def index(request):
    return render(request, 'estoque_app/index.html')


def add_entrada(request):
    nova_entrada = Entrada(produto_id=Produto.objects.get(pk=request.GET['produto']),
                           quantidade=request.GET['qtd'])
    nova_entrada.save()
    return django.http.HttpResponseRedirect('/ver_tabelas')

def add_entrada_form(request):
    context = {'produtos': Produto.objects.all()}
    print(context)
    return render(request, 'estoque_app/entrada_form.html', context)


def add_produto(request):
    novo_produto = Produto(tipo=request.GET['tipo'],
                           categoria=request.GET['categoria'])
    novo_produto.save()
    return django.http.HttpResponseRedirect('/ver_tabelas')

def add_produto_form(request):
    return render(request, 'estoque_app/produto_form.html')


def ver_tabelas(request):
    context = {'produtos': Produto.objects.all(),
               'entradas': Entrada.objects.all(),
               'estoques': Estoque.objects.all()}
    return render(request, 'estoque_app/ver_tabelas.html', context)

def contabilizar(request):
    for entrada in Entrada.objects.all():
        print(entrada)
        print(entrada.produto_id)
        print(entrada.produto_id.id)
        estoque = Estoque.objects.get(produto_id=entrada.produto_id.id)
        estoque.estoque += entrada.quantidade

        # Somente salve um se o outro for deletado, e vice-versa
        _, __ = estoque.save(), entrada.delete()
    return django.http.HttpResponseRedirect('/ver_tabelas')
