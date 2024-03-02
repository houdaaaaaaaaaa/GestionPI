from django import forms
from Ticket.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_titre','ticket_categorie','ticket_description']  # Inclure d'autres champs au besoin
