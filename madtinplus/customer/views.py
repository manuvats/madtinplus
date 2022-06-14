from django.shortcuts import redirect, render
from django.contrib.auth import logout
from customer.models import Customer 
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/contact.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.error(request, "You are logged in") 
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials") 
            return redirect('login')

    return render(request, 'home/login.html')

def signout(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'home/dashboard.html')