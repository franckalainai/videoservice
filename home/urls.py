from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('course/<slug>/', views.view_course, name='course'),
    path('become_pro/', views.become_pro, name='become_pro')
]