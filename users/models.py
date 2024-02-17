from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    num_bureau = models.IntegerField(default=0)

    class Meta(AbstractUser.Meta):
        # Add or change related_name for groups
        permissions = [
            ('view_user', 'Can view user'),
        ]
        db_table = 'custom_user'  # Change to a unique table name
        swappable = 'AUTH_USER_MODEL'  # Add this line

