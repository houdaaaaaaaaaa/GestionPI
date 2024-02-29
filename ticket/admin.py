from django.contrib import admin
from .models import *
from Material_fournisseur.models import Fournisseur  
from django.contrib.auth.models import User
from django.utils import timezone

admin.site.register(Ticket)