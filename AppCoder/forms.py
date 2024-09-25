from django import forms

class Crear_empleador(forms.Form):
    nombre= forms.CharField()
    apellido=forms.CharField()
    email=forms.CharField()

class Crear_trabajador(forms.Form):
    nombre= forms.CharField()
    apellido=forms.CharField()
    email=forms.CharField()

class Crear_trabajo(forms.Form):
    nombre= forms.CharField()
    