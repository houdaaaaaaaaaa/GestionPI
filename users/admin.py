from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'num_bureau', 'is_staff', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)



