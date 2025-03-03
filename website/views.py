from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from . import models, forms
from django.db.models import Sum, Count

class Indexpage(TemplateView):
    template_name = "index.html"


class CadastroLivros(CreateView):
    template_name = "cadastro_livros.html"
    model = models.Livros
    form_class = forms.CadastroLivrosForm 
    success_url = "#"


class CadastroAutores(CreateView):
    template_name = "cadastro_autores.html"
    model = models.Livros
    form_class = forms.CadastroAutoresForm
    success_url = "#"


class Estoque(ListView):
    template_name = "estoque.html"
    model = models.Livros
    context_object_name = "livros"
    
    def getSaldo(self):
        return models.Livros.objects.aggregate(saldo=Sum("preço_capa"))["saldo"]

    def getTotalLivros(self):
        return models.Livros.objects.aggregate(quantidade_livros=Count("id"))["quantidade_livros"]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saldo"] = self.getSaldo()
        context["quantidade_livros"] = self.getTotalLivros()
        return context




