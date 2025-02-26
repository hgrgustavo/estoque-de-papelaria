from django.views.generic import TemplateView, CreateView, ListView, DeleteView 
from . import models, forms
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = "index.html"

class CadastroLivro(CreateView):
    template_name = "cadastro_livro.html"
    model = models.CadastroLivros
    form_class = forms.CadastroLivro
    success_url = reverse_lazy("cadastro_livro_sucesso")

class CadastroAutor(CreateView):
    template_name = "cadastro_autor.html"
    model = models.CadastroAutores
    form_class = forms.CadastroAutor
    success_url = reverse_lazy("cadastro_autor_sucesso")

class ControleEstoque(ListView):
    template_name = "controle_estoque.html"
    model = models.CadastroLivros
    context_object_name = "estoque"

class SucessoView(TemplateView):
    template_name = "success.html"

class DeleteLivro(DeleteView):
    model = models.CadastroLivros
    success_url = "ajax_delete"

