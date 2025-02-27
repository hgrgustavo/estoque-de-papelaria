
from django.db import models
from django.core import validators
from datetime import datetime


class Autores(models.Model):
    nome_completo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=45)
    biografia = models.CharField(max_length=1000)

    class Meta:
        
        db_table = 'cadastro_autores'


class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=17, validators=[validators.RegexValidator(regex=r'^(?:\d[\ |-]?){13}$')])
    edição = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    ano_publicação = models.IntegerField(validators=[validators.MaxValueValidator(datetime.now().year + 2)])  # This field type is a guess.
    preço_capa = models.FloatField()
    categoria = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'cadastro_livros'


class LivrosHasAutores(models.Model):
    cadastro_livros = models.OneToOneField(Livros, models.DO_NOTHING, primary_key=True)  # The composite primary key (cadastro_livros_id, cadastro_autores_id) found, that is not supported. The first column is selected.
    cadastro_autores = models.ForeignKey(Autores, models.DO_NOTHING)

    class Meta:
        
        db_table = 'cadastro_livros_has_cadastro_autores'
        unique_together = (('cadastro_livros', 'cadastro_autores'),)


class ControleEstoque(models.Model):
    cadastro_livros = models.ForeignKey(Livros, models.DO_NOTHING)
    data_entrada = models.DateField()
    data_saida = models.DateField()

    class Meta:
        
        db_table = 'controle_estoque'
        unique_together = (('id', 'cadastro_livros'),)
