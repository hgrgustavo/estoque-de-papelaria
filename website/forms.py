from django.forms import ModelForm, TextInput, NumberInput, Textarea 
from . import models


class CadastroLivrosForm(ModelForm):
    class Meta:
        model = models.Livros
        fields = [
                "título",
                "isbn",
                "edição",
                "editora",
                "ano_publicação",
                "preço_capa",
                "categoria",
        ]
        widgets = {
                "título": TextInput(attrs={"placeholder":"Título"}),
                "isbn": TextInput(attrs={"placeholder":"ISBN", "pattern":r'(?:[- ]*1[03])?:*((?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}|97[89][0-9]{10}|(?=(?:[0-9]+[- ]){4})[- 0-9]{17})(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X])'}),
                
                "edição": TextInput(attrs={"placeholder":"Edição" }),
                "editora": TextInput(attrs={"placeholder":"Editora"}),
                "ano_publicação": TextInput(attrs={"placeholder":"Ano de publicação", "max_length":4}),
                "preço_capa": TextInput(attrs={"placeholder":"Preço (R$) ", "min": 0}),
                "categoria": TextInput(attrs={"placeholder":"Categoria" }),
        }
       

class CadastroAutoresForm(ModelForm):
    class Meta:
        model = models.Autores
        fields = [
            "nome_completo",
            "nacionalidade",
            "biografia",
        ]
        widgets = {
            "nome_completo": TextInput(attrs={"placeholder":"Nome completo"}),
            "nacionalidade": TextInput(attrs={"placeholder":"Nacionalidade"}),
            "biografia": Textarea(attrs={"placeholder":"Biografia", "wrap":"hard", "cols":50}),
        }
