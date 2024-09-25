from django.shortcuts import render
from django.http import HttpResponse
from .models import Trabajo, Trabajador, Empleador



def inicio(request):
    return HttpResponse('vista inicio')

def crea_trabajo(request):
    nuevo_trabajo= Trabajo(nombre=nombre, codigo= codigo)
    nuevo_trabajo.save()
    return HttpResponse("""<p> Trabajo: {nuevo_trabajo.nombre}' creado con exito!<p>""")

def crea_trabajador(request):
    nuevo_trabajador= Trabajo(nombre=nombre, apellido= apellido, email= email)
    nuevo_trabajador.save()
    return HttpResponse("""<p> Trabajor: {nuevo_trabajador.nombre}' creado con exito!<p>""")
    

def crea_empleador(request):
    nuevo_empleador= Trabajo(nombre=nombre, apellido= apellido, email= email)
    nuevo_empleador.save()
    return HttpResponse("""<p> Trabajor: {nuevo_trabajador.nombre}' creado con exito!<p>""")