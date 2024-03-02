from django.db import models
from django.contrib.auth.models import User



class Localisation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    numero_de_bureau=models.IntegerField()
    def __str__(self):
        return f"{self.department} - {self.numero_de_bureau}"
    