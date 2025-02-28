from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path("", views.Indexpage.as_view(), name="indexpage"),
    path("cadastros/", views.Cadastros.as_view(), name="cadastrospage"),
    path("cadastros/livros/", views.CadastroLivros.as_view(), name="cadastrolivrospage"),
    path("cadastros/autores/", views.CadastroAutores.as_view(), name="cadastroautorespage"),
    path("estoque/", views.Estoque.as_view(), name="estoquepage"),
    ]
