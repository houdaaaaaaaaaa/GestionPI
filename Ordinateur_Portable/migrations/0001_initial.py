# Generated by Django 5.0.1 on 2024-02-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chargeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('compatibilite', models.CharField(max_length=100)),
                ('puissance_sortie', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ordinateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('numero_serie', models.CharField(max_length=100)),
                ('processeur', models.CharField(max_length=100)),
                ('memoire_ram', models.CharField(max_length=100)),
                ('capacite_stockage', models.CharField(max_length=100)),
                ('carte_graphique', models.CharField(max_length=100)),
                ('systeme_exploitation', models.CharField(max_length=100)),
                ('taille_ecran', models.CharField(max_length=100)),
                ('autonomie_batterie', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
    ]
