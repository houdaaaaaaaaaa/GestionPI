# Generated by Django 5.0.1 on 2024-02-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlimentationSansInterruption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('puissance', models.CharField(max_length=100)),
                ('autonomie', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SauvegardeSurBande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('capacite', models.CharField(max_length=100)),
                ('vitesse', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SauvegardeSurDisque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('capacite', models.CharField(max_length=100)),
                ('type_connexion', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SurveillanceReseauSecurite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('type_surveillance', models.CharField(max_length=100)),
                ('fonctionnalites', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
    ]