from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('document/', views.document, name='document'),
    path('document/<slug>/', views.view_document, name='document'),
    path('become_pro/', views.become_pro, name='become_pro'),
    path('charge/', views.charge, name='charge'),
    path('login/', views.login_attempt, name='login_attempt'),
    path('register/', views.register_attempt, name='register_attempt'),
    path('logout/', views.logout_attempt, name='logout_attempt'),
]