from django.shortcuts import render
import django.http

# Create your views here.
#from .models import Question


def index(request):
    return render(request, 'estoque_app/index.html')


def add_entrada(request):
    return django.http.HttpResponseRedirect('/')

def add_entrada_form(request):
    return django.http.HttpResponseRedirect('/')


def add_produto(request):
    return django.http.HttpResponseRedirect('/')

def add_produto_form(request):
    return django.http.HttpResponseRedirect('/')


def ver_tabelas(request):
    return django.http.HttpResponseRedirect('/')

def contabilizar(request):
    return django.http.HttpResponseRedirect('/')
