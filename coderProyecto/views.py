from django.http import HttpResponse
from django.template import Template , Context, loader
from AppCoder.models import Trabajo, Trabajador, Empleador


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