from django.db import models

class Routeur(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    ports = models.IntegerField()
    vitesse = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Commutateur(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    ports = models.IntegerField()
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class PareFeu(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    nombre_interfaces = models.IntegerField()
    type = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class PointAccesSansFil(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    standard_wifi = models.CharField(max_length=100)
    nombre_antennes = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
