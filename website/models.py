from django.db import models

class Livros(models.Model):
    título = models.CharField(max_length=45)
    isbn = models.CharField(max_length=17)
    edição = models.CharField(max_length=45)
    editora = models.CharField(max_length=45)
    ano_publicação = models.TextField()  # This field type is a guess.
    preço_capa = models.FloatField()
    categoria = models.CharField(max_length=45)

    class Meta:
        
        db_table = 'livros'


class Autores(models.Model):
    nome_completo = models.CharField(max_length=45)
    nacionalidade = models.CharField(max_length=45)
    biografia = models.TextField()

    class Meta:
        
        db_table = 'autores'


class Estoque(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    livros = models.ForeignKey('Livros', models.DO_NOTHING)

    class Meta:
        
        db_table = 'estoque'
        unique_together = (('id', 'livros'),)





class LivrosHasAutores(models.Model):
    livros = models.OneToOneField(Livros, models.DO_NOTHING, primary_key=True)  
    autores = models.ForeignKey(Autores, models.DO_NOTHING)

    class Meta:
        
        db_table = 'livros_has_autores'
        unique_together = (('livros', 'autores'),)
