from django.forms import ModelForm
from . import models 

class CadastroLivro(ModelForm):
    class Meta:
        model = models.CadastroLivros
        fields = "__all__"


class CadastroAutor(ModelForm):
    class Meta:
        model = models.CadastroAutores
        fields = "__all__"

