from django.contrib import admin
from .models import*

class MaterialAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'material_type' in form.base_fields:
            form.base_fields['material_type'].widget.attrs['onchange'] = 'selectMaterialType(this);'
        return form

    class Media:
        js = (
            'material/admin.js',
        )

@admin.register(Hardware)
class HardwareAdmin(MaterialAdmin):
    pass

@admin.register(Software)
class SoftwareAdmin(MaterialAdmin):
    pass
