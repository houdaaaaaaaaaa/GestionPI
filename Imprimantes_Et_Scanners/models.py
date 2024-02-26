from django.db import models

class Imprimante(models.Model):
    TYPE_CHOICES = [
        ('Laser', 'Laser'),
        ('À jet d\'encre', 'À jet d\'encre')
    ]
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    vitesse_impression = models.CharField(max_length=100)
    resolution_impression = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Scanner(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_capteur = models.CharField(max_length=100)
    resolution_optique = models.CharField(max_length=100)
    vitesse_scan = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)