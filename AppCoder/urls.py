"""
URL configuration for coderProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""
from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('trabajo/', views.trabajo),
    path('trabajador/', views.trabajador),
    path('empleador/', views.empleador),
    path('crear_trabajo/', views.crear_trabajo),
    path('crear_trabajador/', views.crear_trabajador),
    path('crear_empleador/', views.crear_empleador),
]

