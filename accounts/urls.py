from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('connexion/', views.connexion, name='connexion'),
    path('enregistrer/', views.enregistrer, name='enregistrer'),
    path('deconnection/', views.deconnection, name='deconnection'),
]