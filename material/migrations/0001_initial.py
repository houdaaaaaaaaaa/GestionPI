# Generated by Django 5.0.1 on 2024-02-18 07:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Famille_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('hard', 'Matériel informatique'), ('soft', 'Logiciel')], max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('site_web', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=100)),
                ('marque', models.CharField(max_length=100)),
                ('duree_garantie', models.IntegerField()),
                ('duree_vie_debut', models.DateField()),
                ('duree_vie_fin', models.DateField()),
                ('date_affectation', models.DateField(blank=True, null=True)),
                ('statut', models.CharField(choices=[('actif', 'Actif'), ('en_panne', 'En panne'), ('en_reparation', 'En réparation')], max_length=100)),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.famille_material')),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.fournisseur')),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
