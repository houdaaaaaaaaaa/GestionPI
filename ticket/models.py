from django.db import models
from Material_fournisseur.models import Fournisseur  
from django.contrib.auth.models import User
from django.utils import timezone

class Ticket(models.Model):
    utilisateur= models.ForeignKey(User,on_delete=models.CASCADE)
    technicien= models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='engineer',null=True, blank=True)
    ticket_titre = models.CharField(max_length=50)
    ticket_description = models.TextField()
    status = models.CharField(max_length=20, choices= (('Active','Active'),('panding','panding'),('resolved','resolved')),default=True)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    derniere_modification= models.DateTimeField(auto_now=True)
    niveau= models.CharField(max_length=5, choices=(('A','A'),('B','B'),('c','c')),default='B') 