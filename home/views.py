from locale import currency
from multiprocessing import context
from django.shortcuts import render
from . models import *
import stripe

# Create your views here.
def home(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses
    }
    return render(request, 'home.html', context)

def view_course(request, slug):
    course = Course.objects.filter(slug=slug).first()
    course_module = CourseModule.objects.filter(course=course)

    context = {'course': course, 'course_module': course_module}

    return render(request, 'course.html', context)

def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership', 'MONTHLY')
        amount = 100
            if membership == 'YEARLY':
                amount = 1000
            stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

            customer = stripe.Customer.create(
                email = request.user.email
            )

            charge = stripe.Charge.create(
                customer = customer,
                amount = amount * 100,
                currency = 'usd',
                description = 'membership'
            )

    return render(request, 'become_pro.html')