from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Localisation
from Material_fournisseur.models import Fournisseur
from .models import *

@admin.register(CableUSB)
class CableUSBAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('numero_serie', 'marque', 'prix', 'statut', 'utilisateur','fournisseur','date_affectation','date_achat','duree_garantie','duree_vie_debut','duree_vie_fin')
        }),
        ('Autres informations', {
            'fields': ('longueur', 'type_entree', 'type_sortie')
        }),
    )

@admin.register(ServeurPC)
class ServeurPCAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('numero_serie', 'marque', 'prix', 'statut', 'utilisateur')
        }),
        ('Spécifications Serveur PC', {
            'fields': ('processeur', 'memoire_ram', 'capacite_stockage', 'systeme_exploitation')
        }),
    )
