from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Localisation

# Define an inline admin descriptor for Localisation model
class LocalisationInline(admin.StackedInline):
    model = Localisation
    can_delete = False
    verbose_name_plural = 'localisation'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (LocalisationInline,)
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_department', 'get_numero_de_bureau')

    def get_department(self, obj):
        return obj.localisation.department

    def get_numero_de_bureau(self, obj):
        return obj.localisation.numero_de_bureau

    get_department.short_description = 'Department'
    get_numero_de_bureau.short_description = 'Numero de Bureau'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

