from django.contrib.admin import AdminSite
from django.apps import apps

class MaterialAdminSite(AdminSite):
    site_header = 'Material'
    site_title = 'Material'
    index_title = 'Material'

material_admin_site = MaterialAdminSite(name='material')

apps_to_group = [
    'Accessoires',
    'Logiciel',
    'Systemes_De_Refroidissement',
    'Mobilite',
    'Materiel_Audiovisuel',
    'Accessoires_De_Presentation',
    'Equipement_De_Sauvegarde_Et_De_Securite',
    'Imprimantes_Et_Scanners',
    'Périphériques_De_Stockage',
    'Ordinateur_De_Bureau',
    'Ordinateur_Portable',
    'Serveur',
    'Réseau',]

for app_name in apps_to_group:
    
    app = apps.get_app_config(app_name)

    models = app.get_models()
    
    for model in models:
        material_admin_site.register(model)
