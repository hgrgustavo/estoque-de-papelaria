# Generated by Django 5.1.6 on 2025-02-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_cadastrolivros_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastrolivros',
            name='titulo',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
