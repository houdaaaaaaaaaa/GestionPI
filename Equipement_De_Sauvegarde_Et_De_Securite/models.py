from django.db import models

class SauvegardeSurBande(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    vitesse = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SauvegardeSurDisque(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class AlimentationSansInterruption(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    puissance = models.CharField(max_length=100)
    autonomie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SurveillanceReseauSecurite(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_surveillance = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)