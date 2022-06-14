from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('services', views.about, name="services"),
    path('contact', views.about, name="contact"),
    path('login/', views.login, name="login"),
    path('logout/', views.signout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    ]