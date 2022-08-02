from logging import PlaceHolder
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

class CustomerSignUpForm(UserCreationForm):
    username = forms.CharField(required=True, label="Nom d'utilisateur")
    first_name = forms.CharField(required=True, label='Nom')
    last_name = forms.CharField(required=True, label='Prénom')
    email = forms.CharField(required=True, label='Email')
    phone_number = forms.CharField(required=True, label='Numéro de téléphone')
    location = forms.CharField(required=True, label='Lieu de résidence')
    password1 = forms.CharField(label='Mot de passe',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(label='Confirmez le mot de passe',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'location')
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.save()
        return user

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number=self.cleaned_data.get('phone_number')
        employee.designation=self.cleaned_data.get('designation')
        employee.save()
        return user
