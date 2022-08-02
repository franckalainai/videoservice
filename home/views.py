from locale import currency
from multiprocessing import context
from django.shortcuts import redirect, render
from . models import *
import stripe
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')

def formules(request):
    return render(request, 'formules.html')

def presentation(request):
    return render(request, 'presentation.html')


def secteurs(request):
    return render(request, 'secteurs.html')

def document(request):
    documents = Document.objects.all()
    context = {
        'documents' : documents
    }
    profile = Profile.objects.filter(user=request.user).first()
    if profile is not None and request.user.is_authenticated:
        
        request.session['profile'] = profile.is_pro
    
    print(context)
    return render(request, 'document.html', context)

def view_document(request, slug):
    document = Document.objects.filter(slug=slug).first()
    document_module = DocumentModule.objects.filter(document=document)

    context = {'document': document, 'document_module': document_module}

    return render(request, 'doc.html', context)

@login_required(login_url='/login/')

def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership', 'MONTHLY')
        amount = 100
        if membership == 'YEARLY':
            amount = 1000
            
        #stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
        #stripe.api_key = "sk_test_qu7ivgHp9WRH1HJjs2QHugIA00hKFbC5qc"
        stripe.api_key = "sk_test_ekHEsZ0D6wMLcJGkenE3PORZ00MGL1bZSp"
        

        customer = stripe.Customer.create(
            email = request.user.email,
            source=request.POST['stripeToken'],
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount * 100,
            currency = 'usd',
            description = 'Membership'
        )

        if charge['paid']==True:
            profile = Profile.objects.filter(user=request.user).first()
            if charge['amount'] == 100000:
                profile.subscription_type = 'M'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(30)
                profile.pro_expiry_date = expiry
                profile.save()
            elif charge['amount'] == 1100000:
                profile.subscription_type = 'Y'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(365)
                profile.pro_expiry_date = expiry
                profile.save()
        return redirect('/charge/')

    return render(request, 'become_pro.html')

def charge(request):
    return render(request, 'charge.html')

def login_attempt(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user is None:
            context = {'message': 'User does not registered'}
            return render(request, 'login.html', context)
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                context = {'message': 'Wrong password'}
                return render(request, 'login.html', context)
            else:
                login(request, user)
                return redirect('document')

    return render(request, 'login.html')

def logout_attempt(request):
    logout(request)
    return redirect('/')


def register_attempt(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            context = {'message': 'User created successfully'}
            return render(request, 'register.html', context)
        else:
            
            context = {'message' : 'User created successfully' , 'class' : 'success'}
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            return render(request, 'register.html', context)

    return render(request, 'register.html', )