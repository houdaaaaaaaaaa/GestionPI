from django.db import models

class VentilateurBoitier(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    niveau_bruit = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SystemeRefroidissementLiquide(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Type de système (par exemple AIO, custom loop)
    capacite_refroidissement = models.CharField(max_length=100)
    niveau_bruit = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)