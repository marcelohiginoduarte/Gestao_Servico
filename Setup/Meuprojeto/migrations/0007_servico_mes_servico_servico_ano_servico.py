# Generated by Django 5.0.6 on 2024-07-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meuprojeto', '0006_alter_servico_equipe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='Mes_servico',
            field=models.CharField(blank=True, choices=[('Jan', 'Janeiro'), ('Fev', 'Fevereiro'), ('Mar', 'Março'), ('Abr', 'Abril'), ('Mai', 'Maio'), ('Jun', 'Junho'), ('Julho', 'Julho'), ('Ago', 'Agosto'), ('Set', 'Setembro'), ('Out', 'Outubro'), ('Nov', 'Novembro'), ('Dez', 'Desembro')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='ano_servico',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
