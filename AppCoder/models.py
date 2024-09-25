from django.db import models


class Trabajo(models.Model):
    nombre=models.CharField(max_length=40)

class Trabajador(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

class Empleador(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    ProfesionABuscar=models.CharField(max_length=40)