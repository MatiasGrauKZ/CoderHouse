from django.shortcuts import render
from django.http import HttpResponse
from .models import Trabajo, Trabajador, Empleador




def inicio(request):
    return HttpResponse('vista inicio')

def trabajo(request):
    return HttpResponse('vista trabajos')

def trabajador(request):
    return HttpResponse('vista trabajador')

def empleador(request):
    return HttpResponse('vista empleador')