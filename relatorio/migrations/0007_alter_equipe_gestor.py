# Generated by Django 4.0.5 on 2022-11-02 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_codigo_user_is_func_user_nome'),
        ('relatorio', '0006_remove_equipe_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='gestor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='accounts.gestor'),
        ),
    ]
