from django.contrib import admin
from .models import *

admin.site.register(Routeur)
admin.site.register(Commutateur)
admin.site.register(PareFeu)
admin.site.register(PointAccesSansFil)

