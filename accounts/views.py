from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from . models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . filters import SanteFilter



def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'accounts/login/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login_')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'accounts/login/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='login_')
def dashboard(request):
    return render(request, 'accounts/dashboard/accueil.html')

@login_required(login_url='login_')
def sante(request):
    return render(request, 'accounts/dashboard/sante/sante.html')


@login_required(login_url='login_')
def vaccin(request):
    donnees = Sante.objects.all()

    myFilter = SanteFilter(request.GET, queryset=donnees)
    donnees = myFilter.qs
    page = request.GET.get('page', 1)

    paginator = Paginator(donnees, 10)
    try:
        donnees = paginator.page(page)
    except PageNotAnInteger:
        donnees = paginator.page(1)
    except EmptyPage:
        donnees = paginator.page(paginator.num_pages)
    context = {
        'donnees': donnees,
        'myFilter': myFilter
    }
    return render(request, 'accounts/dashboard/sante/vaccin.html', context)
