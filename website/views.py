from django.views.generic import TemplateView, CreateView, ListView 
from . import models, forms

class Home(TemplateView):
    template_name = "index.html"

class CadastroLivro(CreateView):
    template_name = "cadastro_livro.html"
    model = models.CadastroLivros
    form_class = forms.CadastroLivro

class CadastroAutor(CreateView):
    template_name = "cadastro_autor.html"
    model = models.CadastroAutores
    form_class = forms.CadastroAutor


class ControleEstoque(ListView):
    template_name = "controle_estoque.html"
    model = models.CadastroLivros
    context_object_name = "estoque"
