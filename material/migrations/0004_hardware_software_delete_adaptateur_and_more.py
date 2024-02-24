# Generated by Django 5.0.1 on 2024-02-20 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_adaptateur_baiestockage_bandemagnetique_cable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=100, unique=True)),
                ('fabricant', models.CharField(max_length=100)),
                ('fournisseur', models.CharField(max_length=100)),
                ('date_achat', models.DateField()),
                ('date_garantie_expiration', models.DateField()),
                ('date_maintenance', models.DateField(blank=True, null=True)),
                ('etat', models.CharField(choices=[('actif', 'Actif'), ('en_panne', 'En Panne'), ('en_reparation', 'En Réparation'), ('en_maintenance', 'En Maintenance'), ('obsolete', 'Obsolète')], max_length=20)),
                ('utilisateur_actuel', models.CharField(blank=True, max_length=100, null=True)),
                ('emplacement', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=50)),
                ('licence', models.CharField(max_length=100)),
                ('date_achat', models.DateField()),
                ('date_fin_support', models.DateField()),
                ('utilisateur_actuel', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('equipement_utilise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='material.hardware')),
            ],
        ),
        migrations.DeleteModel(
            name='Adaptateur',
        ),
        migrations.DeleteModel(
            name='BaieStockage',
        ),
        migrations.DeleteModel(
            name='BandeMagnetique',
        ),
        migrations.DeleteModel(
            name='Cable',
        ),
        migrations.DeleteModel(
            name='CameraSurveillanceIP',
        ),
        migrations.DeleteModel(
            name='Clavier',
        ),
        migrations.DeleteModel(
            name='Commutateur',
        ),
        migrations.DeleteModel(
            name='DisqueDurExterne',
        ),
        migrations.DeleteModel(
            name='DisqueDurInterne',
        ),
        migrations.DeleteModel(
            name='DisqueOptique',
        ),
        migrations.DeleteModel(
            name='DisqueReseau',
        ),
        migrations.DeleteModel(
            name='EcranInteractif',
        ),
        migrations.DeleteModel(
            name='Fax',
        ),
        migrations.DeleteModel(
            name='HautParleur',
        ),
        migrations.DeleteModel(
            name='Imprimante',
        ),
        migrations.DeleteModel(
            name='LecteurBande',
        ),
        migrations.DeleteModel(
            name='Microphone',
        ),
        migrations.DeleteModel(
            name='Modem',
        ),
        migrations.DeleteModel(
            name='Moniteur',
        ),
        migrations.DeleteModel(
            name='OrdinateurBureau',
        ),
        migrations.DeleteModel(
            name='OrdinateurPortable',
        ),
        migrations.DeleteModel(
            name='PareFeu',
        ),
        migrations.DeleteModel(
            name='Photocopieur',
        ),
        migrations.DeleteModel(
            name='PointAccesWiFi',
        ),
        migrations.DeleteModel(
            name='Projecteur',
        ),
        migrations.DeleteModel(
            name='Routeur',
        ),
        migrations.DeleteModel(
            name='Scanner',
        ),
        migrations.DeleteModel(
            name='ServeurPhysique',
        ),
        migrations.DeleteModel(
            name='ServeurVirtuel',
        ),
        migrations.DeleteModel(
            name='Souris',
        ),
        migrations.DeleteModel(
            name='SSD',
        ),
        migrations.DeleteModel(
            name='SupportStockageAmovible',
        ),
        migrations.DeleteModel(
            name='SystemeControleAcces',
        ),
        migrations.DeleteModel(
            name='SystemeVisioconference',
        ),
        migrations.DeleteModel(
            name='Webcam',
        ),
    ]
