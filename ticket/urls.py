from django.urls import path
from .import views

urlpatterns = [


path('tech/',views.tech,name="tech"),
path('admtech/',views.adm_tech,name="adm_tech"),
path('list/',views.listtech,name='listtech'),
path('resod/',views.resoudre,name='resoudre'),
path('resl/',views.resl,name='resl'),
path('reseaux/',views.reseaux,name='reseaux'),
path('logiciel/',views.logiciel,name='logiciel'),
path('web/',views.web,name='web'),
path('tecket/',views.tecketresul,name='ticket'),
path('rehard/',views.rehard,name='rehard'),
path('logisoft/',views.logisoft,name='logisoft'),
path('matehard/',views.matehard,name='mtehard'),

]