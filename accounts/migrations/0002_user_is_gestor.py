# Generated by Django 4.0.5 on 2022-10-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_gestor',
            field=models.BooleanField(default=False),
        ),
    ]