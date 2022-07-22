from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Donnees(models.Model):
    nom = models.CharField(max_length=200, blank=True)
    structure = models.CharField(max_length=255, blank=True)
    ethnie = models.CharField(max_length=300, blank=True)
    population = models.CharField(max_length=300, blank=True)
    annee = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.ethnie

class Utilisateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)