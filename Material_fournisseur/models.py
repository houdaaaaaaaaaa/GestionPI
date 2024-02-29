from django.db import models
from django.contrib.auth.models import User

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    site_web = models.URLField(blank=True)
def __str__(self):
        return self.nom
    
