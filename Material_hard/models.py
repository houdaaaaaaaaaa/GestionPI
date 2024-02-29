from django.db import models
from Material_fournisseur.models import Fournisseur  # Assurez-vous que Fournisseur est correctement importé
from django.contrib.auth.models import User

class Material(models.Model):
    numero_serie = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_achat = models.DateField()
    duree_garantie = models.IntegerField()  # En mois par exemple
    duree_vie_debut = models.DateField()
    duree_vie_fin = models.DateField()
    date_affectation = models.DateField(null=True, blank=True)
    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('en_panne', 'En panne'),
        ('en_reparation', 'En réparation'),
    ]
    statut = models.CharField(max_length=100, choices=STATUT_CHOICES)
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    class Meta:
        db_table = 'material'  # Nom de la table dans la base de données

class CableUSB(Material):
    type_entree = models.CharField(max_length=100)
    type_sortie = models.CharField(max_length=100)
    longueur = models.CharField(max_length=100)

class ServeurPC(Material):
    processeur = models.CharField(max_length=100)
    memoire_ram = models.CharField(max_length=100)
    capacite_stockage = models.CharField(max_length=100)
    systeme_exploitation = models.CharField(max_length=100)
