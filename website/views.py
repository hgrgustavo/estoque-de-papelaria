from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from . import models

class Indexpage(TemplateView):
    template_name = "index.html"


class Cadastros(TemplateView):
    template_name = "cadastros.html"

class CadastroLivros(CreateView):
    template_name = "cadastro_livros.html"
    model = models.Livros

class CadastroAutores(CreateView):
    template_name = "cadastro_autores.html"
    model = models.Livros

class Estoque(CreateView):
    template_name = "estoque.html"
    model = models.Livros



