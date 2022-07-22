from multiprocessing import context
from django.shortcuts import redirect, render
from . models import *
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def dashboard(request):
    labels = []
    data = []
    data2 = []
 
    queryset = Donnees.objects.order_by('-population')[:9]
    for city in queryset:
        labels.append(city.ethnie)
        data.append(city.population)
        data2.append(city.annee)

    return render(request, 'accounts/dashboard.html', {
        'labels': labels,
        'data': data,
    })


def connexion(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user is None:
            context = {'message': 'User does not registered'}
            return render(request, 'accounts/connexion.html', context)
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                context = {'message': 'Wrong password'}
                return render(request, 'accounts/connexion.html', context)
            else:
                login(request, user)
                return redirect('dashboard')
    return render(request, 'accounts/connexion.html')

def enregistrer(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            context = {'message': 'User created successfully'}
            return render(request, 'accounts/enregistrer.html', context)
        else:
            
            context = {'message' : 'User created successfully' , 'class' : 'success'}
            user = User(username=username)
            user.set_password(password)
            user.save()

            return render(request, 'accounts/enregistrer.html', context)
    return render(request, 'accounts/enregistrer.html')

def deconnection(request):
    logout(request)
    return redirect('/')