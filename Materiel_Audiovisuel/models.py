from django.db import models

class CameraVideosurveillance(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    vision_nuit = models.BooleanField(default=False)
    angle_vue = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)

class SystemeConferenceAudiovisuelle(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    resolution_ecran = models.CharField(max_length=100)
    nombre_micros = models.IntegerField()
    capacite_salles = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    statut = models.CharField(max_length=100)
