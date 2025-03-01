from django.forms import ModelForm, TextInput, NumberInput
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
                
                "edição": TextInput(attrs={"placeholder":"Edição","onchange": "this.options[0].hidden=true;" }),
                "editora": TextInput(attrs={"placeholder":"Editora", "onchange": "this.options[0].hidden=true;" }),
                "ano_publicação": TextInput(attrs={"placeholder":"Ano de publicação", "max_length":4, "onchange": "this.options[0].hidden=true;"}),
                "preço_capa": TextInput(attrs={"placeholder":"Preço", "min": 0,"onchange": "this.options[0].hidden=true;" }),
                "categoria": TextInput(attrs={"placeholder":"Categoria","onchange": "this.options[0].hidden=true;" }),
        }
        
