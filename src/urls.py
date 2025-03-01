from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path("", views.Indexpage.as_view(), name="indexpage"), 
    path("cadastrar_livro/", views.CadastroLivros.as_view(), name="cadastrolivrospage"),
    path("cadastrar_autor/", views.CadastroAutores.as_view(), name="cadastroautorespage"),
    path("estoque/", views.Estoque.as_view(), name="estoquepage"),
    ]
