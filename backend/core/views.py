from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

def faq(request):
    return render(request, 'faq.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def team(request):
    return render(request, 'team.html')

