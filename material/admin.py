from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Localisation
from .models import Material, Famille_Material, Fournisseur

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'numero_serie', 'marque', 'duree_garantie', 'duree_vie_debut', 'duree_vie_fin', 'date_affectation', 'statut', 'get_user_username', 'fournisseur', 'famille')
    
    def get_user_username(self, obj):
        return obj.utilisateur.username if obj.utilisateur else ""
    get_user_username.short_description = 'User'

    def save_model(self, request, obj, form, change):
        if not obj.utilisateur and obj.localisation:
            obj.utilisateur = User.objects.filter(localisation=obj.localisation).first()
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            # If creating a new material, hide the utilisateur field
            form.base_fields['utilisateur'].widget = forms.HiddenInput()
        return form

class FamilleMaterialAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type')

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'telephone', 'email', 'site_web')
    
admin.site.register(Material, MaterialAdmin)
admin.site.register(Famille_Material, FamilleMaterialAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
