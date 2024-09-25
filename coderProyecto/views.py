from django.http import HttpResponse
from django.template import Template , Context, loader
from AppCoder.views import crea

def inicio(request):
    return HttpResponse('vista inicio')

def trabajo(request):
    return HttpResponse('vista trabajos')

def trabajador(request):
    return HttpResponse('vista trabajador')

def empleador(request):
    return HttpResponse('vista empleador')