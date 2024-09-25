from django.shortcuts import render
from django.http import HttpRequest
from .models import Empleador, Trabajador, Trabajo
from .forms import *

def inicio(request):
    return render(request, "inicio.html", {})

def trabajo(request):
    return render(request, "trabajo.html", {} )

def crear_trabajo(request, nombre):
    nuevo_trabajo=Trabajo(nombre=nombre)
    nuevo_trabajo.save()
    return HttpRequest(f"""<p>trabajo: {nuevo_trabajo.nombre} creado con exito!""")

def crear_trabajo(request):
    if request.method=='POST':
        nuevo_trabajo=Trabajo(nombre=request.POST["nombre"])
        nuevo_trabajo.save()
    else:
        return render(request, 'crear_trabajo.html',{})

def trabajador(request):
    return render(request, "trabajador.html", {} )

def crear_trabajador(request, nombre, apellido, email):
    nuevo_trabajador=Trabajador(nombre=nombre, apellido=apellido, email=email)
    nuevo_trabajador.save()
    return HttpRequest(f"""<p>trabajador: {nuevo_trabajador.nombre} creado con exito!""")

def crear_trabajador(request):
    if request.method=='POST':
        nuevo_trabajador=Trabajador(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
        nuevo_trabajador.save()
    else:
        return render(request, 'crear_trabajador.html',{})

def empleador(request):
    return render(request, "empleador.html", {} )

def crear_empleador(request, nombre, apellido, email):
    nuevo_empleador=Empleador(nombre=nombre, apellido=apellido, email=email)
    nuevo_empleador.save()
    return HttpRequest(f"""<p>Empleador: {nuevo_empleador.nombre} creado con exito!""")

def crear_empleador(request):
    if request.method=='POST':
        nuevo_empleador=Empleador(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
        nuevo_empleador.save()
    else:
        return render(request, 'crear_empleador.html',{})

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




