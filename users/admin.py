from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Localisation

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class LocalisationInline(admin.StackedInline):
    model = Localisation
    can_delete = False
    verbose_name_plural = 'localisation'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (LocalisationInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
