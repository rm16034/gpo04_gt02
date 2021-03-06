# Generated by Django 2.2.13 on 2020-06-25 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0002_beneficiado'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAyuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoAyuda', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEntidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTipoEntidad', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEntidad', models.CharField(max_length=100)),
                ('idTipoEntidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.TipoEntidad')),
            ],
        ),
        migrations.CreateModel(
            name='Ayuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBeneficiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.Beneficiado')),
                ('idEntidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.Entidad')),
                ('idTipoAyuda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.TipoAyuda')),
                ('idTipoEntidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.TipoEntidad')),
            ],
        ),
    ]
