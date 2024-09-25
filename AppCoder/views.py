from django.shortcuts import render
from django.http import HttpResponse
from .models import Trabajo, Trabajador, Empleador


def trabajo(request, nombre):
    nuevo_trabajo= Trabajo(nombre=nombre)
    nuevo_trabajo.save()
    return HttpResponse("""<p> Trabajo: {nuevo_trabajo.nombre}' creado con exito!<p>""")

def trabajador(request,nombre,apellido,email):
    nuevo_trabajador= Trabajo(nombre=nombre, apellido= apellido, email= email)
    nuevo_trabajador.save()
    return HttpResponse("""<p> Trabajor: {nuevo_trabajador.nombre}' creado con exito!<p>""")
    

def empleador(request,nombre,apellido,email):
    nuevo_empleador= Trabajo(nombre=nombre, apellido= apellido, email= email)
    nuevo_empleador.save()
    return HttpResponse("""<p> Trabajor: {nuevo_trabajador.nombre}' creado con exito!<p>""")




def inicio(request):
    return render(request, "inicio.html", {} )

def trabajo(request):
    return render(request, "trabajo.html", {} )

def trabajador(request):
    return render(request, "trabajador.html", {} )

def empleador(request):
    return render(request, "empleador.html", {} )