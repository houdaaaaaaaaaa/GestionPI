from django.contrib import admin
from .models import *
from Material_fournisseur.models import Fournisseur  
from django.contrib.auth.models import User
from django.utils import timezone

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_titre', 'ticket_categorie', 'status', 'date_de_creation', 'derniere_modification', 'niveau')

admin.site.register(Ticket, TicketAdmin)
