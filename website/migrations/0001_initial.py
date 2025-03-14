# Generated by Django 5.1.6 on 2025-02-28 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=45)),
                ('nacionalidade', models.CharField(max_length=45)),
                ('biografia', models.TextField()),
            ],
            options={
                'db_table': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=45)),
                ('isbn', models.CharField(max_length=17)),
                ('edição', models.CharField(max_length=45)),
                ('editora', models.CharField(max_length=45)),
                ('ano_publicação', models.TextField()),
                ('preço_capa', models.FloatField()),
                ('categoria', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'livros',
            },
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField()),
                ('livros', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.livros')),
            ],
            options={
                'db_table': 'estoque',
                'unique_together': {('id', 'livros')},
            },
        ),
        migrations.CreateModel(
            name='LivrosHasAutores',
            fields=[
                ('livros', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='website.livros')),
                ('autores', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.autores')),
            ],
            options={
                'db_table': 'livros_has_autores',
                'unique_together': {('livros', 'autores')},
            },
        ),
    ]
