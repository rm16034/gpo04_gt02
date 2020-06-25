# Generated by Django 2.2.13 on 2020-06-25 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0004_auto_20200624_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ayuda',
            old_name='Beneficiado',
            new_name='beneficiado',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='Entidad',
            new_name='entidad',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='TipoAyuda',
            new_name='iipoAyuda',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='TipoEntidad',
            new_name='tipoEntidad',
        ),
        migrations.RenameField(
            model_name='beneficiado',
            old_name='Departamento',
            new_name='departamento',
        ),
        migrations.RenameField(
            model_name='beneficiado',
            old_name='Municipio',
            new_name='municipio',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='Zona',
            new_name='zona',
        ),
        migrations.RenameField(
            model_name='entidad',
            old_name='TipoEntidad',
            new_name='tipoEntidad',
        ),
        migrations.RenameField(
            model_name='municipio',
            old_name='Departamento',
            new_name='departamento',
        ),
    ]