# Generated by Django 4.0.5 on 2022-06-21 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oficina', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome_mae',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome_pai',
        ),
    ]