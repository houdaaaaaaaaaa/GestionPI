from django.db import models

class Serveur(models.Model):
    type = models.CharField(max_length=100) 
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    processeur = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class BaieStockage(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class DisqueDurSSD(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    interface = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class MemoireRAM(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    capacite = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Processeur(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    nombre_coeurs = models.IntegerField()
    frequence = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
