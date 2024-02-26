from django.db import models

class Tablette(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille_ecran = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SmartphoneEntreprise(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class AccessoireMobile(models.Model):
    type = models.CharField(max_length=100)  # Par exemple étui, chargeur, etc.
    marque = models.CharField(max_length=100)
    compatible_modele = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
