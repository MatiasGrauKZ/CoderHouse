from django.shortcuts import render
from django.http import HttpResponse
from .models import Trabajo, Trabajador, Empleador

def inicio(request):
    return render(request, "inicio.html", {} )

def trabajo(request):
    return render(request, "trabajo.html", {} )

def trabajador(request):
    return render(request, "trabajador.html", {} )

def empleador(request):
    return render(request, "empleador.html", {} )


def crear_trabajo(request):
    print(request)
    print('se ejecuto correctamente')
    return render(request, "crear_trabajo.html",{})

def crear_trabajador(request):
    return render(request, "crear_trabajador.html",{})

def crear_empleador(request):
    return render(request, "crear_empleador.html",{})


