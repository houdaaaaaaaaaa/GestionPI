from django.db import models

class CableEthernet(models.Model):
    longueur = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Catégorie (par exemple Cat5e, Cat6)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class CableUSB(models.Model):
    longueur = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Type (par exemple USB-A vers USB-B)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Adaptateur(models.Model):
    type_entree = models.CharField(max_length=100)
    type_sortie = models.CharField(max_length=100)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Connecteur(models.Model):
    type = models.CharField(max_length=100)  # Type (par exemple HDMI, VGA)
    fonctionnalites = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
