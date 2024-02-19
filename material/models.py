from django.db import models
from django.contrib.auth.models import User

class Famille_Material(models.Model): 
    nom=models.CharField(max_length=300)
    TYPES_CHOICES = [
        ('hard', 'Matériel informatique'),
        ('soft', 'Logiciel'),
    ]
    type = models.CharField(max_length=300, choices=TYPES_CHOICES)
    def __str__(self):
        return self.nom

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    site_web = models.URLField(blank=True)
    def __str__(self):
        return self.nom
    
class Material(models.Model):
    nom = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
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
    famille = models.ForeignKey(Famille_Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

