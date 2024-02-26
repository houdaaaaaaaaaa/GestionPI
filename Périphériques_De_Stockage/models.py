from django.db import models

class DisqueDurExterne(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class CleUSB(models.Model):
    marque = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class CarteMemoire(models.Model):
    marque = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class LecteurDisqueOptique(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_disque = models.CharField(max_length=100)  # DVD, Blu-ray, etc.
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)