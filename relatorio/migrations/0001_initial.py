# Generated by Django 4.0.5 on 2022-10-15 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32, verbose_name='Digite o nome da equipe')),
                ('codigoV', models.CharField(max_length=32, verbose_name='Digite o codigo do vendedor')),
                ('contato', models.IntegerField(verbose_name='Contato')),
            ],
        ),
        migrations.CreateModel(
            name='Relatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('frequencia', models.IntegerField()),
                ('data', models.CharField(choices=[('segunda', 'segunda'), ('terça', 'terça'), ('quarta', 'quarta'), ('quinta', 'quinta'), ('sexta', 'sexta')], max_length=20)),
                ('mes', models.CharField(default='', max_length=10)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('equipeNome', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='relatorio.equipe', verbose_name='Nome da Equipe')),
            ],
        ),
    ]
