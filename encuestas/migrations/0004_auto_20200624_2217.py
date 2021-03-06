# Generated by Django 2.2.13 on 2020-06-25 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0003_ayuda_entidad_tipoayuda_tipoentidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ayuda',
            old_name='idBeneficiado',
            new_name='Beneficiado',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='idEntidad',
            new_name='Entidad',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='idTipoAyuda',
            new_name='TipoAyuda',
        ),
        migrations.RenameField(
            model_name='ayuda',
            old_name='idTipoEntidad',
            new_name='TipoEntidad',
        ),
        migrations.RenameField(
            model_name='beneficiado',
            old_name='idDepartamento',
            new_name='Departamento',
        ),
        migrations.RenameField(
            model_name='beneficiado',
            old_name='idMunicipio',
            new_name='Municipio',
        ),
        migrations.RenameField(
            model_name='departamento',
            old_name='idZona',
            new_name='Zona',
        ),
        migrations.RenameField(
            model_name='entidad',
            old_name='idTipoEntidad',
            new_name='TipoEntidad',
        ),
        migrations.RenameField(
            model_name='municipio',
            old_name='idDepartamento',
            new_name='Departamento',
        ),
    ]
