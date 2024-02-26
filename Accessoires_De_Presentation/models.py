from django.db import models

class Projecteur(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    luminosite = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Type de projecteur (par exemple DLP, LCD)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class EcranInteractif(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
