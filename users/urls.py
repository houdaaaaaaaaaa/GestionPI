from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('form/',views.nw_tick,name='form'),
    path('profile/',views.profile,name='profile'),
    path('view/',views.ticket_env,name='viewticket'),
    path('lgoin/',views.lgoin,name='lgoin'),
    path('read/',views.lgout,name='read'),
    path('dash/',views.dashboard,name="dashboard"), 
    
      
]
