from django.urls import path
from .import views

urlpatterns = [


path('tech/',views.tech,name="tech"),
path('admtech/',views.adm_tech,name="adm_tech"),
 ]