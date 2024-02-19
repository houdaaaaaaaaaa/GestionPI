from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Localisation
from .models import Material,Famille_Material,Fournisseur
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'numero_serie', 'marque', 'duree_garantie', 'duree_vie_debut', 'duree_vie_fin', 'date_affectation', 'statut', 'utilisateur', 'fournisseur', 'famille')

admin.site.register(Material, MaterialAdmin)
admin.site.register(Famille_Material)
admin.site.register(Fournisseur)