from django.contrib import admin
from . models import *

# Register your models here.
class DonneesAdmin(admin.ModelAdmin):
    list_display = ("ethnie", "population")

admin.site.register(Donnees)