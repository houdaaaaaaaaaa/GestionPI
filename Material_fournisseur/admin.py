from django.contrib import admin
from django.contrib.auth.models import User
from users.models import Localisation
from .models import Fournisseur

admin.site.register(Fournisseur)