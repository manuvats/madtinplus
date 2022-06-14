from django.contrib import admin
from django.urls import path, include
#from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.smeplus_home, name="smeplus_home"),
    path('sme_dashboard/', views.sme_dashboard, name="sme_dashboard"),
    ]