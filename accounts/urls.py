from django.urls import path
from . import views

urlpatterns=[
     path('register_/',views.register, name='register_'),
     path('customer_register/',views.customer_register.as_view(), name='customer_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('dashboard/',views.dashboard, name='dashboard'),
     path('sante/',views.sante, name='sante'),
     path('vaccin/',views.vaccin, name='vaccin'),
     path('login_/',views.login_request, name='login_'),
     path('logout/',views.logout_view, name='logout'),
]