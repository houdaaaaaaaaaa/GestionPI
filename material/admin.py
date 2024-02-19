from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Localisation
from .models import Material,Famille_Material,Fournisseur
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'numero_serie', 'marque', 'duree_garantie', 'duree_vie_debut', 'duree_vie_fin', 'date_affectation', 'statut', 'utilisateur', 'fournisseur', 'famille')

class FamilleMaterialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type')
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'telephone', 'email', 'site_web')
    
admin.site.register(Material, MaterialAdmin)
admin.site.register(Famille_Material,FamilleMaterialAdmin)
admin.site.register(Fournisseur,FournisseurAdmin)