from django.db import models

class MaterialType(models.TextChoices):
    HARDWARE = 'hardware', 'Hardware'
    SOFTWARE = 'software', 'Software'

class Material(models.Model):
    material_type = models.CharField(
        max_length=10,
        choices=MaterialType.choices,
        default=MaterialType.HARDWARE,
    )

    class Meta:
        abstract = True

class Hardware(Material):
    nom = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    fabricant = models.CharField(max_length=100)
    fournisseur = models.CharField(max_length=100)
    date_achat = models.DateField()
    date_garantie_expiration = models.DateField()
    date_maintenance = models.DateField(blank=True, null=True)
    etat_choices = [
        ('actif', 'Actif'),
        ('en_panne', 'En Panne'),
        ('en_reparation', 'En Réparation'),
        ('en_maintenance', 'En Maintenance'),
        ('obsolete', 'Obsolète'),
    ]
    etat = models.CharField(max_length=20, choices=etat_choices)
    utilisateur_actuel = models.CharField(max_length=100, blank=True, null=True)
    emplacement = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Software(Material):
    nom = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    licence = models.CharField(max_length=100)
    date_achat = models.DateField()
    date_fin_support = models.DateField()
    equipement_utilise = models.ForeignKey(Hardware, on_delete=models.SET_NULL, blank=True, null=True)
    utilisateur_actuel = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom
