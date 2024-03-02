from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('form/', views.creer_ticket, name='creer_ticket'),
    path('profile/',views.profile,name='profile'),
    path('view/',views.ticket_env,name='viewticket'),
    path('lgoin/',views.lgoin,name='lgoin'),
    path('read/',views.lgout,name='read'),
    path('dash/',views.dashboard,name="dashboard"), 
    
      
]
