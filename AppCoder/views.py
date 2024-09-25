from django.shortcuts import render
from django.http import HttpRequest
from .models import Empleador
from .forms import *

def inicio(request):
    return render(request, "inicio.html", {} )

def trabajo(request):
    return render(request, "trabajo.html", {} )

def crear_trabajo(request, nombre):
    nuevo_trabajo=Empleador(nombre=nombre)
    nuevo_trabajo.save()
    return HttpRequest(f"""<p>Empleador: {nuevo_trabajo.nombre} creado con exito!""")

def trabajador(request):
    return render(request, "trabajador.html", {} )

def crear_trabajador(request, nombre, apellido, email):
    nuevo_trabajador=Empleador(nombre=nombre, apellido=apellido, email=email)
    nuevo_trabajador.save()
    return HttpRequest(f"""<p>Empleador: {nuevo_trabajador.nombre} creado con exito!""")

def empleador(request):
    return render(request, "empleador.html", {} )

def crear_empleador(request, nombre, apellido, email):
    nuevo_empleador=Empleador(nombre=nombre, apellido=apellido, email=email)
    nuevo_empleador.save()
    return HttpRequest(f"""<p>Empleador: {nuevo_empleador.nombre} creado con exito!""")

def inicio_sesion(request,):
    return render(request, "inicio_sesion.html", {} )

def crear_trabajo(request):
    print(request)
    print('se ejecuto correctamente')
    return render(request, "crear_trabajo.html",{})

def crear_trabajador(request):
    return render(request, "crear_trabajador.html",{})

def crear_empleador(request):
    return render(request, "crear_empleador.html",{})


