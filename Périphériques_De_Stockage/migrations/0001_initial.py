# Generated by Django 5.0.1 on 2024-02-26 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarteMemoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('capacite', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CleUSB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('capacite', models.CharField(max_length=100)),
                ('interface', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DisqueDurExterne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('capacite', models.CharField(max_length=100)),
                ('interface', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LecteurDisqueOptique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('type_disque', models.CharField(max_length=100)),
                ('interface', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_achat', models.DateField()),
                ('statut', models.CharField(max_length=100)),
            ],
        ),
    ]
