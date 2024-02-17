from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_bureau= models.models.IntegerField()   
def __str__(self):
        return self.user.username
    
