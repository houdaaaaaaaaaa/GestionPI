from django.db import models

class UC(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    processeur = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    carte_graphique = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
    ports_disponibles = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Moniteur(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    taille_ecran = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    type_panneau = models.CharField(max_length=100)
    connectivite = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Clavier(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    technologie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class Souris(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    type_connexion = models.CharField(max_length=100)
    technologie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class HautParleur(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    configuration_audio = models.CharField(max_length=100)
    puissance_sortie = models.CharField(max_length=100)
    connectivite = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
