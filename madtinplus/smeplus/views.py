from django.shortcuts import redirect, render
from django.contrib.auth import logout

# Create your views here.

def smeplus_home(request):
    return render(request, 'smeplus/sme_home.html')

def sme_dashboard(request):
    return render(request, 'smeplus/sme_dashboard.html')

