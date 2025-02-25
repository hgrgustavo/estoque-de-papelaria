from django.core import validators
from django.db import models
import datetime


class CadastroAutores(models.Model):
    nome_completo = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)
    biografia = models.CharField(max_length=1000)
    cadastro_livros = models.ForeignKey('CadastroLivros', models.DO_NOTHING)

    class Meta:
        
        db_table = 'cadastro_autores'
        unique_together = (('id', 'cadastro_livros'),)


class CadastroLivros(models.Model):
    titulo = models.CharField(max_length=255, default='null')
    isbn = models.CharField(max_length=13, validators=[validators.RegexValidator(regex='^(97(8|9))?-[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]{1}$|^(97(8|9))?[0-9]{9}([0-9]|X)$', message='ISBN inválido')])
    edicao = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField(
            validators=[
            validators.MinValueValidator(1960),
            validators.MaxValueValidator(datetime.datetime.now().year + 2)
        ])
    preco_capa = models.FloatField()
    categoria = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'cadastro_livros'


class ControleEstoque(models.Model):
    quantidade_livros = models.IntegerField()
    controle_estoquecol = models.IntegerField()
    data_entrada_livro = models.DateField()
    data_saida_livro = models.DateField()
    cadastro_livros = models.ForeignKey(CadastroLivros, models.DO_NOTHING)

    class Meta:
        
        db_table = 'controle_estoque'
        unique_together = (('id', 'cadastro_livros'),)
