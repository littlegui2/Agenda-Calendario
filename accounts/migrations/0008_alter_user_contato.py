# Generated by Django 4.0.5 on 2022-11-02 11:09

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contato',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', help_text='Insira um número válido.', max_length=128, region='BR', unique=True),
        ),
    ]
