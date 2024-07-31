# Generated by Django 5.0.6 on 2024-07-30 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meuprojeto', '0003_servico_evidencia_execucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='Equipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Meuprojeto.equipe'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='Nota',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='servico',
            name='Projeto',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]