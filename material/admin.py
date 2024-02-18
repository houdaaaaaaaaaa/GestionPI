from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Localisation
from .models import Material,Famille_Material,Fournisseur

admin.site.register(Famille_Material)
admin.site.register(Fournisseur)
admin.site.register(Material)